import random

for i2 in range(1, 22):
    writer = open("W:\\oj\\9F\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(1, 3)
    elif i2 <= 10:
        k = random.randint(1, 5)
    elif i2 <= 15:
        k = random.randint(5, 8)
    elif i2 <= 19:
        k = random.randint(4, 10)
    else:
        k = 10
    writer.write(str(k) + '\n')
    for i1 in range(k):
        if i2 <= 5:
            a = random.randint(2, 10)
            b = random.randint(2, 10)
        elif i2 <= 10:
            a = random.randint(5, 20)
            b = random.randint(5, 20)
        elif i2 <= 15:
            a = random.randint(100, 10000)
            b = random.randint(100, 10000)
        elif i2 <= 19:
            a = random.randint(10000, 100000)
            b = random.randint(10000, 100000)
        else:
            a = 200000
            b = 200000
        writer.write(str(a) + ' ' + str(b) + '\n')
        if i2 <= 5:
            a1 = range(1, a + 1)
            a1 = list(a1)
            random.shuffle(a1)
            for i in range(a):
                writer.write(str(random.randint(1, 5)) + ' ' + str(random.randint(1, 5)) + '\n')
            for i in range(b):
                m1 = random.randint(0, a - 2)
                m2 = random.randint(m1 + 1, a - 1)
                writer.write(str(a1[m1]) + " " + str(a1[m2]) + '\n')
        elif i2 <= 10:
            a1 = range(1, a + 1)
            a1 = list(a1)
            random.shuffle(a1)
            for i in range(a):
                writer.write(str(random.randint(1, 10000)) + ' ' + str(random.randint(1, 10000)) + '\n')
            for i in range(b):
                m1 = random.randint(0, a - 2)
                m2 = random.randint(m1 + 1, a - 1)
                writer.write(str(a1[m1]) + " " + str(a1[m2]) + '\n')
        elif i2 <= 15:
            a1 = range(1, a + 1)
            a1 = list(a1)
            random.shuffle(a1)
            for i in range(a):
                writer.write(str(random.randint(1, 500000)) + ' ' + str(random.randint(1, 500000)) + '\n')
            for i in range(b):
                m1 = random.randint(0, a - 2)
                m2 = random.randint(m1 + 1, a - 1)
                writer.write(str(a1[m1]) + " " + str(a1[m2]) + '\n')
        elif i2 <= 19:
            a1 = range(1, a + 1)
            a1 = list(a1)
            random.shuffle(a1)
            for i in range(a):
                writer.write(str(random.randint(1, 500000)) + ' ' + str(random.randint(1, 5000000)) + '\n')
            for i in range(b):
                m1 = random.randint(0, a - 2)
                m2 = random.randint(m1 + 1, a - 1)
                writer.write(str(a1[m1]) + " " + str(a1[m2]) + '\n')
        else:
            a1 = range(1, a + 1)
            a1 = list(a1)
            random.shuffle(a1)
            for i in range(a):
                writer.write(str(random.randint(1, 500000000)) + ' ' + str(random.randint(1, 500000000)) + '\n')
            for i in range(b):
                m1 = random.randint(0, a - 2)
                m2 = random.randint(m1 + 1, a - 1)
                writer.write(str(a1[m1]) + " " + str(a1[m2]) + '\n')
