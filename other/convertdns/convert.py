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
    for i in range(0,1000):
        with open('china1.txt','a') as f:
            f.write(lines[i])
            f.write('\n')
            f.close()

