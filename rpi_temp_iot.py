#   Raspberry publica a temperatura da CPU no Broker MQTT
#   Exige  a bilioteca Paho.mqtt
#   para instalar use PIP3 install paho.mqtt
#   Nao roda em Windows nem Linux
#
#   Configure com od dados do seu Broker

import os
import paho.mqtt.client as mqtt
import sys
import time
from collections import namedtuple


## Configure com dados da instancia do seu broker
MQTT_ADDRESS = 'url do seu broker'
MQTT_PORT = 1883  # configurar  com a porta da instancia do seu broker
MQTT_USER = 'seu user da instancia'
MQTT_PASSWORD = 'sua senha da instancia'
MQTT_TIMEOUT = 60
 

def on_connect(client, userdata, flags, rc):
    global flag_connected
    print('Conectado. Resultado: %s' % str(rc))
    flag_connected = True

def on_disconnect(client, userdata, rc):
    global flag_connected
    flag_connected = False

def mede_temp():
    name = os.popen("hostname").readline().replace("\n","")
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("'C","")
    temp = temp.replace("temp=","")
    temp = temp.replace("\n","")
    return (temp)
    
def send_message(topic,msg):
    global flag_connected
    if not flag_connected:
        client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    result, mid = client.publish(topic, msg)
    print('Mensagem enviada ao topico pitemp: {}'.format(msg))


client = mqtt.Client()

flag_connected = False
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.username_pw_set(MQTT_USER ,MQTT_PASSWORD ) 
client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

while True:
        temp =  mede_temp()
        topic = 'pitemp/'+ os.popen("hostname").readline().replace("\n","")
        send_message(topic,temp)
        time.sleep(2)

