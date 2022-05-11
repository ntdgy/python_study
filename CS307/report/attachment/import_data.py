import psycopg2.extras
import time
import csvMaker



connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="task4_test",
    user="dgy",
    password='',
)
connection.autocommit = True
cursor = connection.cursor()


def pre_process(file_name):
    start_time = time.time()
    supply_center,client_enterprise,  salesman, \
        product, product_model, contract, contract_content=\
        csvMaker.make_contract_csv(file_name)
    print("pre_process time is %s seconds ---" % (time.time() - start_time))
    time1 = time.time()
    start_time = time.time()
    cursor.execute("""alter table supply_center disable trigger ALL;""")
    cursor.copy_from(supply_center, 'supply_center', sep='|')
    print("director time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table client_enterprise disable trigger ALL;""")
    cursor.copy_from(client_enterprise, 'client_enterprise', sep='|')
    print("client_enterprise time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table salesman disable trigger ALL;""")
    cursor.copy_from(salesman, 'salesman', sep='|')
    print("salesman time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table product disable trigger ALL;""")
    cursor.copy_from(product, 'product', sep='|')
    print("product time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table product_model disable trigger ALL;""")
    cursor.copy_from(product_model, 'product_model', sep='|')
    print("product_model time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table contract disable trigger ALL;""")
    cursor.copy_from(contract, 'contract', sep='|')
    print("contract time is %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    cursor.execute("""alter table contract_content disable trigger ALL;""")
    cursor.copy_from(contract_content, 'contract_content', sep='|')
    print("contract_content time is %s seconds ---" % (time.time() - start_time))
    print("total import time is %s seconds ---" % (time.time() - time1))




def copy_from_test(file_name, table_name):
    with open(file_name, 'r') as f:
        f.readline()
        cursor.copy_from(f, table_name, sep=',')
    connection.commit()

start = time.time()
pre_process('data.csv')
#pre_process('contract_info.csv')

end = time.time()
print('total time:'+str(end - start))
