with open('ans.out','r',encoding='utf-8') as f:
    lines = f.readlines()
with open('ans1.out', 'w') as f:
    for line in lines:
        line = line.strip().replace('),', ')')
        print(line)
        f.write(line+'\n')
