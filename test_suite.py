import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import grovepi

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11,15]
GPIO.setup(chan_list, GPIO.OUT)
#Following commands control the state of the output
#pin = 11


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# get reading from adc 
# mcp.read_adc(adc_channel)

sound_sensor = 0 #a0
light_sensor = 1 #a1


"""def pushMotor():
    GPIO.output(15, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(15, GPIO.LOW)

def blinkLED(times, pin, interval):
    for i in range(times):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(interval/2)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(interval/2)

def lightSensor(channel):
    for i in range(50):
        print(mcp.read_adc(channel))
        if(mcp.read_adc(channel) > 150): #light sensor
            print("light")
        else:
            print("dark")
        time.sleep(0.1)

def soundSensor(channel, pin):
    for i in range(50):
        print(mcp.read_adc(channel))
        if(mcp.read_adc(channel) > 500): #sound sensor
            #print("clap")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
            #time.sleep(0.1)
        else:
            #print("dark")
            time.sleep(0.1)"""


while True: 
    Port_Sound = 8 #D8
    while True:
        print("Sound: " + str(grovepi.analogRead(sound_sensor)))
        time.sleep(1)
        print("Light: " + str(grovepi.analogRead(light_sensor)))
        time.sleep(1)