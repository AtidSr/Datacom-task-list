import socket
import time
import re
from datetime import datetime

encoding = 'utf-8'

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)

sock, info = s.accept()
msg = sock.recv(1024)
msgSpl = re.split(r'(\d+)', msg.decode(encoding))

print("input", msgSpl)


def formatString(val, curr, curr1, val1, curr2, val2, curr3, val3):
    strFormat = """Convert %s %s : \n %s %s \n %s %s \n %s %s \n %s""" % (
        val, curr, val1, curr1, val2, curr2, val3, curr3, dt_string)
    return strFormat


def bahtConverter(THB):
    result = formatString(THB, "THB", "EUR", int(
        THB)*0.0298943, "JPY", int(THB)*3.60220, "USD", int(THB)*0.0331184)
    print(result)
    return result


def eurConverter(eur):
    result = formatString(eur, "EUR", "THB", int(
        eur)*33.4523, "JPY", int(eur)*120.504, "USD", int(eur)*1.10804)
    print(result)
    return result


def jpyConverter(jpy):
    result = formatString(jpy, "JPY", "EUR", int(
        jpy)*0.00829805, "THB", int(jpy)*0.277562, "USD", int(jpy)*0.00919518)
    print(result)
    return result


def usdConverter(usd):
    result = formatString(usd, "USD", "EUR", int(
        usd)*0.902448, "JPY", int(usd)*108.754, "THB", int(usd)*30.1867)
    print(result)
    return result


try:

    if msgSpl[2].lower().__contains__("thb") | msgSpl[2].lower().__contains__("baht"):
        sock.send(str.encode(bahtConverter(msgSpl[1])))

    elif msgSpl[2].lower().__contains__("jpy") | msgSpl[2].lower().__contains__("yen"):
        sock.send(str.encode(jpyConverter(msgSpl[1])))

    elif msgSpl[2].lower().__contains__("usd"):
        sock.send(str.encode(usdConverter(msgSpl[1])))

    elif msgSpl[2].lower().__contains__("eur"):
        sock.send(str.encode(eurConverter(msgSpl[1])))

    else:
        sock.send(b'Error invalid input')
        print('Error invalid input 1')

except IndexError:
    sock.send(b'Error invalid input')
    print('Error invalid input 2')

time.sleep(0.3)
s.close()
