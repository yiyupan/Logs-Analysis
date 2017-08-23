# Database code for the DB News

import psycopg2

DBNAME = "news"


def get_top_articles():
    """Return top 3 articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute(
        "select title, count(log.path) as views " +
        "from articles, log " +
        "where log.path = ('/article/' || articles.slug) " +
        "group by title " +
        "order by views desc " +
        "limit 3")
    top_articles = c.fetchall()
    db.close()
    return top_articles


def get_top_authors():
    """Return authors ranking by views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Create view slug_author
    '''c.execute("create view slug_author as " +
    "select slug, name from articles join authors " +
    "on articles.author = authors.id")
    '''
    c.execute(
        "select name, count(log.path) as views " +
        "from slug_author, log " +
        "where log.path = ('/article/' || slug_author.slug) " +
        "group by name " +
        "order by views desc ")
    top_authors = c.fetchall()
    db.close()
    return top_authors


def get_error_percent():
    """Return days having more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Create view requests
    '''c.execute("create view requests as " +
    "select date(time), count(*) as total " +
    "from log " +
    "group by date(time) ")
    # Create view errors
    c.execute("create view errors as " +
    "select date(time), count(status) as num, status " +
    "from log " +
    "where status != '200 OK' " +
    "group by date(time) " +
    "order by date(time)")
    '''
    c.execute(
        "select errors.date, num * 100.0 / (total) as percentage, status " +
        "from requests, errors " +
        "where requests.date = errors.date and  num * 100.0 / (total) > 1 " +
        "group by errors.date, percentage, status")
    err_prpercent = c.fetchall()
    db.close()
    return err_prpercent

print("Top Three Articles: ")
articles = get_top_articles()
for item in articles:
    print(item[0] + " --- " + str(item[1]) + " views")

print("\nAuthor Ranking: ")
authors = get_top_authors()
for item in authors:
    print(item[0] + " --- " + str(item[1]) + " views")

print("\nDate had more than 1% of requests lead to errors: ")
e = get_error_percent()
for item in e:
    print(str(item[0]) + " --- " + '%.2f' % item[1] + "% " + item[2])
