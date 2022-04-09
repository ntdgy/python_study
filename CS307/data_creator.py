import pandas as pd
import numpy as np
import random
import string
import time

supply_center_country = {
    'Eastern China': ['China'],
    'Europe': ['France', 'Germany', 'Italy', 'Spain', 'Sweden', 'United Kingdom', 'Netherlands'],
    'America': ['Canada', 'Mexico', 'United States'],
    'Southern China': ['China'],
    'Asia': ['India', 'Japan', 'Korea', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam'],
    'Africa': ['Algeria', 'Egypt', 'Morocco', 'South Africa', 'Tunisia'],
    'Southwestern China': ['China'],
    'Australia': ['Australia'],
    'Antarctica': ['Antarctica'],
}

china_cities = ['Shanghai', 'Shenzhen', 'Beijing', 'Guangzhou', 'Chengdu', 'Wuhan', 'Hangzhou', 'Nanjing', 'Xi\'an',
                'Chongqing', 'Kunming',
                'Nanjing', 'Changsha', 'Wuxi', 'Hai\'an', 'Changchun', 'Dalian', 'Qingdao', 'Fuzhou', 'Jinan',
                'Zhengzhou', 'Ningbo', 'Wuhan',
                'Nantong', 'Nanchang']

supply_center_lists = ['Eastern China', 'Europe', 'America', 'Southern China', 'Asia', 'Africa', 'Southwestern China',
                       'Australia', 'Antarctica']

industry = ['Agriculture', 'Automotive', 'Banking', 'Chemicals', 'Construction', 'Consumer Goods',
            'Education', 'Electronics', 'Energy', 'Entertainment', 'Financial Services', 'Food & Beverage',
            'Government', 'Healthcare', 'Hospitality', 'Insurance', 'Machinery', 'Media', 'Metals', 'Oil & Gas',
            'Pharmaceuticals', 'Real Estate', 'Retail', 'Technology', 'Telecommunications', 'Transportation',
            'Utilities', 'Other', 'Internet', 'Bank']

gender = ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'Cisgender', 'Cis Female', 'Cis Male', 'Cis Man', 'Cis Woman', 'Cisgender Female',
          'Cisgender Male', 'Cisgender Man', 'Cisgender Woman', 'Female to Male', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning',
          'Gender Variant', 'Genderqueer', 'Intersex', 'Male to Female', 'MTF', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Trans',
          'Trans*', 'Trans Female', 'Trans* Female', 'Trans Male', 'Trans* Male', 'Trans Man', 'Trans* Man', 'Trans Person', 'Trans* Person', 'Trans Woman',
          'Trans* Woman', 'Transfeminine', 'Transgender', 'Transgender Female', 'Transgender Male', 'Transgender Man', 'Transgender Person', 'Transgender Woman',
          'Transmasculine', 'Transsexual', 'Transsexual Female', 'Transsexual Male', 'Transsexual Man', 'Transsexual Person', 'Transsexual Woman', 'Two-Spirit']


# industry,product code,product name,product model,unit price,quantity,contract date,estimated delivery date,lodgement date,director,salesman,salesman number,gender,age,mobile phone,

start1=(2005,1,1,0,0,0,0,0,0)
end1=(2022,3,31,23,59,59,0,0,0)

def create_product(num: int):
    product_file = []
    product_code_set = set()
    for i0 in range(num):
        product = {
            'product_code': '',
            'product_name': ''
        }
        while True:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            if ran_str not in product_code_set:
                product_code_set.add(ran_str)
                product['product_code'] = ran_str
                break
        for i1 in range(random.randint(1, 10)):
            i1 = random.randint(5, 15)
            name = ''.join(random.sample(
                ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                 'f',
                 'e', 'd', 'c', 'b', 'a'], i1))
            name = name + ' '
            name = name + ''.join(random.sample(
                ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                 'f',
                 'e', 'd', 'c', 'b', 'a'], i1))
            product['product_name'] = name
        product_file.append(product)
    return product_file


def create_product_model(num: int, product_file: list):
    product_model_file = []
    for i0 in range(num):
        product_model = {
            'product_model': '',
            'product_code': '',
            'unit_price': '',
            'product_name': ''
        }
        product = random.choice(product_file)
        product_model['product_code'] = product['product_code']
        product_model['product_name'] = product['product_name']
        product_model['unit_price'] = str(random.randint(1, 10000))
        i1 = random.randint(5, 15)
        name = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        name = name + ' '
        name = name + ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        product_model['product_model'] = name
        product_model_file.append(product_model)
    return product_model_file


def create_supply_center(num: int):
    supply_center = []
    for i0 in range(num):
        supply_center_json = {
            'supply_center': '',
            'director': ''
        }
        supply_center_json['supply_center'] = random.choice(supply_center_lists)
        i1 = random.randint(5, 15)
        name = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        name = name + ' '
        name = name + ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        supply_center_json['director'] = name
        supply_center.append(supply_center_json)
    return supply_center


def create_client_enterprise(num: int, supply_center_list: list):
    client_enterprise = []
    for i0 in range(num):
        client_enterprise_json = {
            'client enterprise': '',
            'country': '',
            'city': '',
            'industry': '',
            'supply center': '',
            'director': ''
        }
        i1 = random.randint(5, 15)
        name = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        name = name + ' '
        name = name + ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        client_enterprise_json['client enterprise'] = name
        supply_center = random.choice(supply_center_list)
        client_enterprise_json['director'] = supply_center['director']
        supply_center = supply_center['supply_center']
        client_enterprise_json['country'] = random.choice(supply_center_country[supply_center])
        if client_enterprise_json['country'] == 'China':
            client_enterprise_json['city'] = random.choice(china_cities)
        else:
            client_enterprise_json['city'] = 'NULL'
        client_enterprise_json['industry'] = random.choice(industry)
        client_enterprise_json['supply center'] = supply_center
        client_enterprise.append(client_enterprise_json)
    return client_enterprise


def create_salesman(num: int):
    salesman = []
    phone_set = set()
    number_set = set()
    # number = list(range(11000000, 19999999))
    # random.shuffle(number)
    # phone_number = list(range(12000000000, 17899999999))
    # random.shuffle(phone_number)
    for i0 in range(num):
        while True:
            num = random.randint(11000000, 19999999)
            if num not in number_set:
                number_set.add(num)
                break
        while True:
            phone = random.randint(12000000000, 17899999999)
            if phone not in phone_set:
                phone_set.add(phone)
                break

        salesman_json = {
            'name': '',
            'number': num,
            'phone': phone,
            'age': random.randint(18, 60),
            'gender': random.choice(gender)
        }
        i1 = random.randint(5, 15)
        name = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        name = name + ' '
        name = name + ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], i1))
        salesman_json['name'] = name
        salesman.append(salesman_json)
    return salesman

def create_contract(num: int, client_enterprise_list: list):
    contract = []
    for i0 in range(num):
        contract_json = {
            'contract': '',
            'client enterprise': '',
            'country': '',
            'city': '',
            'industry': '',
            'supply center': '',
            'contract_date': '',
            'director': '',
        }
        temp = random.choice(client_enterprise_list)
        contract_json['client enterprise'] = temp['client enterprise']
        contract_json['country'] = temp['country']
        contract_json['city'] = temp['city']
        contract_json['industry'] = temp['industry']
        contract_json['supply_center'] = temp['supply center']
        contract_json['director'] = temp['director']
        contract_json['contract'] = 'CSE' + str.zfill(str(i0), 7)
        contract_json['contract_date'] = create_date()
        contract.append(contract_json)
    return contract

def create_contract_content(contract_list: list,
                            product_model_list: list,sale_list: list):
    csv = {
        'contract number': [],
        'client enterprise': [],
        'supply center': [],
        'country': [],
        'city': [],
        'industry': [],
        'product code': [],
        'product name': [],
        'product model': [],
        'unit price': [],
        'quantity': [],
        'contract date': [],
        'estimated delivery date': [],
        'lodgement date': [],
        'director': [],
        'salesman': [],
        'salesman number': [],
        'gender':[],
        'age': [],
        'mobile phone': [],
    }
    for i0 in range(len(contract_list)):
        for i1 in range(random.randint(3, 15)):
            contract_content_json = contract_list[i0]
            product_model_json = random.choice(product_model_list)
            sale_json = random.choice(sale_list)
            csv['contract number'].append(contract_content_json['contract'])
            csv['client enterprise'].append(contract_content_json['client enterprise'])
            csv['supply center'].append(contract_content_json['supply center'])
            csv['country'].append(contract_content_json['country'])
            csv['city'].append(contract_content_json['city'])
            csv['industry'].append(contract_content_json['industry'])
            csv['contract date'].append(contract_content_json['contract_date'])
            csv['director'].append(contract_content_json['director'])
            csv['estimated delivery date'].append(create_date())
            csv['lodgement date'].append(create_lodgement_date())
            csv['product code'].append(product_model_json['product_code'])
            csv['product name'].append(product_model_json['product_name'])
            csv['product model'].append(product_model_json['product_model'])
            csv['unit price'].append(product_model_json['unit_price'])
            csv['quantity'].append(random.randint(100, 10000))
            csv['salesman number'].append(sale_json['number'])
            csv['salesman'].append(sale_json['name'])
            csv['gender'].append(sale_json['gender'])
            csv['age'].append(sale_json['age'])
            csv['mobile phone'].append(sale_json['phone'])
    return csv



def creat_phone():
    # 第二位
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位的值根据第二位来确定
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9)
    }[second]
    # 后8位随机抽取
    suffix = ''
    for x in range(8):
        suffix = suffix + str(random.randint(0, 9))
    # 拼接
    return "1{}{}{}".format(second, third, suffix)

def create_date():
    start_time = time.mktime(start1)
    end_time = time.mktime(end1)
    t = random.randint(start_time, end_time)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return date

def create_lodgement_date():
    if random.randint(0, 10) == 0:
        return ''
    start_time = time.mktime(start1)
    end_time = time.mktime(end1)
    t = random.randint(start_time, end_time)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return date

supply_center = create_supply_center(10)
client_enterprice = create_client_enterprise(5, supply_center)
contract_list = create_contract(4, client_enterprice)
product_file = create_product(10)
product_model_list = create_product_model(20,product_file)
sale_list = create_salesman(10)
csv = create_contract_content(contract_list, product_model_list, sale_list)
data_df = pd.DataFrame(csv)
data_df.to_csv('data.csv', index=False)
