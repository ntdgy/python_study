# -*- coding = utf-8 -*-
# @Time: 2022/4/13 19:35
# @Author: Anshang
# @File: Client.py
# @Software: PyCharm

import socket
from multiprocessing import Process, Pipe


def connection(pipe: Pipe, username, password):
    ip_bind = ("127.0.0.1", 9900)
    c = socket.socket()
    c.connect(ip_bind)
    login = 'login ' + username + ' ' + password
    c.send(bytes(login, encoding='utf-8'))
    permission = str(c.recv(1024), encoding="utf-8")
    print('permission:', permission)
    if permission == '-1':
        raise Exception("Login error")
    while True:
        rec = pipe.recv()
        c.send(bytes(rec, encoding="utf-8"))
        temp = str(c.recv(1024), encoding="utf-8")
        s_send = ''
        while temp != 'finish':
            s_send = s_send + temp
            temp = str(c.recv(1024), encoding="utf-8")
        pipe.send(s_send)


class DBMSClient(object):
    pa, child = Pipe()

    def __init__(self, username, password):
        self.p = Process(target=connection, args=(self.child, username, password))
        self.p.start()
        pass

    def execute(self, sql: str):
        self.pa.send(sql)
        return self.pa.recv()

    def excuse(self, sql: str):
        self.pa.send(sql)
        return self.pa.recv()

    def close(self):
        self.p.terminate()
        self.pa.close()
        self.child.close()


if __name__ == '__main__':
    client = DBMSClient('anshang', '123456')
    client.execute("insert   into supply_center(id, director_name)    values(2, 'name');")
    client.execute("insert   into supply_center(id, director_name)    values(2, 'test');")
    client.execute("insert   into supply_center(id, director_name, supply_center)    values(5, 'test', 'center');")
    client.execute("update supply_center set id = 5, director_name = 'jbjbjb' where id = 2;")
    print(
        client.execute("select * from supply_center where id = '2' and director_name = 'test' or supply_center = 'center';"))
    client.close()
