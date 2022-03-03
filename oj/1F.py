import random
import numpy as np

writer = open("test.in", 'w')
n = random.randint(1, 10)
writer.write(str(n) + '\n')
for i2 in range(n):
    i = random.randint(2, 10)
    array1 = np.random.randint(1, 5)
    array2 = np.random.randint(array1 + 20, array1 + 30)
    array3 = np.random.randint(array2 + 20, array2 + 30)
    array4 = np.random.randint(array3 + 20, array3 + 30)
    writer.write(str(i) + '\n')
    writer.write(str(array1) + ' ' + str(array2) + ' ' + str(array3) + ' ' + str(array4) + '\n')
    if random.randint(0, 1) == 0:
        list1 = []
        for i3 in range(i):
            if random.randint(0, 1) == 0:
                list1 += [random.randint(array1, array2)]
            else:
                list1 += [random.randint(array3, array4)]
        fixed = random.randint(-100, 100)
        for i5 in list1:
            writer.write(str(i5 + fixed) + ' ')
        writer.write('\n')
    else:
        list1 = []
        for i3 in range(i - 1):
            if random.randint(0, 1) == 0:
                list1 += [random.randint(array1, array2)]
            else:
                list1 += [random.randint(array3, array4)]
        fixed = random.randint(-100, 100)
        list1 += [random.randint(array2 + 10, array3 - 10)]
        for i5 in list1:
            writer.write(str(i5 + fixed) + ' ')
        writer.write('\n')
