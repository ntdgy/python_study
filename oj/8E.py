import random

for i2 in range(1, 22, 1):
    writer = open("W:\\oj\\8E\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(10, 20)
    elif i2 <= 10:
        k = random.randint(100, 1000)
    elif i2 <= 15:
        k = random.randint(10000, 20000)
    elif i2 <= 19:
        k = random.randint(20000, 100000)
    else:
        k = 500000
    writer.write(str(k) + "\n")
    for i in range(k):
        if i2 <= 5:
            writer.write(str(random.randint(1, 10)) + " ")
        elif i2 <= 10:
            writer.write(str(random.randint(1, 1000)) + " ")
        elif i2 <= 15:
            writer.write(str(random.randint(1, 10000)) + " ")
        elif i2 <= 19:
            writer.write(str(random.randint(1, 10000000)) + " ")
        else:
            writer.write(str(random.randint(1, 1000000000)) + " ")
