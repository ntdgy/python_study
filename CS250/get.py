import subprocess
import time


def compare_file(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    count = 0
    diff = []
    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            diff.append(count)
    f1.close()
    f2.close()
    return diff


def main():
    i = 1
    while True:
        if i == 10:
            break
        i = i + 1
        subprocess.call("python3 ass1.py", shell=True)
        start = time.clock()
        subprocess.call("./run <input.txt >run.out", shell=True)
        end = time.clock()
        time1 = end - start
        start = time.clock()
        subprocess.call("./cmp <input.txt >cmp.out", shell=True)
        end = time.clock()
        time2 = end - start
        differ1 = compare_file("output.txt", "run.out")
        differ2 = compare_file("output.txt", "cmp.out")
        if len(differ1) == 0 and differ2 == 0:
            print('test case %d passed' % i)
            print("The %d's time of matrix: " % i, time1)
            print("The %d's time of traditional: " % i, time2)
        else:
            print('test case %d failed' % i)
