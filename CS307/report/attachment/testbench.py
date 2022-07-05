import psycopg2.extras
import sqlite3
import time
import fileDB.Client as fileDB
import import_data_test as imp
import select_test as sel
import update_test as upd
import delete_test as delt


def create_connection():
    filedb = fileDB.DBMSClient('anshang', '123456')
    pgsql = psycopg2.connect(
        host="localhost",
        port="5432",
        database="task4_test",
        user="dgy",
        password='',
    )
    pgsql.autocommit = True
    sqlite = sqlite3.connect('sqlite.db')
    return filedb, pgsql, sqlite


if __name__ == '__main__':
    filedb, pgsql, sqlite = create_connection()
    select_supply_center = sel.generate_select_test_supply_center()
    select_client_enterprise = sel.generate_select_test_client_enterprise()
    select_test_salesman = sel.generate_select_test_salesman()
    select_test_product = sel.generate_select_test_product()
    select_test_product_model = sel.generate_select_test_product_model()
    select_test_contract = sel.generate_select_test_contract()
    select_test_contract_content = sel.generate_select_test_contract_content()
    update_test_supply_cente = upd.generate_update_test_supply_center()
    update_test_client_enterprise = upd.generate_update_test_client_enterprise()
    update_test_salesman = upd.generate_update_test_salesman()
    update_test_product = upd.generate_update_test_product()
    update_test_product_model = upd.generate_update_test_product_model()
    update_test_contract = upd.generate_update_test_contract()
    update_test_contract_content = upd.generate_update_test_contract_content()
    delete_test = delt.generate_delete_test()

    pgsql = pgsql.cursor()

    file_db_start = time.time()
    print('Start testing...')
    print("Start testing fileDB...")
    print("Testing insert...")
    imp.test_file_insert(filedb)
    print("Testing select...")
    sel.test_select(select_supply_center, select_client_enterprise, select_test_salesman, select_test_product,
                    select_test_product_model, select_test_contract, select_test_contract_content, filedb, 'fileDB')
    print("Testing update...")
    upd.test_update(update_test_supply_cente, update_test_client_enterprise, update_test_salesman, update_test_product,
                    update_test_product_model, update_test_contract, update_test_contract_content, filedb, 'fileDB')
    print("Testing delete...")
    delt.test_delete(delete_test, filedb, 'fileDB')
    file_db_end = time.time()
    print("Testing fileDB finished.")

    print("Start testing pgsql...")
    pgsql_start = time.time()
    print("Testing insert...")
    imp.test_pgsql_insert(pgsql)
    print("Testing select...")
    sel.test_select(select_supply_center, select_client_enterprise, select_test_salesman, select_test_product,
                    select_test_product_model, select_test_contract, select_test_contract_content, pgsql, 'pgsql')
    print("Testing update...")
    upd.test_update(update_test_supply_cente, update_test_client_enterprise, update_test_salesman, update_test_product,
                    update_test_product_model, update_test_contract, update_test_contract_content, pgsql, 'pgsql')
    print("Testing delete...")
    delt.test_delete(delete_test, pgsql, 'pgsql')
    pgsql_end = time.time()
    print("Testing pgsql finished.")

    print("Start testing sqlite...")
    sqlite_start = time.time()
    print("Testing insert...")
    imp.test_sqlite_insert(sqlite)
    print("Testing select...")
    sel.test_select(select_supply_center, select_client_enterprise, select_test_salesman, select_test_product,
                    select_test_product_model, select_test_contract, select_test_contract_content, sqlite, 'sqlite')
    print("Testing update...")
    upd.test_update(update_test_supply_cente, update_test_client_enterprise, update_test_salesman, update_test_product,
                    update_test_product_model, update_test_contract, update_test_contract_content, sqlite, 'sqlite')
    print("Testing delete...")
    delt.test_delete(delete_test, sqlite, 'sqlite')
    sqlite_end = time.time()
    print("Testing sqlite finished.")

    print('Finished!')
