import serial
import time

ser = serial.Serial("/dev/tty.SLAB_USBtoUART")
print ('send ID request')
ser.write(b'id\r\n')
time.sleep(0.3)

with ser as c:
    recv = c.readline()
    print(recv.decode())
ser.close()