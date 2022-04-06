import psycopg2
import csv
import psycopg2.extras
import String
import time
import pandas as pd
import csvMaker
import csvtest



# connection = psycopg2.connect(
#     host="42.194.178.20",
#     port="5432",
#     database="project1",
#     user="checker",
#     password='xtny38206',
# )
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="project1",
    user="dgy",
    password='xtny38206',
)
connection.autocommit = True
cursor = connection.cursor()


def pre_process(file_name):
    start_time = time.time()
    client_enterprise, director, salesman, \
        product, product_model, contract, contract_content=\
        csvtest.make_contract_csv(file_name)
    print("pre_process time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(client_enterprise, 'client_enterprise', sep='|')
    print("client_enterprise time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(director, 'director', sep='|')
    print("director time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(salesman, 'salesman', sep='|')
    print("salesman time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(product, 'product', sep='|')
    print("product time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(product_model, 'product_model', sep='|')
    print("product_model time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(contract, 'contract', sep='|')
    print("contract time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.copy_from(contract_content, 'contract_content', sep='|')
    print("contract_content time is %s seconds ---" % (time.time() - start_time))
    #print(client_enterprise)
    # copy_from_test(client_enterprise, 'client_enterprise')
    # copy_from_test(director, 'director')
    #copy_from_test(salesman, 'salesman')
    #copy_from_test(product, 'product')
    # copy_from_test(product_model, 'product_model')
    # copy_from_test(contract, 'contract')
    # copy_from_test(contract_content, 'contract_content')



def copy_from_test(file_name, table_name):
    with open(file_name, 'r') as f:
        f.readline()
        cursor.copy_from(f, table_name, sep=',')
    connection.commit()

start = time.time()
pre_process('contract_info.csv')
#copy_from_test('contract_info.csv','testdata')
end = time.time()
print('total time:'+str(end - start))
