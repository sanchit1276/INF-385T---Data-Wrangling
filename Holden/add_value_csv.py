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
    # tell python about the specific csv format
    myCSVReader = csv.DictReader(csvfile)

    # Query has type added, must also set up in database.
    sql = """INSERT INTO venues(name,capacity,type)
                  VALUE (%(name)s,%(capacity)s,%(type)s)"""
    # move row by row through the file
    for row in myCSVReader:
        param_dict = {'name': row["csv_name"],
                      'capacity': row["csv_capacity"],
                      'type': "outdoor"}
        cursor.execute(sql, param_dict)
