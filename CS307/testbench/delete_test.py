import random
import time

def generate_delete_test()->list:
    delete_test = []
    for i in range(0, 10):
        delete_test.append('''
        delete from contract_content where id = %d;
        '''%(random.randint(1, 100000)))
    return delete_test

def test_delete( delete_test:list,cursor,string:str):
    start = time.time()
    for i in delete_test:
        cursor.execute(i)
    end = time.time()
    print('%s delete_all:' % string, end - start)