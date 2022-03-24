# def main():
#     a = 0
#     for i in range(100, 1000):
#         sum = getSum(i)
#         if compare(i, sum):
#             a += 1
#     print(a)
#             #print(i)
#
#
#
# def getSum(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     return sum
#
# def compare(a,b):
#     while a > 0:
#         if a == b:
#             return True
#         a //= 10
#
#     return False

def main():
    mod = int(1e9 + 7)
    d = int(input())
    if d == 1:
        print("10")
        exit()
    out = ""
    for _ in range(d - 2):
        out += '1'
    out += "9"
    print(int(out) % mod)

if __name__ == '__main__':
    main()
