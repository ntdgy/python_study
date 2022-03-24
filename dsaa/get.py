import subprocess


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


i = 0
while True:
    if i > 10:
        break
    subprocess.call("python3 lab4_1.py", shell=True)
    i1 = subprocess.getstatusoutput("./run <test.in >test.out")
    i2 = subprocess.getstatusoutput("./cmp <test.in >testcmp.out")
    if i1[0] != 0 or i2[0] != 0:
        print("Error")
        break
    differ = compare_file("test.out", "testcmp.out")
    if len(differ) == 0:
        print('两个文件一样')
    else:
        subprocess.call("mv test.in " + str(i) + ".in", shell=True)
        i = i + 1
        print('发现错误，文件已经保存')
        # print('两个文件共有%d处不同' % len(differ))
        # for each in differ:
        # print('第%d行不同' % each)
        # break;
