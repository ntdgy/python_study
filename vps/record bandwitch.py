import os
import subprocess
import datetime
import sys


def main():
    f = open('bandwidth.txt')
    time = f.readline()
    sport11 = f.readline()
    sport11 = sport11.split()
    nowdata = subprocess.getstatusoutput("ip6tables -n -v -x -L -t filter | grep spt:10011 | awk '{print $2}'")
    sport11 = int(sport11[1]) + int(nowdata[1])
    sport15 = f.readline()
    sport15 = sport15.split()
    nowdata = subprocess.getstatusoutput("ip6tables -n -v -x -L -t filter | grep spt:10015 | awk '{print $2}'")
    sport15 = int(sport15[1]) + int(nowdata[1])
    dport11 = f.readline()
    dport11 = dport11.split()
    nowdata = subprocess.getstatusoutput("ip6tables -n -v -x -L -t filter | grep dpt:10011 | awk '{print $2}'")
    dport11 = int(dport11[1]) + int(nowdata[1])
    dport15 = f.readline()
    dport15 = dport15.split()
    nowdata = subprocess.getstatusoutput("ip6tables -n -v -x -L -t filter | grep dpt:10015 | awk '{print $2}'")
    dport15 = int(dport15[1]) + int(nowdata[1])
    subprocess.call("ip6tables -Z INPUT 1", shell=True)
    subprocess.call("ip6tables -Z OUTPUT 1", shell=True)
    subprocess.call("ip6tables -Z INPUT 2", shell=True)
    subprocess.call("ip6tables -Z OUTPUT 2", shell=True)
    f.close()
    working_dir = os.getcwd()
    with open("/tmp/my_work_dir.txt", "w") as f:
        f.write(working_dir)
    subprocess.getstatusoutput("rm -rf /root/bandwidth/bandwidth.txt")
    f = open('bandwidth.txt', 'a')
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f.write('Out:10011 ' + str(sport11) + '\n')
    f.write('Out:10015 ' + str(sport15) + '\n')
    f.write('In:10011 ' + str(dport11) + '\n')
    f.write('In:10015 ' + str(dport15) + '\n')
    sum11 = sport11 + dport11
    sum15 = sport15 + dport15
    if sum11 < 1073741824:
        f.write('Sum:10011 ' + str(sum11/1048576) + 'Mb\n')
    else:
        f.write('Sum:10011 ' + str(sum11/1073741824) + 'Gb\n')
    if sum15 < 1073741824:
        f.write('Sum:10015 ' + str(sum15/1048576) + 'Mb\n')
    else:
        f.write('Sum:10015 ' + str(sum15/1073741824) + 'Gb\n')
    f.close()


if __name__ == '__main__':
    main()
