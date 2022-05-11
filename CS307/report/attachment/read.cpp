//
// Created by dgy on 2022/4/6.
//

#include<iostream>
#include<cstdio>
#include<stack>
#include<vector>
#include<list>
#include<algorithm>
#include<map>
#include<cctype>
#include<cmath>
#include<string>
#include<regex>
#include<set>
#include<iomanip>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<fstream>
#include<climits>
#include <random>
#include <type_traits>
#include <unordered_map>
#include <thread>


#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops,fast-math")
using namespace std;

struct csvData {
    string contract_number;
    string client_enterprise_name;
    string supply_center_name;
    string country;
    string city;
    string industry;
    string product_code;
    string product_name;
    string product_model;
    string unit_price;
    string quantity;
    string contract_date;
    string estimated_delivery_date;
    string lodgement_date;
    string director;
    string salesman_name;
    string salesman_number;
    string a;
    string age;
    string mobile_phone;
};

vector<csvData> storage;

int main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    clock_t startTime, endTime;
    startTime = clock();
    ifstream fp("contract_info.csv");
    string line;
    getline(fp, line);
//    FILE *fp;
//    fp=fopen("contract_info.csv","r");
    while (getline(fp, line)) {
        csvData data;
        istringstream iss(line);
        string temp;
        getline(iss, temp, ',');
        data.contract_number = temp;
        getline(iss, temp, ',');
        data.client_enterprise_name = temp;
        getline(iss, temp, ',');
        data.supply_center_name = temp;
        getline(iss, temp, ',');
        data.country = temp;
        getline(iss, temp, ',');
        data.city = temp;
        getline(iss, temp, ',');
        data.industry = temp;
        getline(iss, temp, ',');
        data.product_code = temp;
        getline(iss, temp, ',');
        data.product_name = temp;
        getline(iss, temp, ',');
        data.product_model = temp;
        getline(iss, temp, ',');
        data.unit_price = temp;
        getline(iss, temp, ',');
        data.quantity = temp;
        getline(iss, temp, ',');
        data.contract_date = temp;
        getline(iss, temp, ',');
        data.estimated_delivery_date = temp;
        getline(iss, temp, ',');
        data.lodgement_date = temp;
        getline(iss, temp, ',');
        data.director = temp;
        getline(iss, temp, ',');
        data.salesman_name = temp;
        getline(iss, temp, ',');
        data.salesman_number = temp;
        getline(iss, temp, ',');
        data.a = temp;
        getline(iss, temp, ',');
        data.age = temp;
        getline(iss, temp, ',');
        data.mobile_phone = temp;
        storage.push_back(data);
    }
    ofstream out_supply_center;
    out_supply_center.open("supply_center.csv");
    ofstream out_client_enterprise;
    out_client_enterprise.open("client_enterprise.csv");
    ofstream out_salesman;
    out_salesman.open("salesman.csv");
    ofstream out_product;
    out_product.open("product.csv");
    ofstream out_product_model;
    out_product_model.open("product_model.csv");
    ofstream out_contract;
    out_contract.open("contract.csv");
    ofstream out_contract_detail;
    out_contract_detail.open("contract_content.csv");
    stringstream t1,t2,t3,t4,t5,t6,t7;
    int client_enterprise_serial = 1;
    int supply_center_serial = 1;
    int salesman_serial = 1;
    int product_serial = 1;
    int product_model_serial = 1;
    int contract_serial = 1;
    int contract_content_serial = 1;
    set<string> client_enterprise_set;
    set<string> supply_center_set;
    set<string> salesman_set;
    set<string> product_set;
    set<string> product_model_set;
    set<string> contract_set;
    map<string, int> client_enterprise_map;
    map<string, int> supply_center_map;
    map<string, int> salesman_map;
    map<string, int> product_map;
    map<string, int> product_model_map;
    map<string, int> contract_map;
    for (const auto &tmp: storage) {
        if (supply_center_set.find(tmp.director) == supply_center_set.end()) {
            t1 << supply_center_serial << "|" << tmp.director << "|" << tmp.supply_center_name
               << "\n";
            supply_center_map[tmp.director] = supply_center_serial;
            supply_center_set.insert(tmp.director);
            supply_center_serial++;
        }
        if (client_enterprise_set.find(tmp.client_enterprise_name) == client_enterprise_set.end()) {
            t2 << client_enterprise_serial << "|" << tmp.client_enterprise_name << "|"
               << supply_center_map[tmp.director] <<"|"<< tmp.country << "|" << tmp.city
               << "|" << tmp.industry << "\n";
            client_enterprise_map[tmp.client_enterprise_name] = client_enterprise_serial;
            client_enterprise_set.insert(tmp.client_enterprise_name);
            client_enterprise_serial++;
        }
        if (salesman_set.find(tmp.salesman_number) == salesman_set.end()) {
            t3 << salesman_serial << "|" << tmp.salesman_name << "|" << tmp.salesman_number
               << "|" << tmp.a << "|" << tmp.age << "|" << tmp.mobile_phone << "\n";
            salesman_set.insert(tmp.salesman_number);
            salesman_map[tmp.salesman_number] = salesman_serial;
            salesman_serial++;
        }
        if (product_set.find(tmp.product_code) == product_set.end()) {
            t4 << product_serial << "|" << tmp.product_code << "|" << tmp.product_name << "\n";
            product_map[tmp.product_code] = product_serial;
            product_set.insert(tmp.product_code);
            product_serial++;
        }
        if(product_model_set.find(tmp.product_model) == product_model_set.end()){
            product_model_set.insert(tmp.product_model);
            product_model_map[tmp.product_model] = product_model_serial;
            t5 << product_model_serial << "|" << product_map[tmp.product_code] << "|"
               << tmp.product_model << "|" << tmp.unit_price << "\n";
            product_model_serial++;
        }
        if (contract_set.find(tmp.contract_number) == contract_set.end()) {
            t6 << contract_serial << "|" << tmp.contract_number << "|"
               << client_enterprise_map[tmp.client_enterprise_name] << "|" << tmp.contract_date << "\n";
            contract_set.insert(tmp.contract_number);
            contract_map[tmp.contract_number] = contract_serial;
            contract_serial++;
        }
        string temp;
        if(tmp.lodgement_date.empty()) temp="\\N";
        else temp=tmp.lodgement_date;
        t7 << contract_content_serial << "|" << contract_map[tmp.contract_number] << "|"
           << product_model_map[tmp.product_model] << "|" << tmp.quantity << "|"
           << tmp.estimated_delivery_date
           << "|" << temp << "|" << salesman_map[tmp.salesman_number] << "\n";
        contract_content_serial++;
    }
    out_supply_center<<t1.str();
    out_supply_center.close();
    out_client_enterprise<<t2.str();
    out_client_enterprise.close();
    out_salesman<<t3.str();
    out_salesman.close();
    out_product<<t4.str();
    out_product.close();
    out_product_model<<t5.str();
    out_product_model.close();
    out_contract<<t6.str();
    out_contract.close();
    out_contract_detail<<t7.str();
    out_contract_detail.close();
    endTime = clock();
    cout << "time:" << (double) (endTime - startTime) / CLOCKS_PER_SEC << endl;
}
