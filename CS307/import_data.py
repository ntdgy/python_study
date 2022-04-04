import psycopg2
import csv
import psycopg2.extras
import String
import time
import pandas as pd
import csvMaker



connection = psycopg2.connect(
    host="42.194.178.20",
    port="5432",
    database="project1",
    user="checker",
    password='xtny38206',
)
connection.autocommit = True
cursor = connection.cursor()


def pre_process(file_name):
    client_enterprise, director, salesman, \
        product, product_model, contract, contract_content=\
        csvMaker.make_contract_csv(file_name)
    #cursor.copy_from(client_enterprise, 'client_enterprise', sep='|')
    #cursor.copy_from(director, 'director', sep='|')
    cursor.copy_from(salesman, 'salesman', sep='|')
    #cursor.copy_from(product, 'product', sep='|')
    #cursor.copy_from(product_model, 'product_model', sep='|')
    #cursor.copy_from(contract, 'contract', sep='|')
    #cursor.copy_from(contract_content, 'contract_content', sep='|')
    #print(client_enterprise)
    # copy_from_test(client_enterprise, 'client_enterprise')
    # copy_from_test(director, 'director')
    #copy_from_test(salesman, 'salesman')
    #copy_from_test(product, 'product')
    # copy_from_test(product_model, 'product_model')
    # copy_from_test(contract, 'contract')
    # copy_from_test(contract_content, 'contract_content')



def copy_from_test(file_name, table_name):

    cursor.copy_from(file_name, table_name, sep='|')
    connection.commit()

start = time.time()
pre_process('tt.csv')
end = time.time()
print(end - start)
