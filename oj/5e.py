import random

for i2 in range(1, 17, 1):
    write = open("U:\\oj\\5E\\" + str(i2) + ".in", 'w')
    times = random.randint(1, 10)
    for i3 in range(0, times, 1):
        if (i2 < 5):
            n = random.randint(2, 10)
            q = random.randint(15, 40)
        elif (i2 < 10):
            n = random.randint(2, 100)
            q = random.randint(100, 150)
        elif (i2 < 16):
            n = random.randint(2, 1000)
            q = random.randint(1000, 10000)
        else:
            n = 10000
            q = 20000
        write.write(str(n) + " " + str(q) + "\n")
        for i1 in range(0, q, 1):
            n1 = random.randint(1, 3)
            if n1 == 1:
                n2 = random.randint(1, n)
                write.write(
                    "1 " + str(n2) + " " + str(random.randint(0, 1)) + " " +
                    str(random.randint(1, 10000)) + "\n")
            if n1 == 2:
                write.write("2 " + str(random.randint(1, n)) + " " + str(random.randint(0, 1)) + "\n")
            if n1 == 3:
                n2 = random.randint(1, n)
                n3 = random.randint(1, n)
                while n2 == n3:
                    n2 = random.randint(1, n)
                    n3 = random.randint(1, n)
                write.write("3 " + str(n2) + " " + str(n3) + " " + str(random.randint(0, 1)) + "\n")
