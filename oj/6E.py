import random


def reverse1(s):
    return s[::-1]


char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

for i2 in range(20, 21, 1):
    writer = open("U:\\oj\\6E\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(10, 20)
    elif i2 <= 10:
        k = random.randint(20, 30)
    elif i2 <= 15:
        k = random.randint(100, 300)
    elif i2 <= 19:
        k = random.randint(200, 400)
    else:
        k = 400
    s = ""
    if i2 > 10:
        for i in range(0, k, 1):
            if random.randint(1, 30) == 1:
                s += reverse1(s)
            else:
                s += char[random.randint(0, 25)]
    else:
        for i in range(0, k, 1):
            if random.randint(1, 5) == 1:
                s += reverse1(s)
            else:
                s += char[random.randint(0, 2)]
    s += reverse1(s)
    s += reverse1(s)
    writer.write(s)
