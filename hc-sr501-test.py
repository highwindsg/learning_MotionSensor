# https://www.youtube.com/watch?v=_ACe6z-Hp2E&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=57&t=0s

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) # PIR
GPIO.setup(24, GPIO.OUT) # Buzzer

try:
    time.sleep(2) # to stabilize sensor

    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(0.5) # Buzzer turns on for 0.5 sec
            GPIO.output(24, False)
            print("Motion Detected...")
            time.sleep(5) # to avoid multiple detections
        time.sleep(0.1) # loop delay, should be less than detection delay

except:
    GPIO.cleanup()
