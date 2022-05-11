# director time is 0.6344184875488281 seconds ---
# client_enterprise time is 3.25417423248291 seconds ---
# salesman time is 15.10814881324768 seconds ---
# product time is 7.0951526165008545 seconds ---
# product_model time is 30.48654055595398 seconds ---
# contract time is 5.375250816345215 seconds ---
# contract_content time is 78.99479484558105 seconds ---


# a = 9.81452488899231 + 158.96950459480286 + 0.6344184875488281 + 3.25417423248291 + 15.10814881324768 + 7.0951526165008545 + 30.48654055595398 + 5.375250816345215 + 78.99479484558105
# print(a)
import random
import requests
import numpy as np
import csv
url = "https://tis.sustech.edu.cn"

while True:
    re = requests.post(url,allow_redirects=False)
    if re.status_code == 200:
        print("success")
        print(re.text)
        break
    else:
        print("fail")
        url = re.headers["Location"]

# for i in range(10):
#     print(random.randint(965, 1000)/10)

