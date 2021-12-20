import RPi.GPIO as GPIO
import time

PIN_LEDR = 4
PIN_LEDY = 5
PIN_LEDG = 22
GPIO.setmode (GPIO.BCM)
GPIO.setup(PIN_LEDR, GPIO.OUT)
GPIO.setup(PIN_LEDY, GPIO.OUT)
GPIO.setup(PIN_LEDG, GPIO.OUT)


for i in range(3):
    GPIO.output(PIN_LEDR, GPIO.HIGH)
    print("RED")
    time.sleep(2)
    GPIO.output(PIN_LEDR, GPIO.LOW)
    GPIO.output(PIN_LEDY, GPIO.HIGH)
    print("YELLOW")
    time.sleep(2)
    GPIO.output(PIN_LEDY, GPIO.LOW)
    GPIO.output(PIN_LEDG, GPIO.HIGH)
    print("GREEN")
    time.sleep(2)
    GPIO.output(PIN_LEDG, GPIO.LOW)
    print("NO SIGNAL")
    time.sleep(2)


GPIO.cleanup()