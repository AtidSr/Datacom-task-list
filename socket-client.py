import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.2.41.7',12345))
s.send(b'id\r\n')
time.sleep(0.5)
msg=s.recv(1024)
print(msg)
s.close()
