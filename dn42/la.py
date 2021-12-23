import subprocess

print("Please input name: ")
name = input()
print("Please input dn42 ipv4: ")
ipv4 = input()
print("Please input Link Local: ")
linklocal = input()
print("Please input wireguard publickey: ")
publickey = input()
print("Please input endpoint: ")
endpoint = input()
print("Please input ASN: ")
asn = int(input())
filename = name + ".conf"
wg = open(filename, 'w')
wg.write("[Interface]\n")
wg.write("PrivateKey = 4F51G3K6d/cP1aflf/QsOiRcIp66Rj1rY2IDUts5pWs=\n")
wg.write("ListenPort = " + str(int(asn % 100000)) + "\n")
wg.write("Table = off\n")
wg.write("PostUp = ip addr add fe80::a0e:fb02/64 dev %i\n")
wg.write("PostUp = ip addr add fd11:552f:74db::1/128 dev %i\n")
if ipv4 != "0":
    wg.write("PostUp = ip addr add 172.23.196.0 peer " + ipv4 + " dev %i\n")
wg.write("PostUp = sysctl -w net.ipv6.conf.%i.autoconf=0\n")
wg.write("[Peer]\n")
wg.write("PublicKey = " + publickey + "\n")
if endpoint != "0":
    wg.write("Endpoint = " + endpoint + "\n")
wg.write("AllowedIPs = 10.0.0.0/8, 172.20.0.0/14, 172.31.0.0/16, fd00::/8, fe80::/64\n")
wg.close()
bird = open("dn42_" + name + ".conf", 'w')
bird.write("protocol bgp dn42_" + name + " from dnpeers {\n")
bird.write("    neighbor " + linklocal + " % '" + name + "' as " + str(asn) + ";\n")
bird.write("    source address fe80::a0e:fb02;\n")
bird.write("};\n")
bird.close()
subprocess.call("mv " + filename + " /etc/wireguard/", shell=True)
subprocess.call("mv " + "dn42_" + name + ".conf" + " /etc/bird/peers", shell=True)
subprocess.call("wg-quick up " + name, shell=True)
subprocess.call("systemctl enable wg-quick@" + name, shell=True)
# time.sleep(3)
subprocess.call("birdc c", shell=True)
# os.system("birdc c")
