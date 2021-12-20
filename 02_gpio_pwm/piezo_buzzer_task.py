import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
note=[4,4,5,5,4,4,2,-1,4,4,2,2,1,-1,4,4,5,5,4,4,2,-1,4,2,1,2,0,-1]

try:
    for i in note:
        if i!=-1:
            pwm.ChangeFrequency(melody[i])
            time.sleep(0.5)
        if i==-1:
            time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()