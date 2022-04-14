import random

def generate_delete_test()->list:
    delete_test = []
    for i in range(0, 10):
        delete_test.append('''
        delete from contract_content where id = %d;
        '''%(random.randint(1, 100000)))
    return delete_test