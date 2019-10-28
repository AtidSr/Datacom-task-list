import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input = input("Enter currency (ex 100 THB, 500 JPY, 30 USD, 25 EUR) :")

s.connect(('127.0.0.1', 12345))
s.send(str.encode(input))
time.sleep(0.5)
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.close()
