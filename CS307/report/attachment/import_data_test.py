import time
import pgsql_reader
import innitial
import filedb_reader


def test_file_insert(a):

    start1 = time.time()
    start = time.time()
    supply_center = filedb_reader.read_supply_center()
    for i in supply_center:
        a.excuse(i)
    end = time.time()
    print("File DB Supply Center: ", end - start)
    start = time.time()
    client_enterprise = filedb_reader.read_client_enterprise()
    for i in client_enterprise:
        a.excuse(i)
    end = time.time()
    print("File DB Client Enterprise: ", end - start)
    start = time.time()
    salesman = filedb_reader.read_salesman()
    for i in salesman:
        a.excuse(i)
    end = time.time()
    print("File DB Salesman: ", end - start)
    start = time.time()
    product = filedb_reader.read_product()
    for i in product:
        a.excuse(i)
    end = time.time()
    print("File DB Product: ", end - start)
    start = time.time()
    product_model = filedb_reader.read_product_model()
    for i in product_model:
        a.excuse(i)
    end = time.time()
    print("File DB Product Model: ", end - start)
    start = time.time()
    contract = filedb_reader.read_contract()
    for i in contract:
        a.excuse(i)
    end = time.time()
    print("File DB Contract: ", end - start)
    start = time.time()
    contract_content = filedb_reader.read_contract_content()
    for i in contract_content:
        a.excuse(i)
    end = time.time()
    print("File DB Contract Content: ", end - start)
    end1 = time.time()
    print("File DB: ", end1 - start1)

def test_pgsql_insert(cursor):

    cursor.execute(innitial.pgsql)

    start1 = time.time()
    start = time.time()
    supply_center = pgsql_reader.read_supply_center()
    for i in supply_center:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Supply Center: ", end - start)

    start = time.time()
    client_enterprise = pgsql_reader.read_client_enterprise()
    for i in client_enterprise:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Client Enterprise: ", end - start)

    start = time.time()
    salesman = pgsql_reader.read_salesman()
    for i in salesman:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Salesman: ", end - start)

    start = time.time()
    product = pgsql_reader.read_product()
    for i in product:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Product: ", end - start)

    start = time.time()
    product_model = pgsql_reader.read_product_model()
    for i in product_model:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Product Model: ", end - start)

    start = time.time()
    contract = pgsql_reader.read_contract()
    for i in contract:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Contract: ", end - start)

    start = time.time()
    contract_content = pgsql_reader.read_contract_content()
    for i in contract_content:
        cursor.execute(i)
    end = time.time()
    print("PGSQL Contract Content: ", end - start)
    end1 = time.time()
    print("PGSQL: ", end1 - start1)

def test_mysql_insert(cursor):
    cursor.execute(innitial.mysql)

    start1 = time.time()
    start = time.time()
    supply_center = pgsql_reader.read_supply_center()
    for i in supply_center:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Supply Center: ", end - start)

    start = time.time()
    client_enterprise = pgsql_reader.read_client_enterprise()
    for i in client_enterprise:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Client Enterprise: ", end - start)

    start = time.time()
    salesman = pgsql_reader.read_salesman()
    for i in salesman:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Salesman: ", end - start)

    start = time.time()
    product = pgsql_reader.read_product()
    for i in product:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Product: ", end - start)

    start = time.time()
    product_model = pgsql_reader.read_product_model()
    for i in product_model:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Product Model: ", end - start)

    start = time.time()
    contract = pgsql_reader.read_contract()
    for i in contract:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Contract: ", end - start)

    start = time.time()
    contract_content = pgsql_reader.read_contract_content()
    for i in contract_content:
        cursor.execute(i)
    end = time.time()
    print("MYSQL Contract Content: ", end - start)
    end1 = time.time()
    print("MYSQL: ", end1 - start1)

def test_sqlite_insert(connection):

    start1 = time.time()
    start = time.time()
    supply_center = pgsql_reader.read_supply_center()
    for i in supply_center:
        connection.execute(i)
    end = time.time()
    print("SQLITE Supply Center: ", end - start)

    start = time.time()
    client_enterprise = pgsql_reader.read_client_enterprise()
    for i in client_enterprise:
        connection.execute(i)
    end = time.time()
    print("SQLITE Client Enterprise: ", end - start)

    start = time.time()
    salesman = pgsql_reader.read_salesman()
    for i in salesman:
        connection.execute(i)
    end = time.time()
    print("SQLITE Salesman: ", end - start)

    start = time.time()
    product = pgsql_reader.read_product()
    for i in product:
        connection.execute(i)
    end = time.time()
    print("SQLITE Product: ", end - start)

    start = time.time()
    product_model = pgsql_reader.read_product_model()
    for i in product_model:
        connection.execute(i)
    end = time.time()
    print("SQLITE Product Model: ", end - start)

    start = time.time()
    contract = pgsql_reader.read_contract()
    for i in contract:
        connection.execute(i)
    end = time.time()
    print("SQLITE Contract: ", end - start)

    start = time.time()
    contract_content = pgsql_reader.read_contract_content()
    for i in contract_content:
        connection.execute(i)
    end = time.time()
    print("SQLITE Contract Content: ", end - start)
    end1 = time.time()
    print("SQLITE: ", end1 - start1)








