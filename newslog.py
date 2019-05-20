#!/usr/bin/env python3

import psycopg2

# 1. What are the most popular three articles of all time?
try:

    # Stablishing connection to the database
    connection = psycopg2.connect(user="postgres",
                                  password="cns123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="news")
    cursor = connection.cursor()

    # Excute PostgreSQL Query
    cursor.execute("""SELECT a.title,COUNT(*) AS views  FROM log l
                   JOIN articles a ON l.path=CONCAT('/article/',a.slug)
                   GROUP BY a.title
                   ORDER BY COUNT(*) desc
                   LIMIT 3;""")
    record = cursor.fetchall()

    # Iterate through records and print each row
    print("ANSWER OF QUESTION #1:", "\n")
    print("****************************************************", "\n")
    for rec in record:
        print('{article} - {count} views'.format(article=rec[0], count=rec[1]))
except (Exception, psycopg2.Error) as error:
    print("Error while loading", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()

# 2. Who are the most popular article authors of all time?
try:

    # Stablishing connection to the database
    connection = psycopg2.connect(user="postgres",
                                  password="cns123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="news")
    cursor = connection.cursor()

    # Excute PostgreSQL Query
    cursor.execute("""SELECT au.name,COUNT(*) AS views  from log l
                   JOIN articles a ON l.path=CONCAT('/article/',a.slug)
                   JOIN authors au ON a.author=au.id
                   GROUP BY au.name
                   ORDER BY COUNT(*) DESC;""")
    record = cursor.fetchall()

    # Iterate through records and print each row
    print("\n")
    print("ANSWER OF QUESTION #2:", "\n")
    print("****************************************************", "\n")
    for rec in record:
        print('{article} - {count} views'.format(article=rec[0], count=rec[1]))
except (Exception, psycopg2.Error) as error:
    print("Error while loading", error)
finally:
    #  closing database connection.
    if(connection):
        cursor.close()
        connection.close()

    #  3. On which days did more than 1% of requests lead to errors?
try:

    # Stablishing connection to the database
    connection = psycopg2.connect(user="postgres",
                                  password="cns123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="news")
    cursor = connection.cursor()
    #  Excute PostgreSQL Query
    cursor.execute("""SELECT TO_CHAR(date :: DATE, 'Month dd, yyyy') AS date,
                    ROUND((SUM(Error)*100.0)/(SUM(nonError)+SUM(Error)),2)
                    perError FROM( select date(time) date,
                    CASE WHEN status='200 OK'
                    THEN 1 ELSE 0 end as NonError,
                    CASE WHEN status!='200 OK' THEN 1 ELSE 0 END
                    AS Error FROM log) AS innerdata GROUP BY date HAVING
                    ROUND((SUM(Error)*100.0)/(SUM(nonError)+SUM(Error)),2)>1;
                    """)
    record = cursor.fetchall()
    #  Iterate through records and print each row
    print("\n")
    print("ANSWER OF QUESTION #3:", "\n")
    print("****************************************************", "\n")
    for rec in record:
        print(
            '{article} - {count}% error'.format(article=rec[0], count=rec[1]))
except (Exception, psycopg2.Error) as error:
    print("Error while loading", error)
finally:
    #  closing database connection.
    if(connection):
        cursor.close()
        connection.close()
