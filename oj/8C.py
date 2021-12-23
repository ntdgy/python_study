import random

for i2 in range(1, 10, 1):
    writer = open("U:\\oj\\8C\\" + str(i2) + ".in", 'w')
    a = random.randint(2,5)
    b = random.randint(2,5)
    k = random.randint(1,a*b)
    writer.write(str(a)+" "+str(b)+" "+str(k)+"\n")
    for i in range(a):
        writer.write(str(random.randint(1,20))+" ")
    writer.write("\n")
    for i in range(b):
        writer.write(str(random.randint(1,20))+" ")

