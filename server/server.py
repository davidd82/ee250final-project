import paho.mqtt.client as mqtt
import time
from flask import Flask, render_template
app = Flask(__name__)

avaibility_global = ""

def avaibility(client, userdata, message):
  print("Lounge Availability is " + str(message.payload, "utf-8"))
  avaibility_global = str(message.payload, "utf-8")


def on_connect(client, userdata, flags, rc):
  print("Connected to server (i.e., broker) with result code "+str(rc))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('Getting status')

  client = mqtt.Client()
  client.connect(host= "test.mosquitto.org", port= 1883, keepalive=60)
  print ('Connected to server')
  client.subscribe("davidd82/available")
  client.message_callback_add("davidd82/available", avaibility)
  client.loop_start()
  client.publish("davidd82/light_and_sound", "STATUS")
  client.publish("davidd82/csv", "MAKE_CSV")

  print('Published message')

  time.sleep(10)

  if(avaibility_global == "0"):
    return("Unavailable")
  elif(avaibility_global == "1"):
    return("Available")
  else:
    return("Fail")

if __name__ == '__main__':
  app.run(debug=True)
  