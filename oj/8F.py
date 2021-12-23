import random

for i2 in range(24, 30, 1):
    writer = open("W:\\oj\\8F\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(10, 20)
    elif i2 <= 10:
        k = random.randint(100, 1000)
    elif i2 <= 15:
        k = random.randint(10000, 20000)
    elif i2 <= 19:
        k = random.randint(20000, 100000)
    else:
        k = 400000
    writer.write(str(k) + "\n")
    list1 = [x for x in range(1, k + 1)]
    random.shuffle(list1)
    for i in range(200000):
        b = list1.pop()
        writer.write('1 '+str(b)+'\n')
    for i in range(200000):
        b = list1.pop()
        writer.write('0 '+str(b)+'\n')
# a = random.randint(0, 1)
# b = list1.pop()
# writer.write(str(a) + " " + str(b) + '\n')
