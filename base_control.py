import RPi.GPIO as gpio
import time

#basic control functions
"""
A module that contains basic controls interfacing with the L298N dc motor driver, a
simple function for each of the 4 directions has been implemented.

"""

def init():
    #initialization function
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)

def reverse(sec):
    # reverse direction 
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(sec)
    gpio.cleanup()
    
def forward(sec):
    # forward direction
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(sec)
    gpio.cleanup()

def right_turn(sec):
    # right turn 
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(sec)
    gpio.cleanup()

def left_turn(sec):
    # left turn
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(sec)
    gpio.cleanup()
