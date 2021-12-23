import random

for i2 in range(1, 21, 1):
    writer = open("U:\\oj\\5D\\" + str(i2) + ".in", 'w')
    s = ""
    if i2 < 5:
        n = random.randint(10, 20)
    elif i2 < 10:
        n = random.randint(40, 100)
    elif i2 < 16:
        n = random.randint(1000, 3000)
    else:
        n = 100000
    n2 = n
    while (n > 0) & (n2 > 0):
        n1 = random.randint(1, 5)
        if (n1 % 2 == 0) & (n < n2):
            s = s + ')'
            n2 = n2 - 1
        else:
            s = s + '('
            n = n - 1
    while n2 > 0:
        s=s + ')'
        n2 = n2 - 1
    writer.write(s)
    print(s)
