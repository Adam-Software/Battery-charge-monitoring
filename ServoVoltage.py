from scservo_sdk import *
from servo_serial.connection import Connection
from loguru import logger


class ServoVoltage:
    def __init__(self):
        logger.add('battery.log', retention="10 days", level="Error")

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()
    SCSCL_PRESENT_VOLTAGE = 62

    def GetVoltage(self, servoId: int):
        scs_present_voltage_speed, scs_comm_result, scs_error = \
            self.packetHandler.read4ByteTxRx(self.portHandler, servoId, self.SCSCL_PRESENT_VOLTAGE)

        if scs_comm_result != COMM_SUCCESS:
            logger.warning(self.packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            logger.error(self.packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)

        voltage = self.ToPercent(scs_present_voltage)
        logger.error(voltage)
        return voltage

    @staticmethod
    def ToPercent(scsPresentVoltage):
        voltage = int(((scsPresentVoltage - 92) / (125 - 92)) * 100)
        return voltage
