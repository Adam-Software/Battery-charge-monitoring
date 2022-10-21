#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scservo_sdk import *
from servo_serial.connection import Connection
from loguru import logger

portHandler = Connection().getPortHandler()
packetHandler = Connection().getPacketHandler()
SCSCL_PRESENT_VOLTAGE = 62


def _readTx(servoId):
    scs_present_voltage_speed, scs_comm_result, scs_error = \
        packetHandler.read4ByteTxRx(portHandler,
                                    servoId,
                                    SCSCL_PRESENT_VOLTAGE)

    return scs_present_voltage_speed, scs_comm_result, scs_error


def ToPercent(scsPresentVoltage):
    voltage = int(((scsPresentVoltage - 92) / (125 - 92)) * 100)
    return voltage


class ServoVoltage:

    logger.remove()
    logger.add('battery.log', retention="5 MB", level="ERROR")

    @staticmethod
    def GetVoltage(servoId: int):
        scs_present_voltage_speed, scs_comm_result, scs_error = _readTx(servoId)

        if scs_comm_result != COMM_SUCCESS:
            logger.warning(packetHandler.getTxRxResult(scs_comm_result))

        if scs_error != 0:
            logger.error(packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)

        voltage = ToPercent(scs_present_voltage)
        return voltage
