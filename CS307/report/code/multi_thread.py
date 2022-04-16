import io
import threading
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def clean_csv_value(value: Optional[Any]) -> str:
    if value is None:
        return r'\N'
    return str(value).replace('\n', '\\n')

def make_client_enterprise(file):
    client_enterprise = io.StringIO()
    client_enterprise_set = set()
    client_enterprise_dict = {}
    client_enterprise_serial = 1
    for index, row in file.iterrows():
        if row[1] not in client_enterprise_set:
            client_enterprise.write('|'.join(map(clean_csv_value, (
                client_enterprise_serial,
                row[1],  # client_enterprise_name
                row[2],  # supply center
                row[3],  # country
                row[4],  # city
                row[5],  # industry
            ))) + '\n')
            client_enterprise_dict[row[1]] = client_enterprise_serial
            client_enterprise_set.add(row[1])
            client_enterprise_serial += 1

    return client_enterprise, client_enterprise_dict

def make_derector(file):
    director = io.StringIO()
    director_serial = 1
    director_set = set()
    director_dict = {}
    for index, row in file.iterrows():
        if row[14] not in director_set:
            director.write('|'.join(map(clean_csv_value, (
                director_serial,
                row[14],  # director_name
            ))) + '\n')
            director_dict[row[14]] = director_serial
            director_set.add(row[14])
            director_serial += 1
    return director, director_dict

def make_salesman(file):
    salesman = io.StringIO()
    salesman_serial = 1
    salesman_set = set()
    salesman_dict = {}
    for index, row in file.iterrows():
        if row[15] not in salesman_set:
            gender = '0'
            if row[17] == 'Female':
                gender = '1'
            salesman.write('|'.join(map(clean_csv_value, (
                salesman_serial,
                row[15],  # salesman_name
                row[16],  # salesman number
                gender,
                row[18],  # age
                row[19],  # mobile phone
            ))) + '\n')
            salesman_set.add(row[15])
            salesman_dict[row[15]] = salesman_serial
            salesman_serial +=1
    return salesman, salesman_dict

def make_product(file):
    product = io.StringIO()
    product_serial = 1
    product_set = set()
    product_dict = {}
    for index, row in file.iterrows():
        if row[6] not in product_set:
            product.write('|'.join(map(clean_csv_value, (
                product_serial,
                row[6],  # product code
                row[7],  # product name
            ))) + '\n')
            product_set.add(row[6])
            product_dict[row[6]] = product_serial
            product_serial += 1
    return product, product_dict

def make_product_model(file,product_dict):
    product_model = io.StringIO()
    product_model_serial = 1
    product_model_set = set()
    product_model_dict = {}
    for index, row in file.iterrows():
        product_model.write('|'.join(map(clean_csv_value, (
            product_model_serial,
            product_dict[row[6]],  # product_model_id
            row[8],  # product_model_name
            row[9],  # unit price
        ))) + '\n')
        product_model_set.add(row[8])
        product_model_dict[row[8]] = product_model_serial
        product_model_serial += 1
    return product_model, product_model_dict

def make_contract(file, client_enterprise_dict, director_dict):
    contract = io.StringIO()
    contract_serial = 1
    contract_dict = {}
    contract_set = set()
    for index, row in file.iterrows():
        if row[0] not in contract_set:
            contract.write('|'.join(map(clean_csv_value, (
                contract_serial,
                row[0],  # contract_id
                # client_enterprise_serial,  # client_enterprise_id
                client_enterprise_dict[row[1]],  # client_enterprise_id
                row[11],  # contract_date
                # [12],  # estimated_delivery_date
                # director_serial,  # director_id
                director_dict[row[14]],  # director_id
            ))) + '\n')
            contract_set.add(row[0])
            contract_dict[row[0]] = contract_serial
            contract_serial += 1
    return contract, contract_dict


def make_contract_csv(path: str) -> Tuple[io.StringIO, io.StringIO, io.StringIO, io.StringIO,
                                          io.StringIO, io.StringIO, io.StringIO]:
    global csv_file
    file = pd.read_csv(path, sep=',', header=1)
    file.fillna(value='\\N', inplace=True)

    # Create a list of tuples containing the column names and the data
    # for each row.

    contract_content = io.StringIO()
    contract_content_serial = 1
    #serial = 1
    contract_content_set = set()
    m1 = MyThread(make_client_enterprise, args=(file,))
    m2 = MyThread(make_derector, args=(file,))
    m3 = MyThread(make_salesman, args=(file,))
    m4 = MyThread(make_product, args=(file,))
    m1.start()
    m2.start()
    m3.start()
    m4.start()
    m1.join()
    m2.join()
    m3.join()
    m4.join()
    client_enterprise, client_enterprise_dict = m1.get_result()
    director, director_dict = m2.get_result()
    salesman, salesman_dict = m3.get_result()
    product, product_dict = m4.get_result()
    m5 = MyThread(make_product_model, args=(file,product_dict))
    m6 = MyThread(make_contract, args=(file, client_enterprise_dict, director_dict))
    m5.start()
    m6.start()
    m5.join()
    m6.join()
    product_model, product_model_dict = m5.get_result()
    contract, contract_dict = m6.get_result()
    for index, row in file.iterrows():
        contract_content.write('|'.join(map(clean_csv_value, (
            contract_content_serial,
            #contract_serial,  # contract_id
            contract_dict[row[0]],  # contract_id
            #product_model_serial,  # product_model_id
            product_model_dict[row[8]],  # product_model_id
            row[10],  # quantity
            row[12],  # estimated_delivery_date
            row[13],#lodgement_date
            #salesman_serial,  # salesman_id
            salesman_dict[row[15]],  # salesman_id
        ))) + '\n')
        contract_content_serial += 1

    client_enterprise.seek(0)
    director.seek(0)
    salesman.seek(0)
    product.seek(0)
    product_model.seek(0)
    contract.seek(0)
    contract_content.seek(0)
    return client_enterprise, director, salesman, product, product_model, contract, contract_content
