import hashlib

def main():
    data = "cm++kg"
    hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    print(hash)

    # for i in range(160,190):
    #     for j in range(170,220):
    #         data = str(j) + '++' + str(i)
    #         md5 = hashlib.md5(data.encode('utf-8')).hexdigest()
    #         if md5 == '15e818cd53e6b44e814f6707e0254960':
    #             print(i,j)

if __name__ == '__main__':
    main()