import random


a = []
with open ('gender.txt','r') as f:
    for i in range (56):
        a += (f.readline().splitlines())
print(a)
