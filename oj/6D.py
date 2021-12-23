import random

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

for i2 in range(1, 21, 1):
    writer = open("Y:\\oj\\6D\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(10, 20)
    elif i2 <= 10:
        k = random.randint(100, 1000)
    elif i2 <= 15:
        k = random.randint(1000, 10000)
    elif i2 <= 19:
        k = random.randint(10000, 100000)
    else:
        k = 1000000
    s1 = ''
    s2 = ''
    if i2 > 10:
        for i in range(0, k, 1):
            s1 += char[random.randint(0,25)]
    else:
        for i in range(0, k, 1):
            s1 += char[random.randint(0,5)]
    if i2 > 10:
        for i in range(0, k, 1):
            s2 += char[random.randint(0,25)]
    else:
        for i in range(0, k, 1):
            s2 += char[random.randint(0,5)]
    writer.write(s1)
    writer.write(s2)
