import pandas as pd


def readfile(filename):
    """
    Reads a csv file and returns a pandas dataframe.
    """
    file = pd.read_csv(filename,sep='|',header=None)
    file.fillna(value='\\N', inplace=True)
    return file

def read_client_enterprise() -> list:
    """
    Reads the client_enterprise.csv file and returns a list of tuples.
    Each tuple contains the client_id and the enterprise_id.
    """
    sql = []
    client_enterprise = readfile('client_enterprise.csv')
    for index, row in client_enterprise.iterrows():
        sql.append('''insert into client_enterprise(id,name,supply_center_id,country,city,industry) 
                        values (
                        %s, 
                        %s, %s,%s,%s,%s);''')
    return sql

def read_contract() -> list:
    sql = []
    order = '''insert into contract(id,number,client_enterprise_id,contract_date) 
                    values ({},'{}',{},'{}');'''
    contract = readfile('contract.csv')
    for index, row in contract.iterrows():
        sql.append(order.format(row[0], row[1], row[2], row[3]))
    return sql

def read_contract_content() -> list:
    sql = []
    order = '''insert into contract_content(id,contract_id,product_model_id,quantity,estimated_delivery_date,lodgement_date,salesman_id) 
                    values ({},{},{},{},'{}','{}',{});'''
    contract_content = readfile('contract_content.csv')
    for index, row in contract_content.iterrows():
        sql.append(order.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return sql

def read_product() -> list:
    sql = []
    order = '''insert into product(id,product_code,product_name) 
                    values ({}，'{}'，'{}');'''
    product = readfile('product.csv')
    for index, row in product.iterrows():
        sql.append(order.format(row[0], row[1], row[2]))
    return sql

def read_product_model() -> list:
    sql = []
    order = '''insert into product_model(id,product_id,model_code,model_name) 
                    values ({},{},"{}",{});'''
    product_model = readfile('product_model.csv')
    for index, row in product_model.iterrows():
        sql.append(order.format(row[0], row[1], row[2], row[3]))
    return sql

def read_salesman() -> list:
    sql = []
    order = '''insert into salesman(id,name,number,gender,age,mobile_number)  
                    values ({},'{}','{}','{}',{},'{}');'''
    salesman = readfile('salesman.csv')
    for index, row in salesman.iterrows():
        sql.append(order.format(row[0], row[1], row[2], row[3],row[4],row[5]))
    return sql

def read_supply_center() -> list:
    sql = []
    order = '''insert into supply_center(id,director_name,supply_center) 
                    values ({},'{}','{}');'''
    supply_center = readfile('supply_center.csv')
    for index, row in supply_center.iterrows():
        sql.append(order.format(row[0], row[1], row[2]))
    return sql




