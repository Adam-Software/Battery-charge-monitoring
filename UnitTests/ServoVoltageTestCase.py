import unittest

class ServoVolatageTestCase(unittest.TestCase):

    def testToPercent(self):
        voltage = int(((0 - 92) / (125 - 92)) * 100)
        print(voltage)
        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
