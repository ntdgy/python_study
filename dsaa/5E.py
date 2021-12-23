import collections


def main():
    try:
        while True:
            deque = collections.deque
            list = [deque]
            list.pop()
            s = input()
            s1 = s.split()
            for i in range(int(s1[0])):
                Deque = collections.deque()
                list.append(Deque)
            for i in range(0,int(s1[1])):
                s = input()
                s2 = s.split()
                if s2[0] == '1':
                    u = int(s2[1]) - 1
                    if s2[2] == '1':
                        list[u].append(s2[3])
                    else:
                        list[u].appendleft(s2[3])
                elif s2[0] == '2':
                    u = int(s2[1]) - 1
                    if len(list[u]) == 0:
                        print(-1)
                    elif s2[2] == '1':
                        print(list[u].pop())
                    else:
                        print(list[u].popleft())
                else:
                    u = int(s2[1]) - 1
                    v = int(s2[2]) - 1
                    if s2[3] == '0':
                        if len(list[v])!=0 :
                            list[u].extend(list[v])
                            list[v].clear()
                    else:
                        if len(list[v])!=0 :
                            list[u].extendleft(list[v])
                            list[v].clear()

    except EOFError:
        pass


main()