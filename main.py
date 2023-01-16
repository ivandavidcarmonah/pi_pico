import dht
import machine
import time
global temp
global hum
from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import _thread

sin = _thread.allocate_lock()
d = dht.DHT11(machine.Pin(4))

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def test_main():
    print("Running test_main")
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.putstr("It Works!\nSecond Line")
    sleep_ms(3000)
    lcd.clear()
    count = 0
    while True:
        time.sleep(2)
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        lcd.move_to(0, 0)
        lcd.putstr(f"Temperatura: {temp}\nHumedad: {hum}")
#if __name__ == "__main__":
test_main()


