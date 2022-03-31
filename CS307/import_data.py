import psycopg2
import psycopg2.extras
import String
import time


connection = psycopg2.connect(
    host="42.194.178.20",
    port="5432",
    database="project1_1",
    user="checker",
    password='xtny38206',
)
connection.autocommit = True
cursor = connection.cursor()

def copy_from_test(file_name, table_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        #for row in f:
         #   print(row)
        cursor.copy_from(f, table_name, sep=',')
    connection.commit()

start = time.time()
copy_from_test('contract_info.csv', 'testdata')
end = time.time()
print(end - start)
