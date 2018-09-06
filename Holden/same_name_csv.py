import pymysql
import csv

# First set up the connection to the server
connection = pymysql.connect(
            host="localhost",
            user="sanchit_singhal",  # mysql user
            passwd="woods8Cloudy4moss",  # mysql passd
            db="sanchit_singhal_testdb",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
            )
cursor = connection.cursor()

with open('venues-header.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    sql = """INSERT INTO venues(name,capacity)
                VALUE (%(name)s,%(capacity)s)"""

    for row in myCSVReader:
        # use row directly when csv headers match column names.
        cursor.execute(sql, row)
