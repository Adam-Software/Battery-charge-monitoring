#!/usr/bin/env python
#
# *********     Gen Write Example      *********
#
#
# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(STS/SMS/SCS), and an URT
# Be sure that SCServo(STS/SMS/SCS) properties are already set as %% ID : 1 / Baudnum : 6 (Baudrate : 1000000)
#

from collections import Counter
import os
from pickle import TRUE
import time
import sys
import threading


#AUDIO
from pathlib import Path 
import pygame

#init I2C for RGB indicator
import smbus
bus = smbus.SMBus(1)

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
        
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from scservo_sdk import *                    # Uses SCServo SDK library

# Control table address
ADDR_SCS_TORQUE_ENABLE     = 40
ADDR_SCS_GOAL_ACC          = 41
ADDR_SCS_GOAL_POSITION     = 42
ADDR_SCS_GOAL_SPEED        = 46
ADDR_SCS_PRESENT_POSITION  = 56
SCSCL_PRESENT_VOLTAGE      = 62

# Default setting
SCS_ID                      = 13                # SCServo ID : 1
BAUDRATE                    = 1000000           # SCServo default baudrate : 1000000
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

SCS_MINIMUM_POSITION_VALUE  = 487         # SCServo will rotate between this value
SCS_MAXIMUM_POSITION_VALUE  = 1511        # and this value (note that the SCServo would not move when the position value is out of movable range. Check e-manual about the range of the SCServo you use.)
SCS_MOVING_STATUS_THRESHOLD = 20          # SCServo moving status threshold
SCS_MOVING_SPEED            = 0           # SCServo moving speed
SCS_MOVING_ACC              = 0           # SCServo moving acc
protocol_end                = 0           # SCServo bit end(STS/SMS=0, SCS=1)

index = 0
scs_goal_position = [SCS_MINIMUM_POSITION_VALUE, SCS_MAXIMUM_POSITION_VALUE]         # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = PacketHandler(protocol_end)
#Set switch to False
switch = False

def ledonlowpower():
  #Clear RGB Matrix
  mass=[170,255,0,0,0,0,5,0]
  bus.write_i2c_block_data(0x5f,0,mass)
  time.sleep(0.005)
  mass=[170,255,0,0,0,0,5,0]
  bus.write_i2c_block_data(0x5E,0,mass)
  time.sleep(0.005)
  #On Leds of RGB Matrix
  mass = [170, 0xFC, 2, 1, 44, 1, 4,0]
  bus.write_i2c_block_data(0x5F, 0, mass)
  time.sleep(0.005)
  mass = [170, 0xFC, 2, 1, 44, 1, 4,0]
  bus.write_i2c_block_data(0x5E, 0, mass)

def ledofflowpower():
  #Clear RGB Matrix
  mass=[170,255,0,0,0,0,5,0]
  bus.write_i2c_block_data(0x5f,0,mass)
  time.sleep(0.005)
  mass=[170,255,0,0,0,0,5,0]
  bus.write_i2c_block_data(0x5E,0,mass)
  time.sleep(0.005)
    
def readvolfromfile(): 
    global switch 
    with open('/home/pi/adam/batterylevel.txt', 'r') as batterylevrd:
        value = int(batterylevrd.read())

        if (value <= 15 and switch == False):
           threading.Timer(1.0, playmassege).start()
           switch = True
           ledonlowpower()
                      
        if (value > 15 and switch == True): 
           switch = False
           threading.Timer(1.0, playmassege).cancel()
           ledofflowpower()

def playmassege():
    os.system('mplayer "/home/pi/Music/prj-bat-low-15.mp3" & ')
         
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()


while 1:
        
    while 1:
        # Read SCServo voltage position
        scs_present_voltage_speed, scs_comm_result, scs_error = packetHandler.read4ByteTxRx(portHandler, SCS_ID, SCSCL_PRESENT_VOLTAGE)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            print(packetHandler.getRxPacketError(scs_error))
        
        scs_present_voltage  = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)
        percent_voltage = ((scs_present_voltage - 92)/(125 - 92))*100
        
        intvol = int(percent_voltage)
        #print(intvol)

        if intvol in range(0, 100):
          with open('/home/pi/adam/batterylevel.txt', 'w') as batterylevwrite:
              batterylevwrite.write(str(intvol))  
        
        time.sleep(1.0)
        readvolfromfile()
               
        if not (abs(scs_goal_position[index] - scs_present_voltage_speed) > SCS_MOVING_STATUS_THRESHOLD):
            break   
        
            
scs_comm_result, scs_error = packetHandler.write1ByteTxRx(portHandler, SCS_ID, ADDR_SCS_TORQUE_ENABLE, 0)
if scs_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(scs_comm_result))
elif scs_error != 0:
    print("%s" % packetHandler.getRxPacketError(scs_error))

portHandler.closePort()