"""
Team: Michael Qi, David Delgado
Github: https://github.com/davidd82/lab07-pcb
"""
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def ledBlink(x, board_num, interval):
    for i in range(x):
        GPIO.output(board_num, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(board_num, GPIO.LOW)
        time.sleep(interval)

def lightSensor(channel):
    for i in range (50):
        light_val = mcp.read_adc(channel)
        print(light_val)

        if (light_val > 100):
            print("bright")
        else:
            print("dark")
        time.sleep(0.1)

def soundSensor(channel, board_num):
    count = 0
    for i in range(50):
        sound_val = mcp.read_adc(channel)
        print(sound_val)

        if count == 1:
            count = 0
            GPIO.output(board_num, GPIO.LOW)

        if (sound_val > 500):
            GPIO.output(board_num, GPIO.HIGH)
            count+=1
        time.sleep(0.1)

# Main program loop.
while True:
    # LED blinks with 500ms intervals
    ledBlink(5, 11, 0.5)

    # Read light sensor and print value and if dark or bright
    lightSensor(0)

    # LED blinks with 200ms intervals
    ledBlink(4, 11, 0.2)
    
    # Read sound sensor and print value and determine if sensor was tapped
    soundSensor(1,11)

    time.sleep(0.5)