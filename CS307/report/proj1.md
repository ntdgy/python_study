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
  -cpp data process and python import with trigger off
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

I use cloudserver at the begining. ![image-20220416014145596](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py1.png)

The contact_content time seems to long because it is not corresponding to the size proportion of contract, and at the same time, the network monitor find a peek at the rate of my vps network limitation, so i suppose that the limitation is network io.

The next test is on my own computer with the connection to localhost with the negligible latency and network limitation. The result is below:

![image-20220416014837588](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py2.png)

The import time of contract_content is reduced to `0.85s`. We can find that pre_process costs most time. So my next step is to optimize the pre_process period.

My first consideration is use muilty_threads(`multi_thread.py`). However, python has the fake multicore process, the pre_process costs much more than before:

![image-20220416022146030](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py3.png)

So we must change the ideas. The potentiality of python has been excavated. So i decided to use cpp as an substitute. The cpp code is `read.cpp `. The optimization of cpp is use stringstream to substitute fileout. It can be optimized for 0.1s. The result of cpp is:

![image-20220416025248215](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py4.png)

Then import is with python(import_cpp.py):

![image-20220416033853680](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py5.png)

We can find that the total time comsumption is reduced to `1.586s`. Which is much more faster.(If i have a better ssd, it would be faster.)

If we turn off the trigger, the total time will be further reduced to `0.933s`.

![image-20220416031103378](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py6.png)

The pure python script with trigger off(`import_data.py`) is:

![image-20220416141030295](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py7.png)

The comparison is below:

![image-20220416141233372](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py8.png)

The optimize rate, with baseline of localhost:

![image-20220416141311403](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\py9.png)

# Part 4. Benchmark

### Test description:

In order to test the performance of different database, so i use a data generator(`data_creator.py`) to create more data. It is about `2.05 Gb` and after processing(`read.cpp`), the lines of the table is:

```
supply_center:  10000
client_enterprise: 432243
salesman: 100000
product: 86545
product_model: 200000
contract: 1000000
contract_content: 9000758
```

The insert test requires `import_data_test.py`, `innitial.py` ,`pgsql_reader.py` and `filedb_reader.py`. It creates import order and then excute `insert one by one`. Then compare the total time. The lines counts are listed above.

The select test requires `select_test.py` it generates 

```
supply_center:  1009
client_enterprise: 1009
salesman: 1027
product: 1018
product_model: 2009
contract: 1000
contract_content: 1000
```

orders to test the select efficiency to database.

The update test requires `update_test.py` . It will generate `1000` test cases to every table.

The delete test requires `delete_test.py` It only generates `1000` test cases to table `contract_content`.

You can use `testbench.py` to conduct all test at one time.

For `Debian/Ubuntu` users, we provides bash script `prepare.sh` to get your environment ready for the test. 

### Test 1:

#### Environment:

- CPU: AMD Ryzen 7 5800X 8-Core Processor，3801 Mhz

- Memory: Gloway 3200Mhz 16G * 2

- Swap: 64G

- SSD: Asgard AN2 1TB with 10% spaces left

- Oprating System: Windows 10 Professional version 19043

- Postgresql version: 14.2

- g++ compiler: mingw64 w64 6.0

- Python version: python 3.10

#### Database Structure:

We promise that our test data is the same format of task 3. So we use the same database as task 3.

#### Result:

You can get the detailed result at the `result1.txt`.

![image-20220416152351043](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re1.png)

![image-20220416152512474](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re2.png)

![image-20220416152613711](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re3.png)

![image-20220416152708428](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re4.png)

### Test 2:

#### Environment:

- CPU: Intel(R) Xeon(R) Platinum 8124M CPU @ 3.00GHz * 2

- Memory: ddr4 reg ecc 2r*4 16G 2666Mhz 12-channel

- Ramdisk: 64Gb

- Oprating System: Linux version 5.13.0-39-generic (buildd@lcy02-amd64-072) (gcc (Ubuntu 11.2.0-7ubuntu2) 11.2.0, GNU ld (GNU Binutils for Ubuntu) 2.37) #44-Ubuntu

- Ubuntu version: Ubuntu 21.10 impish

- Postgresql version: 13.6

- g++ compiler: gcc 11.2.0

- Python version: python 3.8

  ##### Note: Postgresql run on the ramdisk as well.

#### Database Structure:

We promise that our test data is the same format of task 3. So we use the same database as task 3.

#### Result:

You can get the detailed result at the `result2.txt`.

![image-20220416152949769](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re5.png)

![image-20220416153122350](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re6.png)

![image-20220416153327041](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re7.png)

![image-20220416153646924](C:\Users\dgy\OneDrive - Trash Network\GitHub\python_study\CS307\report\pic\re8.png)

### Analysis:

1. In most cases, for examle, simple `insert`, `update`,`delete` actions, sqlite has the fastest rate.Howerver, it does not support complex search queries and if the select command is more complex it will costs more time for the limitations of disk io.

2. The File DB has the close time complexity to postgresql in result 1, result 2 is for some other reason. However, `select` order doesn't support complex functions, rather than `join` or other functions.

3. Postgresql and SQLite support use index to speed up searching function with multy tables. It's really difficult for File system to support index.

4. In File DB, every order will be excuted immediately while the other SQLs supports cache locally and the commit to excute which enables us to roll back in some conditions.

5. The database structure was defined when finishing our code of file db while for databases we can change it.

6. You can read the database at one time for several users while it is impossible for file db.

### Other:

###### Ramdisk:

1. SQLite and file DB becomes much faster than on common SSD. Because the operations of are based on the change of the file system. So the spped is limited to Storage IO. So they become faster when using ramdisk.
2. Postgresql use ram as buffer for the operations, so it would not faster when using ramdisk. That's why the time cost in test1 is almost the same as file db while moch slower in test2.

###### Insert time:

1. SQLite and file db won't do the `type checking` while postgresql need it while do every insert. So it becomes much slower than SQLite.
2. The unique check is conducted by hashset in file db, so it won't support muilty cores check.

###### Index:

1. Our structure of database use primary keys as foreign keys and postgresql will create index automatically to the unique columns. So there is no need for us to create it manually.
