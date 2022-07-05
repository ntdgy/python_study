import socket

address = ('0.0.0.0', 10000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
while 1:
    data, addr = s.recvfrom(2048)
    if not data:
        break
    with open('log.txt', 'a') as f:
        f.write(str(data) + str(addr) + '\n')
s.close()
