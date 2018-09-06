import pymysql
import pprint

# First set up the connection to the server
connection = pymysql.connect(
            host="localhost",
            user="sanchit_singhal",  # mysql user
            passwd="woods8Cloudy4moss",  # mysql passd
            db="class_music_festival",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
            )
with connection.cursor() as cursor:
    # SQL queries are just a string.
    sql = "SELECT * FROM venues"
    cursor.execute(sql)
    results = cursor.fetchall()  # list of dicts

    print(sql)
    pprint.prrint(result)
    #for row in results:
    #    output = "Venue: {name} has Capacity: {capacity}"
    #    print(output.format(**row))
