import time
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host='127.0.0.1', port=502, unit_id=1, auto_open=True)

if __name__ == "__main__":
    while True:
        time.sleep(5)
        coils = c.read_coils(0,10)
        print(coils)