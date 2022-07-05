import random
import requests

with open('text', 'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        line = line.split("	", 2)
        print(line[2].strip())


