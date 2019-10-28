import serial
with serial.Serial("/dev/tty.SLAB_USBtoUART") as ser:
    s = ser.readline()
    if (s == b'id\r\n') :
        print(s.decode())
        ser.write(b'6210040999\r\n')
        print("send ID Response:6210040999")
ser.close()
