#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def db_connect():
    """ Creates and returns a connection to the database defined by DBNAME,
        as well as a cursor for the database.

        Returns:
            db, c - a tuple. The first element is a connection to the database.
                    The second element is a cursor for the database.
    """

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    db_c = (db, c)
    return db_c


def execute_query(query):
    """execute_query takes an SQL query as a parameter.
        Executes the query and returns the results as a list of tuples.
       args:
           query - an SQL query statement to be executed.

       returns:
           A list of tuples containing the results of the query.
    """

    try:
        db_c = db_connect()
        db = db_c[0]
        c = db_c[1]
        c.execute(query)
        res = c.fetchall()
        db.close()
        return res
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def print_top_articles():
    """Prints out the top 3 articles of all time."""
    query = """select title, count(log.path) as views
        from articles, log
        where log.path = ('/article/' || articles.slug)
        group by title
        order by views desc
        limit 3"""
    results = execute_query(query)
    print("\nTop Three Articles: ")
    print("----------------------")
    for title, views in results:
        print('\"{}\" --- {} views'.format(title, views))


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = """select name, count(log.path) as views
        from slug_author, log
        where log.path = ('/article/' || slug_author.slug)
        group by name
        order by views desc"""
    results = execute_query(query)
    print("\nAuthor Ranking: ")
    print("----------------------")
    for name, views in results:
        print('\"{}\" --- {} views'.format(name, views))


def print_errors_over_one():
    """Prints out the days where more than 1%
    of logged access requests were errors."""
    query = """select errors.date, num * 100.0 / (total) as percentage, status
        from requests, errors
        where requests.date = errors.date and  num * 100.0 / (total) > 1
        group by errors.date, percentage, status"""
    results = execute_query(query)
    print("\nDate had more than 1% of requests lead to errors: ")
    print("----------------------")
    for item in results:
        print('{0:%B %d, %Y} -- {1:.2f}% {2}'.format(
            item[0], item[1], item[2]))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
