import icmp_test
import subprocess
import send
import datetime
import time


def check_latency(domain):
    min, avg, max, lost = icmp_test.shend_icmp_packet(domain, '8')
    message = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
    if float(avg) > 100:
        message += domain + 'test failed: latency too long.\n'
        message += 'min: ' + min + 'ms\n'
        message += 'avg: ' + avg + 'ms\n'
        message += 'max: ' + max + 'ms\n'
        message += 'lost: ' + lost + '\n'
        message += 'Trying get a new ip!\n'
        if domain.find('v4') != -1:
            changeIpv4()
        else:
            changeIpv6()
        ip = subprocess.getoutput('cat /etc/hosts | grep ' + domain)
        message += 'New ip: ' + ip + '\n'
        with open('log.txt', 'a') as f:
            f.write(message)
        send.sendMessage(message)
        return False
    elif float(lost) > 50:
        message += domain + 'test failed: too many packets lost.\n'
        message += 'min: ' + min + 'ms\n'
        message += 'avg: ' + avg + 'ms\n'
        message += 'max: ' + max + 'ms\n'
        message += 'lost: ' + lost + '\n'
        message += 'Trying get a new ip!\n'
        if domain.find('v4') != -1:
            changeIpv4()
        else:
            changeIpv6()
        ip = subprocess.getoutput('cat /etc/hosts | grep ' + domain)
        message += 'New ip: ' + ip + '\n'
        with open('log.txt', 'a') as f:
            f.write(message)
        send.sendMessage(message)
        return False
    else:
        message += domain + 'test passed: latency is normal.\n'
        message += 'min: ' + min + 'ms\n'
        with open('log.txt', 'a') as f:
            f.write(message)
        return True


def changeIpv4():
    changeIp = subprocess.getoutput('cd /root/CloudflareST && ./cfst_hosts.sh')
    return changeIp

def changeIpv6():
    changeIp = subprocess.getoutput('cd /root/CloudflareST && ./cfst_hosts_v6.sh')
    return changeIp



def main():
    while True:
        countv4 = 0
        countv6 = 0
        domain1 = 'v4.test8.sustc.icu'
        domain2 = 'v6.hk.cf.sustc.icu'
        while countv4 <= 3:
            if check_latency(domain1) == False:
                countv4 += 1
            else:
                break
        while countv6 <= 3:
            if check_latency(domain2) == False:
                countv6 += 1
            else:
                break
        time.sleep(60)

if __name__ == '__main__':
    main()

