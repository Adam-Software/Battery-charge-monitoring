from scservo_sdk import *
from servo_serial.connection import Connection
import logging


def logToFile():
    logging.basicConfig(filename='example.log',
                        level=logging.DEBUG)
    return logging.getLogger(__name__)


class ServoVoltage:
    logger = None

    def __init__(self):
        #logging.basicConfig(encoding='utf-8',
        #                    level=logging.DEBUG,
        #                    filename='battery.log',
        #                    filemode='w')

        self.logger = logToFile()
        # self.logger.setLevel(logging.DEBUG)
        # self.logger.addHandler(logging.FileHandler('test_log.log', mode='w'))
        self.logger.info('init battery')

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()
    SCSCL_PRESENT_VOLTAGE = 62

    @staticmethod
    def setLogginLevel(logginLevel):
        logging.getLogger().setLevel(logginLevel)

    @staticmethod
    def getLoggingLevel():
        return logging.getLogger().getEffectiveLevel()

    @staticmethod
    def setLogPath(path):
        logging.basicConfig(filename=path)

    def GetVoltage(self, servoId: int):
        scs_present_voltage_speed, scs_comm_result, scs_error = \
            self.packetHandler.read4ByteTxRx(self.portHandler, servoId, self.SCSCL_PRESENT_VOLTAGE)

        if scs_comm_result != COMM_SUCCESS:
            logging.warning(self.packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            logging.error(self.packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)

        self.logger.warning(scs_present_voltage)
        voltage = self.ToPercent(scs_present_voltage)
        return voltage

    @staticmethod
    def ToPercent(scsPresentVoltage):
        voltage = int(((scsPresentVoltage - 92) / (125 - 92)) * 100)
        return voltage
