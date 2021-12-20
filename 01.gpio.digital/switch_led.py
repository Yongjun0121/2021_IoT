import RPi.GPIO as GPIO
import time

LED_PIN = 9
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN,val)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
    