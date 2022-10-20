from scservo_sdk import *
from servo_serial.connection import Connection

class ServoVoltage:

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()
    SCSCL_PRESENT_VOLTAGE = 62

    def GetVoltage(self, servoId: int):
        scs_present_voltage_speed, scs_comm_result, scs_error = self.packetHandler.read4ByteTxRx(self.portHandler,
                                                                                                 servoId,
                                                                                                 self.SCSCL_PRESENT_VOLTAGE)
        #if scs_comm_result != COMM_SUCCESS:
        #    print(self.packetHandler.getTxRxResult(scs_comm_result))
        #elif scs_error != 0:
        #    print(self.packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)
        percent_voltage = ((scs_present_voltage - 92) / (125 - 92)) * 100

        voltage = int(percent_voltage)
        return voltage
