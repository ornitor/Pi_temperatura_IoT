# Pi_temperatura_IoT

Este programa lê a tempretaura da CPU utilzando um programa utiltario nativo no Raspberry Pi.  Para publicar as mensagens  é necessário configurar com os dados do seu broker.
NAs linhas do codigo, repetidas abaixo:

Configure com dados da instancia do seu broker
MQTT_ADDRESS = 'url do seu broker'
MQTT_PORT = 1883  # configurar  com a porta da instancia do seu broker
MQTT_USER = 'seu user da instancia'
MQTT_PASSWORD = 'sua senha da instancia'
MQTT_TIMEOUT = 60


Exige  a bilioteca Paho.mqtt
Para instalar a biblioteca use:

PIP3 install paho.mqtt

Nao roda em Windows, nem Linux,
