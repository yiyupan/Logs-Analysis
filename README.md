# Logs-Analysis

## I. Design of Code
#### Description of the project
In this project, a Python program was built as a reporting tool in which **psycopg2** module was used to connect the database which is a PostgreSQL database for a fictional news website. This _news_ database contains three tables as follows:
  1. Table **articles** with columns *author*, *title*, *slug*, *lead*, *body*, *time* and *id*:
    - Primary key: *id*;
    - Foreign key: *author*, references Table **authors**(*id*).
  2. Table **authors** with columns *name*, *bio* and *id*:
    - Primary key: *id*, referenced by Table **articles**(*author*)
  3. Table **log** with columns *path*, *ip*, *method*,*status*, *time*, *id*:
    - Primary key: *id*.
    
#### Tasks of the project
Here are three questions the reporting tool should answer:
  1. __What are the most popular three articles of all time?__ Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
  2. __Who are the most popular article authors of all time?__ That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
  3. __On which days did more than 1% of requests lead to errors?__ The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

#### Construction of the code
In the Python program, three functions were constructed: 
  1. **print_top_articles()**: return top three articles
  2. **print_top_authors()**: return authors' ranking
  3. **print_errors_over_one()**: return dates which had more than 1% of requests lead to errors
  

## II. Run the Code
#### Step 1: DOWNLOAD DATA
  - Download and install [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtualbox](https://www.virtualbox.org/wiki/Downloads) on your computer.
  - Download and install [the Vafrantfile](https://github.com/yiyupan/fullstack-nanodegree-vm), where _news_ database has been already set.
  - Download and unzip the `newsdata.zip` folder to get the file `newsdata.sql`. Move this file and the `newsdatadb.py` file into `vagrant` directory which is shared with your virtual machine.
#### Step 2: LOG INTO VIRTUAL MACHINE
Open up the `vagrant` directory. To use the command `vagrant up` to bring the virtual machine back online, and log into it with `vagrant ssh`.
#### Step 3: LOAD DATABASE
Access to shared files by using the command `cd \vagrant`.
Use the command `psql -d news -f newsdata.sql` to load the data. 
#### Step 4: CREAT VIEW
We should create three views before we run the code. A SQL script has written for this purpose, so you can import the views from the command line by tpying: `psql -d news -f create_views.sql`.
#### Step 5: RUN PYTHON
Use the command `python newsdatadb.py` to run relavant python program and get required output.
