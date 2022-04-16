# CS307 Project 1

**Contributor**:

- 戴郭轶 12011211
- 周凡卜 12012519

# Task 1: E-R Diagram

**Software:** `draw.io`

![ER.drawio](https://pic.cdn.ntdgy.top/images/2022/04/16/ER.drawio-16500220674913.png)

# Task 2: Database Design

![img](https://pic.cdn.ntdgy.top/images/2022/04/16/datagripER-16500220595722.png)

The id of each table is the serial primary key of each table.

**Supply_center: **

- director_name: As each director only in charge of one center, so we put it in the supply center
- supply_center: The name of supply center, unique

**Client_enterprise:**

- name: The name of enterprise
- supply center id: The foreign key which links to supply center
- country: Where the enterprise comes from
- city: Where the enterprise comes from
- industry: The enterprise's industry
- unique by (name, country, city, industry) as all elements can have the same name

**Contract:**

- number: The contract number, which is unique
- client enterprise id: The foreign key which links to client enterprise
- contract date: The date when the contract made
- unique by number, as each contract should be only made to one enterprise for ease of change.

**Product:**

- product code: The unique code of product
- product name: The name of it

**Product model:**

- product model: The unique name of the specified model
- unit price: Price of this model

**Salesman:**

- name: Name of salesman
- gender: Female or male
- age: Age of salesman
- mobile number: As name can be repeated, use it as unique

**Contract content:**

- product model id: Foreign key links to product model
- quantity: The quantity needed
- estimated delivery date: the estimated time
- lodgement date: the actual time
- salesman id: Who in charge of this item of contract
- As a contract may contain many items, divide them into a smaller table

# Task 3: Data import

In this part, we tried two main ways to import data. 

Time cost of each code.

![importtime](https://pic.cdn.ntdgy.top/images/2022/04/16/importtime.png)

```
-Java
  -goodloader
  -multiple thread
  -trigger off
-Python
  -pure python
  -cpp data process and python import
```

## Java import

Java part, we first divide the csv into tables and store into memory temporarily.

Secondly, according to the E-R diagram, we do top down insertion and get the order stored.

Then insert line by line.

At first, we used our cloud server, but the time is too horrible. And we found the limit is mainly on network IO. So we changed to local postgresql server. Getting speed up of 3.71 times.

And according to the E-R diagram, we can find there are three row parallel, which can be used in multiple threading. Then we get a  time record of 2.325s.

The rest part, I cancel the triggers as I can manually maintain the data availability. Finally, the time of java part reduced to average of 1.128s.

![Time](https://pic.cdn.ntdgy.top/images/2022/04/16/java-compare.png)

The optimize rate, with baseline of goodloader.

![improving rate](https://pic.cdn.ntdgy.top/images/2022/04/16/javaimproverate.png)

## Python import

Firstly, i find that psycopg2 provides the function that allows us to copy  data directly from a csv file to database with a efficiency same as function insert with batch. So i choose to pre_process the data and generate .csv files and import it with the functions. As we all know, if we write to much to the disk, the limitations is our disk io, so i choose the use python io.String that creates a csv like file and read it directly in memory.

I use cloudserver at the begining. ![image-20220416014145596](C:\Users\dgy\AppData\Roaming\Typora\typora-user-images\image-20220416014145596.png)

The contact_content time seems to long because it is not corresponding to the size proportion of contract, and at the same time, the network monitor find a peek at the rate of my vps network limitation, so i suppose that the limitation is network io.

The next test is on my own computer with the connection to localhost with the negligible latency and network limitation. The result is below:

![image-20220416014837588](C:\Users\dgy\AppData\Roaming\Typora\typora-user-images\image-20220416014837588.png)

The import time of contract_content is reduced to 0.85s. We can find that pre_process costs most time. So my next step is to optimize the pre_process period.

My first consideration is use muilty_threads(csv). So 

# Part 4. Benchmark

