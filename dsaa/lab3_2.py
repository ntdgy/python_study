import subprocess
import sys
import random


def main():
    for i2 in range(18, 21):
        f = open("lab3_2/lab3_2_" + str(i2) + ".in", "w")
        t = random.randint(1,5000000)  # time
        c = random.randint(1,2000000)  # capacity
        nest = []  # position of nests
        bunny = []  # position of bunnies
        nest.append(random.randint(-1000000000, 0))
        bunny.append(random.randint(-1000000000, 0))
        for i in range(1, random.randint(200000, 100000 * 5)):
            nest.append(random.randint(nest[i - 1] + 1, nest[i - 1] + 500))
        for i in range(1, random.randint(20000 * 10, 100000 * 10)):
            bunny.append(random.randint(bunny[i - 1] + 1, bunny[i - 1] + 500))
        f.write(str(bunny.__len__()) + ' ' + str(nest.__len__()) + ' ' + str(c) + ' ' + str(t) + '\n')
        for i in bunny:
            f.write(str(i) + ' ')
        f.write('\n')
        for i in nest:
            f.write(str(i) + ' ')
        f.write('\n')
        f.close()


if __name__ == "__main__":
    main()
