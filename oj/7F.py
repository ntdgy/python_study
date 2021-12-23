import queue
import random

for i2 in range(1, 22):
    writer = open("W:\\oj\\7F\\" + str(i2) + ".in", 'w')
    if i2 <= 5:
        k = random.randint(3, 20)
    elif i2 <= 10:
        k = random.randint(10, 1000)
    elif i2 <= 15:
        k = random.randint(10000, 20000)
    elif i2 <= 19:
        k = random.randint(20000, 80000)
    else:
        k = 100000
    i1 = random.randint(1, int(i2 / 2) + 1)
    writer.write(str(i1) + "\n")
    for i in range(i1):
        live = random.randint(2, k)
        writer.write(str(k) + " " + str(live) + "\n")
        list1 = [x for x in range(1, k + 1)]
        root = random.randint(1, k - 1)
        temp = list1[root]
        list1[root] = list1[k - 1]
        list1[k - 1] = temp
        nxt_idx = k - 2
        Que = queue.Queue()
        Que.put(list1[k - 1])
        while not Que.empty():
            now = Que.get()
            cnt = random.randint(1, 10)
            for i1 in range(cnt):
                tmp_idx = random.randint(0, nxt_idx)
                temp = list1[tmp_idx]
                list1[tmp_idx] = list1[nxt_idx]
                list1[nxt_idx] = temp
                if random.randint(1, 2) == 1:
                    writer.write(str(now) + " " + str(list1[nxt_idx]) + "\n")
                else:
                    writer.write(str(list1[nxt_idx]) + " " + str(now) + "\n")
                Que.put(list1[nxt_idx])
                nxt_idx -= 1
                if nxt_idx == -1:
                    break
            if nxt_idx == -1:
                break
        list3 = [x for x in range(1, k + 1)]
        random.shuffle(list3)
        for i1 in range(live):
            writer.write(str(list3.pop()) + " ")
        writer.write("\n")
    writer.close()
