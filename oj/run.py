import subprocess

for i in range(1, 22, 1):
    subprocess.call("./run <" + str(i) + ".in >" + str(i) + ".out", shell=True)