import random


def main():
    for i2 in range(1, 25):
        f = open("lab4_2/" + str(i2) + ".in", "w")
        if i2 <= 5:
            a = random.randint(5, 20)
            b = random.randint(10, 40)
        elif i2 <= 10:
            a = random.randint(20, 50)
            b = random.randint(50, 100)
        elif i2 <= 15:
            a = random.randint(1000, 5000)
            b = random.randint(1000, int(1e9))
        elif i2 <= 20:
            a = random.randint(10000, 50000)
            b = random.randint(int(9e8), int(1e9))
        else:
            a = random.randint(int(9e4), int(1e5))
            b = random.randint(int(9e8), int(1e9))
        f.write(str(a) + " " + str(b) + "\n")
        for i in range(a):
            if i2 <= 5:
                f.write(str(random.randint(10, 100)) + " ")
            elif i2 <= 10:
                f.write(str(random.randint(100, 1000)) + " ")
            elif i2 <= 15:
                f.write(str(random.randint(10000, 100000)) + " ")
            elif i2 <= 20:
                f.write(str(random.randint(int(1e5), int(1e8))) + " ")
            else:
                f.write(str(random.randint(int(9e8), int(1e9))) + " ")
        for i in range(a):
            if i2 <= 5:
                f.write(str(random.randint(10, 100)) + " ")
            elif i2 <= 10:
                f.write(str(random.randint(100, 1000)) + " ")
            else:
                f.write(str(random.randint(9000, 10000)) + " ")
        f.close()

if __name__ == '__main__':
    main()
