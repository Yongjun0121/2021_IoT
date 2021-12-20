from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN=4


display = drivers.Lcd()


try:
    while True:
        humidity, temperatur = Adafruit_DHT.read_retry(sensor, PIN)
        now=datetime.datetime.now()
        
        display.lcd_display_string(now.strftime("%x%X"), 1)
        display.lcd_display_string(f"{temperatur:.1f}*C, {humidity:.1f}%", 2)

finally:
    display.lcd_clear()