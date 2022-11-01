# Servo-voltage [![Platforms](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white) [![Language](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) [![IDE](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white) [![adam package](https://img.shields.io/badge/adam_package-red?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Adam-Software)

[![License](https://img.shields.io/github/license/Adam-Software/Servo-voltage)](https://img.shields.io/github/license/Adam-Software/Servo-voltage)
[![Activity](https://img.shields.io/github/commit-activity/m/Adam-Software/Servo-voltage)](https://img.shields.io/github/commit-activity/m/Adam-Software/Servo-voltage)
[![LastStatus](https://img.shields.io/github/last-commit/Adam-Software/Servo-voltage)](https://img.shields.io/github/last-commit/Adam-Software/Servo-voltage)
[![CodeSize](https://img.shields.io/github/languages/code-size/Adam-Software/Servo-voltage)](https://img.shields.io/github/languages/code-size/Adam-Software/Servo-voltage)
[![Depencies](https://img.shields.io/librariesio/github/Adam-Software/Servo-voltage)](https://img.shields.io/librariesio/github/Adam-Software/Servo-voltage)

[![PyPI version](https://badge.fury.io/py/servo-voltage.svg)](https://badge.fury.io/py/servo-voltage)
[![PythonVersion](https://img.shields.io/pypi/pyversions/servo-voltage)](https://img.shields.io/pypi/pyversions/servo-voltage)
[![Wheel](https://img.shields.io/pypi/wheel/servo-voltage)](https://img.shields.io/pypi/wheel/servo-voltage)
[![Status](https://img.shields.io/pypi/status/servo-voltage)](https://img.shields.io/pypi/status/servo-voltage)
[![Format](https://img.shields.io/pypi/format/servo-voltage)](https://img.shields.io/pypi/format/servo-voltage)

### What the library can do?

1. Get the servo voltage value using the feetech sdk
2. Serialize and deserialize voltage values in json

### How install

```commandline
pip install servo-voltage
```

### How to get values using the feetech sdk?

```python
from servo_voltage.ServoVoltage import *

def ServoVoltage():
    servoId = 13
    voltage = ServoVoltage().GetVoltage(servoId)
```

