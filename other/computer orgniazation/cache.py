getBinary = lambda x, n: format(x, 'b').zfill(n)



while True:
    a = input()
    st = str(getBinary(int(a), 32))
    print(st)
    print("offset: " + st[28:32] + "  " + str(int(st[28:32], 2)))
    print("index:  " + st[21:28] + "  " + str(int(st[21:28], 2)))
    print("tag:    " + st[0:21] + "  " + str(int(st[0:21], 2)))
    print("\n")

