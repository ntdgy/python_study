import psycopg2.extras
import time
import pgsql_reader
import innitial

connection = psycopg2.connect(
    host="42.194.178.20",
    port="5432",
    database="project1",
    user="checker",
    password='xtny38206',
)
connection.autocommit = True
cursor = connection.cursor()


cursor.execute(innitial.sql)
time.sleep(1)
start = time.time()
supply_center = pgsql_reader.read_supply_center()
for i in supply_center:
    cursor.execute(i)
end = time.time()
print("Supply Center: ", end - start)

start = time.time()
client_enterprise = pgsql_reader.read_client_enterprise()
for i in client_enterprise:
    cursor.execute(i)
end = time.time()
print("Client Enterprise: ", end - start)

start = time.time()
salesman = pgsql_reader.read_salesman()
for i in salesman:
    cursor.execute(i)
end = time.time()
print("Salesman: ", end - start)

start = time.time()
product = pgsql_reader.read_product()
for i in product:
    cursor.execute(i)
end = time.time()
print("Product: ", end - start)

start = time.time()
product_model = pgsql_reader.read_product_model()
for i in product_model:
    cursor.execute(i)
end = time.time()
print("Product Model: ", end - start)

start = time.time()
contract = pgsql_reader.read_contract()
for i in contract:
    cursor.execute(i)
end = time.time()
print("Contract: ", end - start)

start = time.time()
contract_content = pgsql_reader.read_contract_content()
for i in contract_content:
    cursor.execute(i)
end = time.time()
print("Contract Content: ", end - start)





