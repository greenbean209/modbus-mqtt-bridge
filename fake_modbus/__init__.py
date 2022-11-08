from pubsub import pub
import time
import random
import threading


class modbus_client():
    def __init__(self) -> None:
        pass

    def loop_forever(self):
        while True:
            value = random.random()
            payload = {'metric': 'Voltage', 'value' : value}
            pub.sendMessage('modbus', payload=payload)
            time.sleep(5)

    def loop_start(self):
        thread = threading.Thread(target=self.loop_forever)
        thread.daemon = True
        thread.start()


