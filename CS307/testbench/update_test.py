import random
import time

def getname() -> str:
    i1 = random.randint(5, 15)
    name = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
        'e', 'd', 'c', 'b', 'a'], i1))
    name = name + ' '
    name = name + ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
        'e', 'd', 'c', 'b', 'a'], i1))
    return name


def generate_update_test_supply_center() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update supply_center set director_name = %s where id = %d;''' % (name, random.randint(1, 93632)))
    return update_test

def generate_update_test_client_enterprise() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update client_enterprise set name = %s where id = %d;''' % (name, random.randint(1, 275302)))
    return update_test

def generate_update_test_salesman() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update salesman set name = %s where id = %d;''' % (name, random.randint(1, 972749)))
    return update_test

def generate_update_test_product() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update product set name = %s where id = %d;''' % (name, random.randint(1, 962787)))
    return update_test

def generate_update_test_product_model() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update product_model set name = %s where id = %d;''' % (name, random.randint(1, 3597940)))
    return update_test

def generate_update_test_contract() -> list:
    update_test = []
    for i in range(0, 10):
        name = getname()
        update_test.append(
            '''
            update contract set name = %s where id = %d;''' % (name, random.randint(1, 400000)))
    return update_test

def generate_update_test_contract_content() -> list:
    select_test = []
    for i in range(0, 10):
        select_test.append(
            '''
            select * from contract_content where id = %d;''' % random.randint(1, 3597940))
    return select_test

def test_update(update_supply_center: list, update_client_enterprise: list, update_salesman: list,
                update_product: list, update_product_model: list, update_contract: list,
                update_contract_content: list,curcor,string:str) -> None:
    start1 = time.time()
    start = time.time()
    for i in update_supply_center:
        curcor.execute(i)
    end = time.time()
    print('%s update_supply_center:' % string, end - start)
    start = time.time()
    for i in update_client_enterprise:
        curcor.execute(i)
    end = time.time()
    print('%s update_client_enterprise:' % string, end - start)
    start = time.time()
    for i in update_salesman:
        curcor.execute(i)
    end = time.time()
    print('%s update_salesman:' % string, end - start)
    start = time.time()
    for i in update_product:
        curcor.execute(i)
    end = time.time()
    print('%s update_product:' % string, end - start)
    start = time.time()
    for i in update_product_model:
        curcor.execute(i)
    end = time.time()
    print('%s update_product_model:' % string, end - start)
    start = time.time()
    for i in update_contract:
        curcor.execute(i)
    end = time.time()
    print('%s update_contract:' % string, end - start)
    start = time.time()
    for i in update_contract_content:
        curcor.execute(i)
    end = time.time()
    print('%s update_contract_content:' % string, end - start)
    end1 = time.time()
    print('%s update_all:' % string, end1 - start1)

