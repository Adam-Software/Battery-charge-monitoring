from JsonWorker import JsonWorker
from servo_voltage.ServoVoltage import *


class ServoVoltageTest:
    servoId = 13
    voltage = ServoVoltage().GetVoltage(servoId)
    JsonWorker.saveToJson(servoId, voltage)
