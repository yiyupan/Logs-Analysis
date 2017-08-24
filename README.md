# Logs-Analysis

## Design of Code
In this project, a Python program was built as a reproting tool in which **psycopg2** moudle was used to connect the database.

In the Python program, three functions were constructed: 
  1. **get_top-articles()**: return top three articles
  2. **get_top_authors()**: return authors' ranking
  3. **get_error_percent()**: return dates which had more than 1% of requests lead to errors
  

## Run the Code
#### Step 1: DOWNLOAD DATA
First of all, download `FSND-Virtual-Machine` file, where `news database` has been already set.
#### Step 2: LOG INTO VIRTUAL MACHINE
Open up the `vagrant` directory. To use the command `vagrant up` to bring the virtual machine back online, and log into it with `vagrant ssh`.
#### Step 3: LOAD DATABASE
Access to shared files by using the command `cd \vagrant`.
Use the command `psql -d news -f newsdata.sql` to load the data. 
#### Step 4: CREAT VIEW
We should create three views before we run the code. And here are statements for these views, just copy and paste on Git Bash.
1. Create view slug_author: 
```
create view slug_author as 
select slug, name from articles join authors 
on articles.author = authors.id
```
2. Create view requests: 
```
create view requests as
select date(time), count(*) as total 
from log
group by date(time)
```
3. Create view errors:
```
create view errors as 
select date(time), count(status) as num, status 
from log 
where status != '200 OK' 
group by date(time) 
order by date(time)
```
#### Step 5: RUN PYTHON
Use the command `python newsdatadb.py` to run relavant python program and get required output.
