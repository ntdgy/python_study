# -*- coding = utf-8 -*-
# @Time: 2022/4/13 19:31
# @Author: Anshang
# @File: Server.py
# @Software: PyCharm

import socketserver
import fileDBMS
import base64
import json
from multiprocessing import Pipe
from threading import Thread


class MyTcpServerClass(socketserver.BaseRequestHandler):
    def handle(self):
        print("等待新的连接：")
        print("新的客户端:", self.client_address)
        permission = -1
        while True:
            try:
                rec = self.request.recv(1024)
                data = str(rec, encoding="utf-8")
                # print('data', data, type(data))
                if data not in ('', 'done'):
                    # print("客户端:", self.client_address, str(data, encoding="utf-8"))
                    if data.startswith('login'):
                        permission = login(data)
                        self.request.send(bytes(str(permission), encoding="utf-8"))
                        if permission == -1:
                            self.request.close()
                    else:
                        if permission != 1:
                            if not data.startswith('select'):
                                self.request.send(bytes('failed', encoding='utf-8'))
                                continue
                        ans = getSQL(data)
                        if ans is not None:
                            self.request.send(bytes(ans, encoding='utf-8'))
                        self.request.send(bytes('finish', encoding='utf-8'))
                else:
                    self.request.close()
            except OSError:
                print("Client exit")
                self.request.close()
                break


# 1 means superuser, other means read-only
def login(info):
    infos = info.split(' ')
    username = infos[1]
    password = infos[2]
    user = {}
    print('login')
    with open('users.json', 'r') as f:
        user = json.loads(f.read())
    try:
        if user[username]['Password'] == password:
            print('success')
            return user[username]['Permission']
    except KeyError:
        print("User Not Found")
        pass
    return -1


process_list = []  # 内含一个元组。0为通信pipe，1为sql语句


def manager(list__):
    global stop_p
    while True:
        if len(list__) != 0:
            list__[0][0].send(database.excuse(list__[0][1]))
            list__[0][0].close()
            del list__[0]
        else:
            if stop_p:
                break


def getSQL(sql):
    pa, child = Pipe()
    process_list.append((child, sql))
    rec = pa.recv()
    pa.close()
    return rec


def run_forever(server_forever):
    server_forever.serve_forever()


database = fileDBMS.DBMS('test.json')
stop_p = False
if __name__ == '__main__':
    p = Thread(target=manager, args=(process_list, ))
    p.start()
    ip_bind = ("127.0.0.1", 9900)
    server = socketserver.ThreadingTCPServer(ip_bind, MyTcpServerClass)
    # 每次来一个连接，就构建一个实例
    t = Thread(target=run_forever, args=(server, ))
    t.start()
    while True:
        e = input('exit() to end')
        if e == 'exit()':
            database.close()
            server.shutdown()
            server.server_close()
            stop_p = True
            exit()

