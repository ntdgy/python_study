import random

def main():
    f = open('test.in', 'w')
    n = random.randint(int(2e5), (int)(3e5))
    f.write(str(n) + '\n')
    for i in range(n):
        f.write(str(random.randint(1, int(1e9))) + ' ')
    f.close()

if __name__ == '__main__':
    main()