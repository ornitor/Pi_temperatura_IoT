#   Raspberry publica a temperatura da CPU no Broker MQTT
#   Nao roda em Windows nem Linux
#
#   Configure com od dados do seu Broker

import os
import paho.mqtt.client as mqtt
import sys
import time

from collections import namedtuple

def on_connect(client, userdata, flags, rc):
    global flag_connected
    print('Conectado. Resultado: %s' % str(rc))
    flag_connected = True

def on_disconnect(client, userdata, rc):
    global flag_connected
    flag_connected = False

def mede_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("'C","")
    temp = temp.replace("temp=","")
    temp = temp.replace("\n","")
    return (temp)
    
def send_message(msg):
    global flag_connected
    if not flag_connected:
        client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    result, mid = client.publish('pitemp', msg)
    print('Mensagem enviada ao topico pitemp: {}'.format(msg))

Auth = namedtuple('Auth', ['user', 'password'])   # da instancia do seu broker
MQTT_ADDRESS = 'url do seu broker'
MQTT_PORT = 1883  # configura=e com a porta do instancia do seu broker
MQTT_AUTH = Auth('user,''password')    # da instancia do seu broker
MQTT_TIMEOUT = 60

client = mqtt.Client()

flag_connected = False
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.username_pw_set(MQTT_AUTH[0], MQTT_AUTH[1])
client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
while True:
        temp =  mede_temp()
        send_message(temp)
        time.sleep(2)

