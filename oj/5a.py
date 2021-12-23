import random

for i2 in range(6, 17, 1):
    writer = open("U:\\oj\\5A\\" + str(i2) + ".in", 'w')
    s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    if i2 < 5:
        n = random.randint(10, 40)
    elif i2 < 10:
        n = random.randint(100, 1000)
    elif i2 < 16:
        n = random.randint(1000, 3000)
    else:
        n = 10000
    writer.write(str(n) + "\n")
    for i1 in range(0, n, 1):
        n1 = random.randint(1, 3)
        if n1 == 1:
            x = random.randint(0, 9)
            writer.write("NewComer " + s[x] + "\n")
        elif n1 == 2:
            x = random.randint(0, 9)
            writer.write("NewFood " + s[x] + "\n")
        else:
            writer.write("TakeFood\n")
