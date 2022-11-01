import unittest
import json
import os
from pathlib import Path
from servo_voltage.JsonWorker import JsonWorker


class JsonWorkerTestCase(unittest.TestCase):

    def test_GetJson(self):
        jsonTest = JsonWorker.GetJson(13, 100)
        dictionary = \
            {
                "servo_id": 13,
                "servo_voltage": 100
            }

        jsonSample = voltage = json.dumps(dictionary, indent=2)

        self.assertEqual(jsonTest, jsonSample)

    def test_SaveJsonDefaultPath(self):
        JsonWorker.SaveToJson(13, 100)
        defaultJsonFilePath = Path('voltage.json')
        fileExist = defaultJsonFilePath.is_file()

        self.assertEqual(fileExist, True)
        os.remove(defaultJsonFilePath)

    def test_SaveJsonCustomPath(self):
        customDirName = 'customDirrectory'
        fileName =  'voltage.json'

        customFilePath = os.path.join(customDirName, fileName)

        if os.path.isdir(customDirName) is False:
            os.mkdir(customDirName)

        JsonWorker.SaveToJson(13, 100, customFilePath)
        defaultJsonFilePath = Path(customFilePath)
        fileExist = defaultJsonFilePath.is_file()

        self.assertEqual(fileExist, True)
        os.remove(customFilePath)
        os.rmdir(customDirName)

    def test_ReadJsonDefaultPath(self):
        defaultJsonFilePath = Path('voltage.json')
        fileExist = defaultJsonFilePath.is_file()
        if fileExist is False:
            JsonWorker.SaveToJson(13, 100)

        jsonTest = JsonWorker.ReadFromJson()
        dictionary = \
            {
                "servo_id": 13,
                "servo_voltage": 100
            }

        jsonSample = json.loads(json.dumps(dictionary, indent=2))

        self.assertEqual(jsonTest, jsonSample)
        os.remove(defaultJsonFilePath)

    def test_ReadJsonCustomPath(self):
        customDirName = 'customDirrectory'
        fileName = 'voltage.json'

        customFilePath = os.path.join(customDirName, fileName)

        if os.path.isdir(customDirName) is False:
            os.mkdir(customDirName)

        fileExist = Path(customFilePath).is_file()
        if fileExist is False:
            JsonWorker.SaveToJson(13, 100, customFilePath)

        jsonTest = JsonWorker.ReadFromJson(customFilePath)
        dictionary = \
            {
                "servo_id": 13,
                "servo_voltage": 100
            }

        jsonSample = json.loads(json.dumps(dictionary, indent=2))

        self.assertEqual(jsonTest, jsonSample)
        os.remove(customFilePath)
        os.rmdir(customDirName)

if __name__ == '__main__':
    unittest.main()
