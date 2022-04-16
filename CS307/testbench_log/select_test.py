import random
import time

director_name = ['ahpwnzl mabfhlu','augsiq qbtxmw','gyrpvldoewfuin tmsgrjahozqwun',
                 'grecfblmuqz jkebcmdwqao','ljuemdby gfdewsck','dsrhgtxzivcuoya rcxmdlofqkgvphs',]

client_enterprise_name = ['hjwpfxevdlmcqz jexytvcfnrglaq','wrvjudn paydvfc','xuanq hxzve',
                          'drhelmfupxnz ljscbumproni','ugodj zutjm','yjgwlnzpbk bhevflixys',
                          'fiovwl hnzray','lsyexrpwzicdfq ckndofjeuzgpbi']

salesman_name = ['gndxzrfyulie qvfykexcuopw','lykjcqwteznomhp vlfsegqxodabznt','napdbvwkfytxzho gtsxmdyehwjblvc',
                 'bhrfsxwvpnoz deuqazrgnkot','pybwg chxeg','podxevkisw wrosfeuzvc',
                 'wvpgnuym mqktwoib','swmdinbcohtarlk iylvfhorbucpjem','agtwu ykazf']

salesman_number = ['11049911','19647906','17444041',
                   '15938426','19707413','14263792',
                   '18402745','15744174','19246098']

salesman_phone = ['15794620485','13261138409','16613282797',
                  '14268410346','12808971977','15530011206',
                  '17120631428','12505751408','16568866838']

product_code = ['N9C7h0Jx','i5gCFe4k','zsVaSZrH',
                'uPUofy6q','yeKWEuzc','kpfj5GlW',
                '1f7TCp9K','FJnygAXG','qkjmafCR']

product_name = ['nuoaxkqgcvt cfhrtbemaix','mzftpibjwo nzsgeyloru','cftxq ivajf',
                'mzqhnsfbpoevjdk gefqcwlxvpionut','qyhlungdz rfuleqwnd','bfoau xajml',
                'mbyjo lownu','rlgoemuwfkdqjs evfxmalobyuhij','qndtxlmfjcgaupe ytiwvjzqamxopeg']

product_model = ['yhzqi yzhdt','sxvwgua iyjxnwf','vwlybetukzcqn cvyirmsnebqod',
                 'ijkvtenzscupxq lktjzofacgxwen','ryeohdupljb usfbaohzyvx','mdlycxjvkzrpqb cqeflukpznxtgy',
                 'uonhcjasbypvxwe uweajmrlihgotbx','czhsruvj hqxrgudl','xzkbjvrqgdlmco ifqtgmzhuewkjc']
#8081 selections in 7 tables

def generate_select_test_supply_center() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM supply_center WHERE id = %d;
        ''' % random.randint(1, 93632))
    for i in director_name:
        select_test.append('''
        SELECT * FROM supply_center WHERE director_name = '%s';
        ''' % i)
    return select_test

def generate_select_test_client_enterprise() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM client_enterprise WHERE id = %d;
        ''' % random.randint(1, 275302))
    for i in client_enterprise_name:
        select_test.append('''
        SELECT * FROM client_enterprise WHERE name = '%s';
        ''' % i)
    return select_test

def generate_select_test_salesman() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM salesman WHERE id = %d;
        ''' % random.randint(1, 972749))
    for i in salesman_name:
        select_test.append('''
        SELECT * FROM salesman WHERE name = '%s';
        ''' % i)
    for i in salesman_number:
        select_test.append('''
        SELECT * FROM salesman WHERE number = '%s';
        ''' % i)
    for i in salesman_phone:
        select_test.append('''
        SELECT * FROM salesman WHERE mobile_number = '%s';
        ''' % i)
    return select_test

def generate_select_test_product() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM product WHERE id = %d;
        ''' % random.randint(1, 962787))
    for i in product_code:
        select_test.append('''
        SELECT * FROM product WHERE product_code = '%s';
        ''' % i)
    for i in product_name:
        select_test.append('''
        SELECT * FROM product WHERE product_name = '%s';
        ''' % i)
    return select_test

def generate_select_test_product_model() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM product_model WHERE id = %d;
        ''' % random.randint(1, 3597940))
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM product_model WHERE product_id = %d;
        ''' % random.randint(1, 962787))
    for i in product_model:
        select_test.append('''
        SELECT * FROM product_model WHERE product_model = '%s';
        ''' % i)
    return select_test

def generate_select_test_contract() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM contract WHERE id = %d;
        ''' % random.randint(1, 400000))
    return select_test

def generate_select_test_contract_content() -> list:
    select_test = []
    for i1 in range(1000):
        select_test.append('''
        SELECT * FROM contract_content WHERE id = %d;
        ''' % random.randint(1, 3597940))
    return select_test

def test_select(select_supply_center:list, select_client_enterprise:list, select_salesman:list, select_product:list,
                     select_product_model:list, select_contract:list, select_contract_content:list,curcor,string:str):
    start1 = time.time()
    start = time.time()
    for i in select_supply_center:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select supply_center: %f\n' % (string, end - start))
    print('%s select_supply_center:'%string, end - start)
    start = time.time()
    for i in select_client_enterprise:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select client_enterprise: %f\n' % (string, end - start))
    print('%s select_client_enterprise:'%string, end - start)
    start = time.time()
    for i in select_salesman:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select salesman: %f\n' % (string, end - start))
    print('%s select_salesman:' %string, end - start)
    start = time.time()
    for i in select_product:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select product: %f\n' % (string, end - start))
    print('%s select_product:' %string, end - start)
    start = time.time()
    for i in select_product_model:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select product_model: %f\n' % (string, end - start))
    print('%s select_product_model:' %string, end - start)
    start = time.time()
    for i in select_contract:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select contract: %f\n' % (string, end - start))
    print('%s select_contract:' %string, end - start)
    start = time.time()
    for i in select_contract_content:
        curcor.execute(i)
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select contract_content: %f\n' % (string, end - start))
    print('%s select_contract_content:' %string, end - start)
    end1 = time.time()
    with open('log.txt', 'a') as f:
        f.write('%s select all: %f\n' % (string, end1 - start1))
    print('%s select_all:' %string, end1 - start1)




