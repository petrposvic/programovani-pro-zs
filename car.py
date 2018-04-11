#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Nastaveni jmen PINu podle BCM (ne podle BOARD)
GPIO.setmode(GPIO.BCM)

# Nastavení PINu do modu zapisovani
GPIO.setup(2,  GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(2, GPIO.HIGH)
time.sleep(1)
GPIO.output(2, GPIO.LOW)

enA = GPIO.PWM(18, 50)
enB = GPIO.PWM(19, 50)
enA.start(0)
enB.start(0)

def forward():
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

def backward():
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

def startA():
    enA.ChangeDutyCycle(50)

def stopA():
    enA.ChangeDutyCycle(0)

def startB():
    enB.ChangeDutyCycle(50)

def stopB():
    enB.ChangeDutyCycle(0)

forward()
startA()
startB()
time.sleep(3)
stopA()
stopB()
enA.stop()
enB.stop()
GPIO.cleanup()

