import random
import requests

with open('text.txt', 'r') as f:
    line = f.readline()
    line = line.split(" ",3)
    print(line[3])