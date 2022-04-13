pgsql = '''
drop table if exists client_enterprise cascade;
drop table if exists supply_center cascade;
drop table if exists salesman cascade;
drop table if exists contract cascade;
drop table if exists contract_content cascade;
drop table if exists product_model cascade;
drop table if exists product cascade;
create table supply_center
(
    id   serial primary key,
    director_name varchar(35) unique not null,
    supply_center varchar(35) not null
);
create table client_enterprise
(
    id            serial primary key,
    name          varchar(60) unique not null ,
    supply_center_id int references supply_center(id) not null ,
    country       varchar(30) not null,
    city          varchar(20),
    industry      varchar(40) not null
);
create table salesman
(
    id            serial primary key,
    name          varchar(35) not null ,
    number        varchar(8) unique not null ,
    gender        varchar,
    age           int,
    mobile_number varchar(11) unique not null
);

create table product
(
    id           serial primary key,
    product_code varchar(20) unique not null ,
    product_name varchar(128) not null
);

create table product_model
(
    id            serial primary key,
    product_id    int references product (id) not null ,
    product_model varchar(64) not null,
    unit_price    int         not null
);

create table contract
(
    id                   serial primary key,
    number               varchar(10) not null unique ,
    client_enterprise_id int references client_enterprise (id) not null ,
    contract_date        date        not null,
    --estimated_delivery   date,
    --director_id          int references supply_center (id),
    unique (id, number)
);

create table contract_content
(
    id                      serial primary key,
    contract_id             int references contract (id) not null ,
    product_model_id        int references product_model (id) not null ,
    quantity                int not null,
    estimated_delivery_date date,
    lodgement_date          date,
    salesman_id             int references salesman (id) not null
);


'''

mysql = '''drop table if exists contract_content cascade;
drop table if exists contract cascade;
drop table if exists product_model cascade;
drop table if exists salesman cascade;
drop table if exists product cascade;
drop table if exists client_enterprise cascade;
drop table if exists supply_center cascade;

create table supply_center
(
    id  int  primary key,
    director_name varchar(35) unique not null,
    supply_center varchar(35) not null
);
create table client_enterprise
(
    id            int primary key,
    name          varchar(60) unique not null ,
    supply_center_id int,
    -- supply_center_id int references supply_center(id) not null ,
    country       varchar(30) not null,
    city          varchar(20),
    industry      varchar(40) not null,
    foreign key (supply_center_id) references supply_center(id)
);
create table salesman
(
    id            int primary key,
    name          varchar(35) not null ,
    number        varchar(8) unique not null ,
    gender        varchar(60),
    age           int,
    mobile_number varchar(11) unique not null
);

create table product
(
    id           int primary key,
    product_code varchar(20) unique not null ,
    product_name varchar(128) not null
);

create table product_model
(
    id            int primary key,
    product_id    int ,
        -- references product (id) not null ,
    product_model varchar(64) not null,
    unit_price    int         not null,
    foreign key (product_id) references product(id)

);

create table contract
(
    id                   int primary key,
    number               varchar(10) not null unique ,
    client_enterprise_id int,
    -- client_enterprise_id int references client_enterprise (id) not null ,
    contract_date        date        not null,
    estimated_delivery   date,
    director_id int ,
    foreign key (client_enterprise_id) references client_enterprise(id),
    foreign key (director_id) references supply_center(id),
    -- director_id          int references supply_center (id),
    unique (id, number)
);

create table contract_content
(
    id                      int primary key,
    contract_id int,
    product_model_id int,
    -- contract_id             int references contract (id) not null ,
    -- product_model_id        int references product_model (id) not null ,
    quantity                int not null,
    estimated_delivery_date date,
    lodgement_date          date,
    salesman_id int,
    foreign key (contract_id) references contract(id),
    foreign key (salesman_id) references salesman(id),
    foreign key (product_model_id) references product_model(id)
    -- salesman_id             int references salesman (id) not null
);
'''