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
    logger.info(f"Voltage daemon started for servo id {servoId} "
                f"Polling grequency is {pollingFrequency} "
                f"Json file path is {voltageJsonFilePath} ")

    while True:
        voltage = ServoVoltage().GetVoltage(servoId)
        JsonWorker.SaveToJson(servoId, voltage, voltageJsonFilePath)
        time.sleep(pollingFrequency)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Voltage daemon")
    # Мы можем заменить default или запускать приложение с указанием нахождения
    # log файла, через параметр -l /путь_к_файлу/файл.log
    parser.add_argument('-l', '--log-file', default='/home/pi/test_daemon.log')
    parser.add_argument('-s', '--serv-id', default=13)
    parser.add_argument('-t', '--polling-frequency', default=5)
    parser.add_argument('-j', '--json-save-path', default='/home/pi/voltage.json')
    args = parser.parse_args()
    print(parser)
    signal.signal(signal.SIGTERM, terminate)

    fh = logging.FileHandler(args.log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    VoltageUpdate(args.servo_id, args.polling_frequency, args.json_save_path)