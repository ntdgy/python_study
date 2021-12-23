import random
import subprocess

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
char1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
for i2 in range(1, 22, 1):
    writer = open("U:\\oj\\6F\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(1, 20)
    elif i2 <= 10:
        k = random.randint(1, 1000)
    elif i2 <= 15:
        k = random.randint(10000, 20000)
    elif i2 <= 19:
        k = random.randint(20000, 100000)
    else:
        k = 500000
    random.shuffle(char)
    for ch in char:
        writer.write(ch + ' ')
    writer.write("\n")
    for i in range(1, k, 1):
        writer.write(char1[random.randint(0, 25)])
    writer.write("\n")
