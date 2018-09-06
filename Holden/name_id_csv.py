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

# "Auditorium Shores","Young the Giant","2013-04-13 12:45:00"

sql_select_venue = "SELECT id from venues WHERE name = %(venue_name)s"
sql_select_band_name = "SELECT id from bands WHERE name = %(band_name)s"

sql_insert_performance = """INSERT INTO performances(start,band_id,venue_id)
                VALUE (%(start_time)s, %(band_id)s, %(venue_id)s)
"""

with open('new_performances_existing_venues.csv') as csvfile:
    # tell python about the specific csv format
    myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

    for row in myCSVReader:
        cursor.execute(sql_select_venue, row)
        results = cursor.fetchone()
        venue_id = results['id']

        cursor.execute(sql_select_band, row)
        results = cursor.fetchone()
        band_id = results['id']

        # we have what we need.
        param_dict = {'venue_id': venue_id,
                      'band_id': band_id,
                      'start_time': row['start']}
        cursor.execute(sql_insert_performance, param_dict)
