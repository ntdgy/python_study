# -*- coding = utf-8 -*-
# @Time: 2022/4/11 19:29
# @Author: Anshang
# @File: fileDBMS.py
# @Software: PyCharm
import json
import re
import os
import copy


class DBMS(object):

    def __init__(self, file=''):
        self.file = file
        if file != '':
            if os.path.exists(file):
                with open(file, 'r') as f:
                    self.tree = json.loads(f.read())
            else:
                self.tree = {}
        else:
            print("please select a DBMS file")
        pass

    re_condition = re.compile(r"(?P<key>[^\s]+?) *(?P<sign>[<>]*)= *(?P<value>[^\s;]+)", re.I)
    sel = re.compile(r" *select +(?P<col>.*?) +from +(?P<table>.*?) +where +(?P<condition>.*?); *", re.I)
    ins = re.compile(r" *insert +into +(?P<table>.*?)[(](?P<col>.*?)[)] +values[(](?P<value>.*?)[)]; *", re.I)
    up = re.compile(r" *update +(?P<table>.*?) +set +(?P<set>.*?) +where +(?P<condition>.*?); *")
    dele = re.compile(r" *delete +from +(?P<table>.*?) +where +(?P<condition>.*?); *", re.I)
    aor = re.compile(r"\s+(and|or)\s+")

    def excuse(self, sql: str):
        r = self.sel.match(sql)
        if r:
            return self.select(r.group('col'), r.group('table'), r.group('condition'))
        r = self.ins.match(sql)
        if r:
            return self.insert(r.group('table'), r.group('col'), r.group('value'))
        r = self.up.match(sql)
        if r:
            return self.update(r.group('table'), r.group('set'), r.group('condition'))
        r = self.dele.match(sql)
        if r:
            return self.delet(r.group('table'), r.group('condition'))
        pass

    def condition_judge(self, table: str, c: tuple, selected: list):
        if c[1] == '<':
            for k, v in self.tree[table][c[0]]:
                if int(v) < int(c[2]):
                    if k not in selected and v != '114514Deleted':
                        selected.append(k)
        if c[1] == '>':
            for k, v in self.tree[table][c[0]]:
                if int(v) > int(c[2]):
                    if k not in selected and v != '114514Deleted':
                        selected.append(k)
            pass
        if c[1] == '':
            for k, v in self.tree[table][c[0]].items():
                if v == c[2].replace("'", ""):
                    if k not in selected and v != '114514Deleted':
                        selected.append(k)
            pass

    def get_condition(self, table, condition):
        conditions = self.re_condition.findall(condition)
        aor = self.aor.findall(condition)
        index = -1
        selected = []
        for c in conditions:
            if index >= 0:
                if aor[index] == 'and':
                    new_select = copy.deepcopy(selected)
                    for i in selected:
                        try:
                            if c[1] == '<':
                                if not int(self.tree[table][c[0]][i]) < int(c[2]):
                                    new_select.remove(i)
                            if c[1] == '>':
                                if not int(self.tree[table][c[0]][i]) > int(c[2]):
                                    new_select.remove(i)
                                pass
                            if c[1] == '':
                                if not self.tree[table][c[0]][i] == c[2].replace("'", ""):
                                    new_select.remove(i)
                                pass
                        except KeyError:
                            new_select.remove(i)
                        pass
                    selected = new_select
                else:
                    self.condition_judge(table, c, selected)
            else:
                self.condition_judge(table, c, selected)
            index = index + 1
        return selected

    def select(self, col, table, condition):
        col_list = re.split(r'[\s,]+', col)
        index = -1
        result = ''
        selected = self.get_condition(table, condition)
        for index in selected:
            for c in col_list:
                if c == '*':
                    for column in self.tree[table]:
                        if column == 'len':
                            continue
                        try:
                            result = result + self.tree[table][column][index] + ' '
                        except KeyError:
                            result = result + 'NULL '
                else:
                    result = result + self.tree[table][c][index] + ' '
            result = result + '\n'
        return result

    def insert(self, table, col, value):
        col_list = re.split(r'[\s,]+', col)
        value_list = re.split(r'[\s,]+', value)
        # print(col_list, value_list)
        length = self.tree[table]['len']
        for i in range(len(col_list)):
            #print(i, table, length, col_list[i], value_list[i])
            if value_list[i].replace("'", "").lower() == 'null':
                continue
            self.tree[table][col_list[i]][str(length)] = value_list[i].replace("'", "")
        self.tree[table]['len'] = length + 1
        pass

    sett = re.compile(r"(.*?)[\s=]+(.*)")

    def update(self, table, setting, condition):
        selected = self.get_condition(table, condition)
        setting_list = re.split(r'[,]+', setting)
        settings = []
        for s in setting_list:
            print(s.strip())
            temp = self.sett.match(s.strip())
            settings.append((temp.group(1), temp.group(2).replace("'", "")))
        print(settings)
        table = self.tree[table]
        for i in selected:
            for t in settings:
                table[t[0]][i] = t[1]
            pass
        pass

    def delet(self, table, condition):
        selected = self.get_condition(table, condition)
        table = self.tree[table]
        for i in selected:
            for column in table:
                if column == 'len':
                    continue
                table[column][i] = '114514Deleted'
        pass

    def newDB(self):
        self.tree['supply_center'] = {'id': {}, "director_name": {}, 'supply_center': {}, 'len': 0}
        self.tree['client_enterprise'] = {'id': {}, 'name': {}, 'supply_center_id': {}, 'country': {}, 'city': {},
                                          'industry': {}, 'len': 0}
        self.tree['salesman'] = {'id': {}, 'name': {}, 'number': {}, 'gender': {}, 'age': {}, 'mobile_number': {}, 'len': 0}
        self.tree['product'] = {'id': {}, 'product_code': {}, 'product_name': {}, 'len': 0}
        self.tree['product_model'] = {'id': {}, 'product_id': {}, 'product_model': {}, 'unit_price': {}, 'len': 0}
        self.tree['contract'] = {'id': {}, 'number': {}, 'client_enterprise_id': {}, 'contract_date': {}, 'len': 0}
        self.tree['contract_content'] = {'id': {}, 'contract_id': {}, 'product_model_id': {}, 'quantity': {},
                                         'estimated_delivery_date': {}, 'lodgement_date': {}, 'salesman_id': {}, 'len': 0}

    def close(self):
        with open(self.file, "w") as f:
            f.write(json.dumps(self.tree))


if __name__ == '__main__':
    a = DBMS('./test.json')
    # a.newDB()
    # a = DBMS('./test.json')
    a.excuse("insert   into supply_center(id, director_name)    values(2, 'name');")
    a.excuse("insert   into supply_center(id, director_name)    values(2, 'test');")
    a.excuse("insert   into supply_center(id, director_name, supply_center)    values(5, 'test', 'center');")
    a.excuse("update supply_center set id = 5, director_name = 'jbjbjb' where id = 2;")
    print(a.excuse("select * from supply_center where id = '2' and director_name = 'test' or supply_center = 'center';"))
    a.close()
