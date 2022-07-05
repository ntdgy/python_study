import socket
import time

addrress = input('Enter address: ')
port = input('Enter port: ')
name = input('Enter name: ')
addr = (addrress, int(port))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = time.ctime()
    s.sendto(bytes(name + ': ' + data, 'utf-8'), addr)
    time.sleep(10)
