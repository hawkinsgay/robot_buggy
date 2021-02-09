from gpiozero import Robot, InputDevice, OutputDevice
from time import sleep, time

trig = OutputDevice(4)
echo = InputDevice(17)

olivia = Robot(right=(7,8), left=(10,9))

duration = 8
end_time = time() + duration
running = True

sleep(2)

def get_pulse_time():
    pulse_start, pulse_end = 0, 0
    
    trig.on()
    sleep(0.00001)
    trig.off()

    while echo.is_active == False:
        pulse_start = time()

    while echo.is_active == True:
        pulse_end = time()

    return pulse_end - pulse_start

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance

while running:
    duration = get_pulse_time()
    distance = calculate_distance(duration)
    
    if distance < 0.25:
        olivia.left()
        sleep(0.5)
        olivia.forward()
        sleep(1.0)
        olivia.right()
        sleep(0.5)
    else:
        olivia.forward()
        
    if time() >= end_time:
        running = False
        olivia.stop()

    sleep(0.06)
    
    