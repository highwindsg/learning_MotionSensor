#!/usr/bin/env python3

from gpiozero import MotionSensor
from gpiozero import Buzzer
from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buzzer_pin = 24
led_pin = 18
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
camera = PiCamera()
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.capture("/home/pi/Desktop/image.jpg")
    camera.start_recording(filename)
    GPIO.output(buzzer_pin, True)
    GPIO.output(led_pin, True)
    sleep(1)
    GPIO(1)
    GPIO.output(buzzer_pin, False)
    pir.wait_for_no_motion()
    GPIO.output(led_pin, True)
    GPIO.putput(buzzer_pin, True)
    sleep(1)
    GPIO.output(buzzer_pin, False)
    camera.stop_recording()

