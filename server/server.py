import paho.mqtt.client as mqtt
import time
from flask import Flask, render_template
app = Flask(__name__)

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
  client.loop_start()
  client.publish("davidd82/light", "LIGHT_STATUS")
  client.publish("davidd82/sound", "SOUND_STATUS")
  print('Published message')

  
  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
  