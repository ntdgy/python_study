x = input()
count = 0
c = 0
for char in x:
    if char == '0':
        count = count + 1
    if char == ',':
        c = c + 1
print(count)
print(c)
