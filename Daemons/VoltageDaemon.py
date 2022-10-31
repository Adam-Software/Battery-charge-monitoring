import time
import argparse
import logging
import sys
import signal

from servo_voltage.JsonWorker import JsonWorker
from servo_voltage.ServoVoltage import *

logger = logging.getLogger('VoltageDaemon')
logger.setLevel(logging.INFO)
formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(formatstr)


def terminate(signalNumber, frame):
    """
    Здесь мы можем обработать завершение нашего приложения
    Главное не забыть в конце выполнить выход sys.exit()
    """


    logger.info(f'Recieved {signalNumber}')
    sys.exit()


def VoltageUpdate(servoId:int, pollingFrequency: float, voltageJsonFilePath: str):
    servoId = 13
    logger.info(f"Voltage daemon started for servo id {servoId}"
                f"Polling grequency is {pollingFrequency} "
                f"Json file path is {voltageJsonFilePath} ")

    while True:
        voltage = ServoVoltage().GetVoltage(servoId)
        JsonWorker.SaveToJson(servoId, voltage, voltageJsonFilePath)
        time.sleep(pollingFrequency)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Voltage daemon")
    parser.add_argument('-l', '--log-file', default='/home/pi/test_daemon.log', help='Log files path')
    parser.add_argument('-s', '--servo-id', default=13,
                        help='Id of the servo with which the voltage will be monitored. The default value is 13')
    parser.add_argument('-t', '--polling-frequency', default=5,
                        help='Frequency of servo polling. The default value is 13')
    parser.add_argument('-j', '--json-save-path', default='/home/pi/voltage.json',
                        help='The storage location of the json file in which the voltage is written')
    args = parser.parse_args()

    signal.signal(signal.SIGTERM, terminate)

    fh = logging.FileHandler(args.log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    VoltageUpdate(args.servo_id, args.polling_frequency, args.json_save_path)