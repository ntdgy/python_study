import subprocess


def main():
    subprocess.call("./gettime >time.txt", shell=True)
    f1 = open("time.txt", 'r')
    l = f1.readline()
    l = int(l)
    l = l + 10
    for i in range(100):
        subprocess.call("nc 103.102.44.218 10001", shell=True)
        subprocess.call('1', shell=True)
        subprocess.call('1', shell=True)
        subprocess.call('1 ' + str(l), shell=True)
        subprocess.call('exit', shell=True)


main()