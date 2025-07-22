# from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.serial import AsyncModbusSerialClient as ModbusClient
from pymodbus.client.mixin import ModbusClientMixin
from pymodbus import FramerType
import time
import asyncio
import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

UNIT = 0x1


async def run_sync_client():
    client = ModbusClient(port='COM2', framer=FramerType.RTU,
                          baudrate=9600, timeout=1)
    client.connect()
    rr = client.read_holding_registers(address=0x0, count=2, slave=UNIT)
    value = client.convert_from_registers(
        rr, data_type=ModbusClientMixin.DATATYPE.FLOAT32, word_order="big")
    for i in value:
        print(i)
    print(len(value))
    time.sleep(0.5)
    client.close()


if __name__ == "__main__":
    asyncio.run(run_sync_client())
