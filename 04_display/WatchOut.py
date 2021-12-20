import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
SEGMENT_PINS = [3,4,5,6,7,8,9]
TRIGGER_PIN = 2
ECHO_PIN = 10
BUZZER_PIN = 11
dis = 0

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SEGMENT_PINS, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9


try:
    while True:
        pwm.stop()
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001) # 10us (0.000001s)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = 17160 * duration_time # 거리 = 속력 * 시간, (소리의 속도(34321cm/s)/2)*Time)

        print('Distance : %.1lfcm' % distance)

        if distance < 10:
            pwm.stop()
            GPIO.output(SEGMENT_PINS, GPIO.HIGH)
            print("SEGMENT ON")
            dis = int(distance) #정수 단위로 거리를 변환
            for j in range(7):
                    GPIO.output(SEGMENT_PINS[j], data[dis][j]) #7세그먼트에 거리에 맞게 숫자가 표시되게 함
            if distance < 5:
                pwm.start(0.5) #거리가 5cm미만이면 소리 재생

            
        else:
            GPIO.output(SEGMENT_PINS, GPIO.LOW) #거리가 10cm 이상이면 세그먼트 off
            print("SEGMENT OFF")

        time.sleep(0.1)


finally:
    GPIO.cleanup()
    print(['bye'])