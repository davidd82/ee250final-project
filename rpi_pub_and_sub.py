"""EE 250L Lab 04 Starter Code
Team: Michael Qi, David Delgado
Github: https://github.com/usc-ee250-fall2023/lab-5-mqqt-mordom01

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

from grovepi import *
from grove_rgb_lcd import *

# Hardware SPI configuration
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def light_status(client, userdata, message):
    if (str(message.payload, "utf-8") == "LIGHT_STATUS"):
       for i in range (5):
            light_val = mcp.read_adc(0)
            print(light_val)

            time.sleep(1)

def sound_status(client, userdata, message):
    count = 0
    for i in range(5):
        sound_val = mcp.read_adc(1)
        print(sound_val)
            
        time.sleep(1)


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("davidd82/light")
    client.message_callback_add("davidd82/light", light_status)
    client.subscribe("davidd82/sound")
    client.message_callback_add("davidd82/sound", sound_status)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    time.sleep(1)
    while True:
        time.sleep(1)