#!/usr/bin/python

import serial
import time
import RPi.GPIO as GPIO
import spidev


# This code resets the serial lcd backpack incase things get wonky

port = serial.Serial("/dev/ttyAMA0", baudrate = 9600)

# Send Reset Command
port.write(b'\xFE\x72')
time.sleep(0.05)

# Set screen type to 16x2
port.write(b'\x7C\x04')
time.sleep(0.05)
port.write(b'\x7C\x06')
time.sleep(0.05)

# Send Clear Screen Command
port.write(b'\xFE\x01')
time.sleep(0.05)
