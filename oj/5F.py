import random

for i2 in range(1, 21, 1):
    writer = open("U:\\oj\\5F\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(1, 20)
        q = random.randint(1, 100)
    elif i2 <= 10:
        k = random.randint(1, 1000)
        q = random.randint(500, 1000)
    elif i2 <= 15:
        k = random.randint(1, 2000000)
        q = random.randint(5000, 100000)
    elif i2 <= 19:
        k = random.randint(1, 2000000000)
        q = random.randint(1000000, 2000000)
    else:
        k = 2000000000
        q = 3000000
    writer.write(str(k) + " " + str(q) + "\n")
    s = ""
    for i in range(0, q, 1):
        s += str(random.randint(1, 2000000000)) + " "
    writer.write(s)
