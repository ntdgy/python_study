import random
from sympy import *

flag = 'flag'
a = 5322682364
b = 4849411009
c = 5218014711
d = 4215800245
encode = [5699462831574115, 6762178137517177, 4904006952609865, 5868227804276587, 9978816733414447, 2555804598727387,
          7339798412634739, 9038863758685179, 4607800653388515, 8591875579876765, 4607800653388515, 2012199806528365,
          761800081770865, 8813480590313107, 718942790851879, 4607800653388515, 8374016791281969, 6040291893502029,
          5533965039300429, 4607800653388515, 4904006952609865, 5056755384110247, 6215687035344625, 6762178137517177,
          638111591795929, 3189435100987729, 9501092313613249, 4607800653388515, 8374016791281969, 7339798412634739,
          4607800653388515, 1622988744649015, 7949410135240279, 9501092313613249, 7539405133434565, 8374016791281969,
          600073811470597, 196738654989577, 10472292506842245]
decode = ''

for x1 in encode:
    flag = False
    for i in range(0, 126):
        re = pow(i, 3) * a + pow(i, 2) * b + i * c + d
        if x1 == int(re):
            decode = decode + chr(i)
            flag = True
    if not flag:
        print(x1)
print(decode)
#     x = sympy.Symbol('x')
#     f = x ** 3 * a + x ** 2 * b + x * c + d - x1
#     result = sympy.solve(f)
#     print(result)

# print('a*' + str(pow(ord(x), 3)) + '+b*' + str(pow(ord(x), 2)) + '+c*' + str(ord(x))+'+d')
# res = (a * pow(ord(x), 3) + b * pow(ord(x), 2) + c * ord(x) + d)
# enc.append(res)