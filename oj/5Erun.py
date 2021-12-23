import subprocess

for i in range(16, 17, 1):
    subprocess.call("./5E <" + str(i) + ".in >" + str(i) + ".out", shell=True)
