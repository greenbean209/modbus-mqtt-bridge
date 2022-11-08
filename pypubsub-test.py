from pubsub import pub
from fake_modbus import modbus_client
from fake_mqtt import mqtt_client

def modbus_listener(payload):
    metric = payload['metric']
    value = payload['value']
    print('Recieved message from modbus:')
    print(f'Metric = {metric}')
    print(f'Value = {value}')

def mqtt_listener(payload):
    metric = payload['metric']
    value = payload['value']
    print('Recieved message from mqtt:')
    print(f'Metric = {metric}')
    print(f'Value = {value}')

modbus = modbus_client()
mqtt = mqtt_client()

modbus.loop_start()
mqtt.loop_start()

pub.subscribe(modbus_listener, 'modbus')
pub.subscribe(mqtt_listener, 'mqtt')


while True:
    pass