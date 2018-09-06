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

with open('venues-header-diff-headers.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    # change names in placeholder to match names in csv file.
    sql = """INSERT INTO venues(name,capacity)
          VALUE (%(some_name_in_csv)s,%(capacity_in_csv)s)"""

    for row in myCSVReader:
        # use row directly
        cursor.execute(sql, row)
