import random


def main():
    f = open('test.in', 'w')
    n = random.randint(10, 25)
    m = random.randint(10, 30)
    a = range(1, n + 1)
    a = list(a)
    #random.shuffle(a)
    f.write(str(n) + ' ' + str(m) + ' ' + str(random.randint(1, 10)) + '\n')
    for i in range(n):
        f.write(str(random.randint(1, 10)) + ' ' + str(random.randint(1, 10)) + ' ' + str(
            random.randint(1, 10)) + ' ' + str(random.randint(1, 10)) + '\n')
    for i in range(m):
        m1 = random.randint(0, n - 2)
        m2 = random.randint(m1 + 1, n - 1)
        f.write(str(a[m1]) + " " + str(a[m2]) + '\n')
    f.close()

if __name__ == '__main__':
    main()
