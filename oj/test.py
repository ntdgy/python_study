import random
import collections

def rundata():
    n1 = random.randint(5, 15)
    n2 = random.randint(20, 100)
    string = str(n1) + " " + str(n2) + "\n"
    for i in range(0, n2, 1):
        n3 = random.randint(1, 3)
        if n3 == 1:
            n4 = random.randint(1, n1)
            string += "1 " + str(n4) + " " + str(random.randint(0, 1)) + " " + str(random.randint(1, 100)) + "\n"
        if n3 == 2:
            string += "2 " + str(random.randint(1, n1)) + " " + str(random.randint(1, 2)) + "\n"
        if n3 == 3:
            n5 = random.randint(1, n1)
            n6 = random.randint(1, n1)
            while n5 == n6:
                n5 = random.randint(1, n1)
                n6 = random.randint(1, n1)
            string += "3 " + str(n5) + " " + str(n6) + " " + str(random.randint(1, 2)) + "\n"
    print(string)




def ac():

    d = collections.deque()
    storage = []
    i = 0
    n = int(input())
    i += 1
    q = int(input())
    i += 1
    for i1 in range(0, n, 1):
        storage.append(collections.deque())
    for i1 in range(0, q, 1):
        a = int(input())
        i += 1
        if a == 1:
            u = int(input()) - 1
            i += 1
            w = int(input())
            i += 1
            val = int(input())
            i += 1
            if w == 1:
                storage[u].append(val)
            else:
                storage[u].appendleft(val)
        if a == 2:
            u = int(input()) - 1
            i += 1
            w = int(input())
            i += 1
            if storage[u].__len__() == 0:
                print(-1)
            elif w == 1:
                print(storage[u].pop())
            else:
                print(storage[u].popleft())
        if a == 3:
            u = int(input()) - 1
            i += 1
            v = int(input()) - 1
            i += 1
            w = int(input())
            i += 1
            if w == 0:
                while storage[v].__len__() != 0:
                    storage[u].append(storage[v].popleft())
            else:
                while storage[v].__len__() != 0:
                    storage[u].append(storage[v].pop())

ac()
