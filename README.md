Team: Michael Qi, David Delgado

Link to writeup: https://docs.google.com/document/d/e/2PACX-1vQIVTD7UnpR_TEaYXPr8gLRO2vfN1faGkrDh8bEBwDfNjwy-lR6NtHiWXXWKK8MOHqzvxLMXxhJo8zv/pub

Instructions:
1. RPI must have grovepi sound and light sensors plugged into Adafruit_MCP3008 ports 1 and 0 respectively. Please see writeup and rpi_pub_and_sub.py in github for more reference.
2. On laptop, to run the website front end, cd into the directory of "server" and run python3 server.py to activate the flask server
3. On RPI, stay in the main directory of ee250final-project and run python3 rpi_pub_and_sub.py
4. On laptop, open web browser and go to localhost:5000 to open the flask webpage and click the button
5. Wait ~10 seconds and the webpage should print either available or unavailable.

Libraries Used: paho.mqtt.client, pandas, Adafruit_GPIO.SPI, Adafruit_MCP3008, RPi.GPIO, grovepi, flask, pickle, numpy, sklearn, sys, os, time
