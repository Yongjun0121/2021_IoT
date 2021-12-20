import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)

try:
    time.sleep(2)
    pwm.ChangeDutyCycle(0)

finally:
    pwm.stop()
    GPIO.cleanup()