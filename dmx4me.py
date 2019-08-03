#!/usr/bin/env python3

# DMX4ME v1.0
# Author: Guillermo O. «Tordek» Freschi

import serial
import serial.rs485
import time


in_port = serial.Serial("com5", timeout=0.001)
out_port = serial.rs485.RS485(port="com3",
    baudrate=250000,
    stopbits=serial.STOPBITS_TWO)

data = [0] * 512
while True:
    while True:
        c = in_port.read(8)
        if not c:
            break
        elif c[0] == 67:
            idx = int(c[1:4])
            val = int(c[5:8])
            data[idx] = val
        else:
            print("Unknown message:", c)
    out_port.send_break(0.0001)
    out_port.write(bytes([0] + data))
    time.sleep(0.03)

in_port.close()
out_port.close()
