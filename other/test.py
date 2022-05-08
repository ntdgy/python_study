# director time is 0.6344184875488281 seconds ---
# client_enterprise time is 3.25417423248291 seconds ---
# salesman time is 15.10814881324768 seconds ---
# product time is 7.0951526165008545 seconds ---
# product_model time is 30.48654055595398 seconds ---
# contract time is 5.375250816345215 seconds ---
# contract_content time is 78.99479484558105 seconds ---


# a = 9.81452488899231 + 158.96950459480286 + 0.6344184875488281 + 3.25417423248291 + 15.10814881324768 + 7.0951526165008545 + 30.48654055595398 + 5.375250816345215 + 78.99479484558105
# print(a)
import numpy as np
import csv
count = 0
with open('test.txt', 'r',encoding='utf-8') as f:
    a = f.readlines()
    print(len(a))

