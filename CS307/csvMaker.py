import io
import threading
import StringIteratorIO
from typing import Any, Dict, List, Optional, Tuple
import csv
import pandas as pd


def clean_csv_value(value: Optional[Any]) -> str:
    if value is None:
        return r'\N'
    return str(value).replace('\n', '\\n')


def make_contract_csv(path: str) -> Tuple[io.StringIO, io.StringIO, io.StringIO, io.StringIO,
                                          io.StringIO, io.StringIO, io.StringIO]:
    global csv_file
    file = pd.read_csv(path, sep=',', header=1)

    # Create a list of tuples containing the column names and the data
    # for each row.
    client_enterprise = io.StringIO()
    director = io.StringIO()
    salesman = io.StringIO()
    product = io.StringIO()
    product_model = io.StringIO()
    contract = io.StringIO()
    contract_content = io.StringIO()

    client_enterprise_serial = 1
    director_serial = 1
    salesman_serial = 1
    product_serial = 1
    product_model_serial = 1
    contract_serial = 1
    contract_content_serial = 1
    #serial = 1

    for index, row in file.iterrows():
        client_enterprise.write('|'.join(map(clean_csv_value, (
            client_enterprise_serial,
            row[1],  # client_enterprise_name
            row[2],  # supply center
            row[3],  # country
            row[4],  # city
            row[5],  # industry
        ))) + '\n')
        director.write('|'.join(map(clean_csv_value, (
            director_serial,
            row[14],  # director_name
        ))) + '\n')
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
        product.write('|'.join(map(clean_csv_value, (
            product_serial,
            row[6],  # product code
            row[7],  # product name
        ))) + '\n')
        product_model.write('|'.join(map(clean_csv_value, (
            product_model_serial,
            product_serial,  # product_model_id
            row[8],  # product_model_name
            row[9],  # unit price
        ))) + '\n')
        contract.write('|'.join(map(clean_csv_value, (
            contract_serial,
            row[0],  # contract_id
            client_enterprise_serial,  # client_enterprise_id
            row[11],  # contract_date
            #[12],  # estimated_delivery_date
            director_serial,  # director_id
        ))) + '\n')
        contract_content.write('|'.join(map(clean_csv_value, (
            contract_content_serial,
            contract_serial,  # contract_id
            product_model_serial,  # product_model_id
            row[10],  # quantity
            row[12],  # estimated_delivery_date
            row[13],#lodgement_date
            salesman_serial,  # salesman_id
        ))) + '\n')
        client_enterprise_serial += 1
        director_serial += 1
        salesman_serial += 1
        product_serial += 1
        product_model_serial += 1
        contract_serial += 1
        contract_content_serial += 1

    client_enterprise.seek(0)
    director.seek(0)
    salesman.seek(0)
    product.seek(0)
    product_model.seek(0)
    contract.seek(0)
    contract_content.seek(0)
    return client_enterprise, director, salesman, product, product_model, contract, contract_content
