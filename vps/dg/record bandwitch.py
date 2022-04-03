import os
import subprocess
import datetime
import sys


def main():
    f = open('/root/bandwidth/bandwidth.txt')
    time = f.readline()
    sport11 = f.readline()
    sport11 = sport11.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep spt:10011 | awk '{print $2}'")
    sport11 = int(sport11[1]) + int(nowdata[1])
    sport15 = f.readline()
    sport15 = sport15.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep spt:10015 | awk '{print $2}'")
    sport15 = int(sport15[1]) + int(nowdata[1])
    sport19 = f.readline()
    sport19 = sport19.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep spt:10019 | awk '{print $2}'")
    sport19 = int(sport19[1]) + int(nowdata[1])
    sport20 = f.readline()
    sport20 = sport20.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep spt:10020 | awk '{print $2}'")
    sport20 = int(sport20[1]) + int(nowdata[1])
    dport11 = f.readline()
    dport11 = dport11.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep dpt:10011 | awk '{print $2}'")
    dport11 = int(dport11[1]) + int(nowdata[1])
    dport15 = f.readline()
    dport15 = dport15.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep dpt:10015 | awk '{print $2}'")
    dport15 = int(dport15[1]) + int(nowdata[1])
    dport19 = f.readline()
    dport19 = dport19.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep dpt:10019 | awk '{print $2}'")
    dport19 = int(dport19[1]) + int(nowdata[1])
    dport20 = f.readline()
    dport20 = dport20.split()
    nowdata = subprocess.getstatusoutput("/usr/sbin/ip6tables -n -v -x -L -t filter | grep dpt:10020 | awk '{print $2}'")
    dport20 = int(dport20[1]) + int(nowdata[1])
    subprocess.call("/usr/sbin/ip6tables -Z INPUT 1", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z OUTPUT 1", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z INPUT 2", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z OUTPUT 2", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z INPUT 3", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z OUTPUT 3", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z INPUT 4", shell=True)
    subprocess.call("/usr/sbin/ip6tables -Z OUTPUT 4", shell=True)
    f.close()
    subprocess.getstatusoutput("rm -rf /root/bandwidth/bandwidth.txt")
    f = open('/root/bandwidth/bandwidth.txt', 'w')
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f.write('Out:10011 ' + str(sport11) + '\n')
    f.write('Out:10015 ' + str(sport15) + '\n')
    f.write('Out:10019 ' + str(sport19) + '\n')
    f.write('Out:10020 ' + str(sport20) + '\n')
    f.write('In:10011 ' + str(dport11) + '\n')
    f.write('In:10015 ' + str(dport15) + '\n')
    f.write('In:10019 ' + str(dport19) + '\n')
    f.write('In:10020 ' + str(dport20) + '\n')
    sum11 = sport11 + dport11
    sum15 = sport15 + dport15
    sum19 = sport19 + dport19
    sum20 = sport20 + dport20
    if sum11 < 1073741824:
        f.write('Frankss: ' + str(sum11/1048576) + 'Mb\n')
    else:
        f.write('Frankss: ' + str(sum11/1073741824) + 'Gb\n')
    if sum15 < 1073741824:
        f.write('ipv4: ' + str(sum15/1048576) + 'Mb\n')
    else:
        f.write('ipv4: ' + str(sum15/1073741824) + 'Gb\n')
    if sum19 < 1073741824:
        f.write('ipv6: ' + str(sum19/1048576) + 'Mb\n')
    else:
        f.write('ipv6: ' + str(sum19/1073741824) + 'Gb\n')
    if sum20 < 1073741824:
        f.write('Froster: ' + str(sum20 / 1048576) + 'Mb\n')
    else:
        f.write('Froster: ' + str(sum20 / 1073741824) + 'Gb\n')
    f.close()


if __name__ == '__main__':
    main()
