import time
import argparse
import logging
import sys
import signal
import smbus
import os
import time
import threading

from servo_voltage.JsonWorker import JsonWorker
from servo_voltage.ServoVoltage import *

logger = logging.getLogger('NotificationDaemon')
logger.setLevel(logging.ERROR)
formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(formatstr)

bus = smbus.SMBus(1)

# Set switch to False
switch = False

def terminate(signalNumber, frame):
    logger.info(f'Recieved {signalNumber}')
    sys.exit()

def JsonReadUpdate(pollingFrequency: float,
                   voltageJsonFilePath: str,
                   batteryLevelWarning: int,
                   musicFilePath: str):
    logger.info(f"Polling grequency is {pollingFrequency} "
                f"Json file path is {voltageJsonFilePath} "
                f"Battery level warning {batteryLevelWarning} "
                f"Music file path {musicFilePath}")

    while True:
        global switch
        musicTimer = None
        voltage = JsonWorker.ReadFromJson(voltageJsonFilePath)['servo_voltage']

        if voltage <= batteryLevelWarning and switch == False:
            switch = True

            musicTimer = threading.Timer(1.0, playMessage, [musicFilePath])

            if musicTimer.is_alive() is False:
                musicTimer.start()
                logger.info('timer start')

            logger.info('Warning enable')
            EnableRgbMatrix()

        if voltage > batteryLevelWarning and switch == True:
            switch = False
            if musicTimer is not  None and musicTimer.is_alive():
                musicTimer.cancel()
                logger.info('timer cancel')

            logger.info('Warning disable')
            ClearRgbMatrix()

        time.sleep(pollingFrequency)

def ClearRgbMatrix():
    mass = [170, 255, 0, 0, 0, 0, 5, 0]
    try:
        bus.write_i2c_block_data(0x5E, 0, mass)
        bus.write_i2c_block_data(0x5D, 0, mass)
    except Exception as err:
        logger.error(f"Unexpected rgb clear error {err=}, {type(err)=}")
        pass


def EnableRgbMatrix():
    ClearRgbMatrix()
    mass = [170, 0xFC, 2, 1, 44, 1, 4, 0]
    try:
        bus.write_i2c_block_data(0x5E, 0, mass)
        bus.write_i2c_block_data(0x5D, 0, mass)
    except Exception as err:
        logger.error(f"Unexpected rgb enable {err=}, {type(err)=}")
        pass

def playMessage(musicFilePath: str):
    try:
        os.system(f'ffplay -autoexit -nodisp {musicFilePath}')
    except Exception as err:
        logger.error(f"Unexpected play message {err=}, {type(err)=}")
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notification daemon")
    parser.add_argument('-l', '--log-file', default='/var/log/voltage_daemon.log', help='Log files path')
    parser.add_argument('-t', '--polling-frequency', default=5,
                        help='Frequency of json read polling. The default value is 5')
    parser.add_argument('-j', '--json-save-path', default='/tmp/voltage.json',
                        help='The storage location of the json file in which the voltage reader')
    parser.add_argument('-w', '--warning-battery-level', default=15,
                        help='The battery charge level at which alerts are activated')
    parser.add_argument('-m', '--music-file-path', default='bat-low-15.mp3',
                        help='Music file for alerts')

    args = parser.parse_args()

    signal.signal(signal.SIGTERM, terminate)

    fh = logging.FileHandler(args.log_file)
    fh.setLevel(logging.ERROR)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    JsonReadUpdate(float(args.polling_frequency), args.json_save_path, int(args.warning_battery_level), args.music_file_path)
