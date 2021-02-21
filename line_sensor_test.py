from gpiozero import Robot, LineSensor
from time import sleep
from signal import pause
#import RPi.GPIO as GPIO

left_sensor = LineSensor(pin=21, pull_up=None, active_state=True)
#right_sensor = LineSensor(20)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(21, GPIO.IN)

try:
    while True:
        if left_sensor.when_no_line:
            print('White')
        else:
            print("Black")

except:
    left_sensor.close()