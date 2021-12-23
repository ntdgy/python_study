import random

writer = open("test.in", 'w')
a = random.randint(5, 15)
b = random.randint(10, 15)
writer.write(str(a) + " " + str(b) + " " + "\n")
for i1 in range(b):
    m1 = random.randint(1, a)
    m2 = random.randint(1, a)
    m3 = random.randint(10, int(10e9))
    while m1 == m2:
        m1 = random.randint(1, 2)
        m2 = random.randint(1, 2)
    writer.write(str(m1) + " " + str(m2) + ' ' + str(m1) + '\n')
