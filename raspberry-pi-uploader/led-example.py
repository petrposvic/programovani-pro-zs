#!/usr/bin/python3
# Example what you can send to webserver
import RPi.GPIO as GPIO
import time

pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
