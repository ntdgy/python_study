import random

director_name = ['ahpwnzl mabfhlu','augsiq qbtxmw','gyrpvldoewfuin tmsgrjahozqwun',
                 'grecfblmuqz jkebcmdwqao','ljuemdby gfdewsck','dsrhgtxzivcuoya rcxmdlofqkgvphs',]

client_enterprise_name = ['hjwpfxevdlmcqz jexytvcfnrglaq','wrvjudn paydvfc','xuanq hxzve',
                          'drhelmfupxnz ljscbumproni','ugodj zutjm','yjgwlnzpbk bhevflixys',
                          'fiovwl hnzray','lsyexrpwzicdfq ckndofjeuzgpbi']

def generate_select_test_supply_center() -> list:
    select_test = []
    for i1 in range(10):
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
    for i1 in range(10):
        select_test.append('''
        SELECT * FROM client_enterprise WHERE id = %d;
        ''' % random.randint(1, 275302))
    for i in client_enterprise_name:
        select_test.append('''
        SELECT * FROM client_enterprise WHERE name = '%s';
        ''' % i)
    return select_test

