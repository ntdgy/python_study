import random
import time

def generate_delete_test()->list:
    delete_test = []
    numset = set()
    for i in range(0, 1000):
        while True:
            random_num = random.randint(0, 1000000)
            if random_num not in numset:
                numset.add(random_num)
                break
        delete_test.append('''
        delete from contract_content where id = %d;
        '''%random_num)
    return delete_test

def test_delete( delete_test:list,cursor,string:str):
    start = time.time()
    for i in delete_test:
        cursor.execute(i)
    end = time.time()
    print('%s delete_all:' % string, end - start)