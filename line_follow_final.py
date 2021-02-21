from gpiozero import Robot, LineSensor
from time import sleep, time 

robin = Robot(right=(7, 8), left=(10, 9))

left_sensor = LineSensor(21)
right_sensor = LineSensor(20)

#robin.forward()

#left_sensor.when_no_line = robin.left
#right_sensor.when_no_line = robin.right
#left_sensor.when_line = robin.forward
#right_sensor.when_line = robin.forward

speed = 0.8

duration = 11
end_time = time() + duration

running = True

while running:
    left_detect  = left_sensor.value
    right_detect = right_sensor.value
    
    
    # Rule 1
    if left_detect == 0 and right_detect == 0:
        left_mot = 1
        right_mot = 1
    # Rule 2
    elif left_detect == 1:
        left_mot = -1
        right_mot = 1
    # Rule 3
    elif right_detect == 1:
        left_mot = 1
        right_mot = -1

    robin.left_motor.value = left_mot * speed
    robin.right_motor.value = right_mot * speed 

    if time() >= end_time:
        running = False
        robin.stop()
        robin.close()
        left_sensor.close()
        right_sensor.close()
