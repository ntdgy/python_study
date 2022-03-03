import random

a = random.randint(3, 5)
b = random.randint(a, 7)
print(str(a) + ' ' + str(b))
for i in range(b):
    a1 = random.randint(1,a)
    a2 = random.randint(1,a)
    while a1 == a2:
        a1 = random.randint(1, a)
        a2 = random.randint(1, a)
    print(str(a1)+' '+str(a2))
