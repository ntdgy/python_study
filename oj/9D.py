import random

for i2 in range(1, 30):
    writer = open("W:\\oj\\9D\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(1, 3)
    elif i2 <= 10:
        k = random.randint(1, 10)
    elif i2 <= 15:
        k = random.randint(1, 10)
    elif i2 <= 19:
        k = random.randint(1, 20)
    else:
        k = 20
    writer.write(str(k) + '\n')
    for i1 in range (k):
        if i2 <= 5:
            a = random.randint(2, 3)
            b = random.randint(2, 3)
        elif i2 <= 10:
            a = random.randint(2, 4)
            b = random.randint(2, 4)
        elif i2 <= 15:
            a = random.randint(3, 6)
            b = random.randint(3, 6)
        elif i2 <= 19:
            a = random.randint(3, 6)
            b = random.randint(3, 6)
        else:
            a = 6
            b = 6
        writer.write(str(a) + ' ' + str(b) + '\n')
        if i2 <= 5:
            for i in range(a):
                for i in range(b):
                    writer.write(str(random.randint(1, 10)) + ' ')
                writer.write('\n')
        elif i2 <= 10:
            for i in range(a):
                for i in range(b):
                    writer.write(str(random.randint(1, 500)) + ' ')
                writer.write('\n')
        elif i2 <= 15:
            for i in range(a):
                for i in range(b):
                    writer.write(str(random.randint(1, 1000)) + ' ')
                writer.write('\n')
        elif i2 <= 19:
            for i in range(a):
                for i in range(b):
                    writer.write(str(random.randint(1, 1000)) + ' ')
                writer.write('\n')
        else:
            for i in range(a):
                for i in range(b):
                    writer.write(str(random.randint(1, 100000)) + ' ')
                writer.write('\n')
