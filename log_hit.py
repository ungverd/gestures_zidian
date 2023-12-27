import asyncio
import struct
from bleak import BleakClient

address = "F8:3A:7B:7A:6A:04"
CHAR_UUID = '0000278A-0000-1000-8000-00805f9b34fb'
ACC_UUID = '00002789-0000-1000-8000-00805f9b34fb'
FN = "data3"

i = [0]
f = open(f"{FN}_{i[0]}.txt", "w")
ff = [f]
fflag = []

def notification_handler(sender, data):
    floats = struct.unpack('3f', data)
    ff[0].write(f"{floats[0]} {floats[1]} {floats[2]}\n")

def notification_handler_char(sender, data):
    if data == b's':
        f.close()
        i[0] += 1
        ff[0] = open(f"{FN}_{i[0]}.txt", "w")
        print(i[0])
    elif data == b'n':
        ff[0].close()
        fflag[0].set()

async def main(address):
    flag = asyncio.Event()
    fflag.append(flag)
    async with BleakClient(address) as client:
        await client.start_notify(ACC_UUID, notification_handler)
        await client.start_notify(CHAR_UUID, notification_handler_char)
        await flag.wait()
        await client.stop_notify(ACC_UUID)
        await client.stop_notify(CHAR_UUID)

asyncio.run(main(address))

