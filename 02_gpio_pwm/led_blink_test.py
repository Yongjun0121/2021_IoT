import RPi.GPIO as GPIO
import time

PIN_LEDR = 9
PIN_LEDY = 10
PIN_LEDG = 11
PIN_BUTR = 4
PIN_BUTY = 5
PIN_BUTG = 6
GPIO.setmode (GPIO.BCM)
GPIO.setup(PIN_LEDR, GPIO.OUT)
GPIO.setup(PIN_LEDY, GPIO.OUT)
GPIO.setup(PIN_LEDG, GPIO.OUT)
GPIO.setup(PIN_BUTR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BUTY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BUTG, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



try:
    while True:
        GPIO.output(PIN_LEDR,GPIO.input(PIN_BUTR))
        GPIO.output(PIN_LEDY,GPIO.input(PIN_BUTY))
        GPIO.output(PIN_LEDG,GPIO.input(PIN_BUTG))
        print(GPIO.input(PIN_BUTR),GPIO.input(PIN_BUTY),GPIO.input(PIN_BUTG))
finally:
    GPIO.cleanup()
    print('cleanup and exit')