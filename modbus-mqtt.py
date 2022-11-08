import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()
mqtt_host = os.getenv('MQTT_HOST')
mqtt_port = int(os.getenv('MQTT_PORT'))
mqtt_uname = os.getenv('MQTT_UNAME')
mqtt_pword = os.getenv('MQTT_PWORD')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("modbus-mqtt-bridge/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.tls_set()
mqtt_client.username_pw_set(username=mqtt_uname, password=mqtt_pword)
mqtt_client.connect(host=mqtt_host, port=mqtt_port, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_start()

import time
from pyModbusTCP.client import ModbusClient

modbus_client = ModbusClient(host='127.0.0.1', port=502, unit_id=1, auto_open=True)

if __name__ == "__main__":
    while True:
        time.sleep(1)
        coils = modbus_client.read_coils(0,10)
        print(coils)
        i = 0
        for coil in coils:
            topic = f''
            mqtt_client.publish(f'modbus-mqtt-bridge/127.0.0.1/1/coils/{i}', coil)
            i += 1
