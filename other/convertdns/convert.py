# with open('temp.conf','r') as f:
#     lines = f.readlines()
# with open('re.conf','w') as f:
#     for line in lines:
#         print(line)
#         line = line.replace('server=', '[')
#         line = line.replace('114.114.114.114', ']172.18.1.92')
#         print(line)
#         f.write(line)

with open('china.txt','r') as f:
    lines = f.readlines()
    f1 = open('china1.txt','w')
    f2 = open('china2.txt','w')
    f3 = open('china3.txt','w')
    f4 = open('china4.txt','w')
    f5 = open('china5.txt','w')
    f6 = open('china6.txt','w')
    for i in range(0,1000):
        f1.write(lines[i])
    for i in range(1000,2000):
        f2.write(lines[i])
    for i in range(2000,3000):
        f3.write(lines[i])
    for i in range(3000,4000):
        f4.write(lines[i])
    for i in range(4000,5000):
        f5.write(lines[i])
    for i in range(5000,5451):
        f6.write(lines[i])
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()


