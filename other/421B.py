import random


def create():
    writerin = open("test.in", "w")
    writerout = open("testcmp.out", "w")
    k = random.randint(1, 4)
    if k == 1:
        m = random.randint(1, 127)
        n = m
        m = bin(m)
        m = str(m)
        m = m[2:len(m)]
        while len(m) < 7:
            m = '0' + m
        m = '1' + m
        m = int(m)
        writerin.write('1\n')
        writerin.write(hex(m) + '\n')
        writerout.write('1\n')
        writerout.write(str(n) + '\n')
    if k == 2:
        m = random.randint(1, 2047)
        n = m
        m = bin(m)
        m = str(m)
        m = m[2:len(m)]
        while len(m) < 11:
            m = '0' + m
        m1 = m[0:4]
        m2 = m[5:10]
        m1 = '110' + m1
        m2 = '10' + m2
        m1 = int(m1)
        m2 = int(m2)
        writerin.write('2\n')
        writerin.write(hex(m1) + ' ' + hex(m2) + '\n')
        if n > 127:
            writerout.write('2\n')
        else:
            writerout.write('1\n')
        writerout.write(str(n) + '\n')
    if k == 3:
        m = random.randint(1, 65535)
        n = m
        m = bin(m)
        m = str(m)
        m = m[2:len(m)]
        while len(m) < 16:
            m = '0' + m
        m1 = m[0:3]
        m2 = m[4:9]
        m3 = m[10:15]
        m1 = '1110' + m1
        m2 = '10' + m2
        m3 = '10' + m3
        m1 = int(m1)
        m2 = int(m2)
        m3 = int(m3)
        writerin.write('3\n')
        writerin.write(hex(m1) + ' ' + hex(m2) + ' ' + hex(m3) + '\n')
        if n > 2047:
            writerout.write('3\n')
        elif n > 127:
            writerout.write('2\n')
        else:
            writerout.write('1\n')
        writerout.write(str(n) + '\n')


create()
