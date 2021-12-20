import spidev
import time

#SPI인스턴스 생성
spi=spidev.SpiDev()

#SPI 통신시작
spi.open(0, 0)  #(bus:0, dev: 0(CE'0')

#SPI 통신 최대 속도 설정
spi.max_speed_hz = 100000

#0~7 채널에서 SPI데이터 읽기
def analog_read(channel):
    ret = spi.xfer2([1, (channel+8)<<4, 0])
    adc_out = ((ret[1]&3)<<8)+ret[2]
    return adc_out


try:
    while True:
        ldr_value = analog_read(0)
        print("LDR Value = %d" % ldr_value)
        time.sleep(0.5)

finally:
    spi.close()