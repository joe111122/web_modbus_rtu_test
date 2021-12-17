from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

UNIT = 0x1


def run_sync_client():
    client = ModbusClient(method='rtu', port='com3', baudrate=9600, timeout=1)
    client.connect()
    rr = client.read_holding_registers(address=0x0, count=2, unit=UNIT)
    print(rr)
    print(len(rr.registers))
    time.sleep(0.5) 
    client.close()


if __name__ == "__main__":
    run_sync_client()
