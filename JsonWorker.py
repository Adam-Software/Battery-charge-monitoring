import json


class JsonWorker:
    dictionary = None

    @staticmethod
    def saveToJson(servoId: int, servoVoltage: int):
        dictionary = \
            {
                "servo_id": servoId,
                "servo_voltage": servoVoltage
            }

        voltage = json.dumps(dictionary, indent=2)
        with open("voltage.json", "w") as outfile:
            outfile.write(voltage)

