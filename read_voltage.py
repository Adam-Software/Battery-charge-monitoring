#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import os
import time
import threading

from servo_voltage.JsonWorker import JsonWorker

# init I2C for RGB indicator
bus = smbus.SMBus(1)

# Set switch to False
#switch = False


def ledOnPower():
    # Clear RGB Matrix
    mass = [170, 255, 0, 0, 0, 0, 5, 0]
    bus.write_i2c_block_data(0x5f, 0, mass)
    time.sleep(0.005)
    mass = [170, 255, 0, 0, 0, 0, 5, 0]
    bus.write_i2c_block_data(0x5E, 0, mass)
    time.sleep(0.005)

    # On Leds of RGB Matrix
    mass = [170, 0xFC, 2, 1, 44, 1, 4, 0]
    bus.write_i2c_block_data(0x5F, 0, mass)
    time.sleep(0.005)
    mass = [170, 0xFC, 2, 1, 44, 1, 4, 0]
    bus.write_i2c_block_data(0x5E, 0, mass)


def ledOffPower():
    # Clear RGB Matrix
    mass = [170, 255, 0, 0, 0, 0, 5, 0]
    bus.write_i2c_block_data(0x5f, 0, mass)
    time.sleep(0.005)

    mass = [170, 255, 0, 0, 0, 0, 5, 0]
    bus.write_i2c_block_data(0x5E, 0, mass)
    time.sleep(0.005)


def readFromFile():
    #global switch
    # with open('/home/pi/adam/batterylevel.txt', 'r') as batteryLevelFile:
    voltage = JsonWorker.ReadFromJson()['servo_voltage']

    if voltage <= 15: # and switch == False:
        threading.Timer(1.0, playMessage).start()
        #switch = True
        ledOnPower()

    if voltage > 15: # and switch == True:
        #switch = False
        threading.Timer(1.0, playMessage).cancel()
        ledOffPower()


def playMessage():
    os.system('mplayer "/home/pi/Music/prj-bat-low-15.mp3" & ')

# while 1:
#    servo_voltage = ServoVoltage().GetVoltage(13)
#
#    if servo_voltage in range(0, 100):
#        with open('/home/pi/adam/batterylevel.txt', 'w') as batterylevwrite: batterylevwrite.write(str(servo_voltage))
#
#        time.sleep(1.0)
#        readFromFile()
