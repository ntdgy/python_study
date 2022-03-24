import subprocess
import sys
import random


def main():
    for i2 in range(20, 21):
        f = open("lab3_2/lab3_2_" + str(i2) + ".in", "w")
        t = random.randint(1e9,1e9+7)  # time
        c = random.randint(1,5)  # capacity
        nest = []  # position of nests
        bunny = []  # position of bunnies
        nest.append(random.randint(-1e9, -1e8))
        bunny.append(random.randint(-1e9, -1e8))
        for i in range(1, random.randint(2e5, 3e5)):
            nest.append(random.randint(nest[i - 1] + 1, nest[i - 1] + 50))
        for i in range(1, random.randint(2e5, 3e5)):
            bunny.append(random.randint(bunny[i - 1] + 1, bunny[i - 1] + 50))
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
