from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(right=(7, 8), left=(10, 9))

robot.forward()
sleep(2)
robot.right()
sleep(0.6)
robot.backward()
sleep(2.0)
robot.left()
sleep(.4)
robot.forward()
sleep(1)

robot.stop()