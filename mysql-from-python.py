import os
import datetime
import pymysql

# Get username
# modify this if running on another environment
username = os.getenv('C9_USER')

# Connection object to Connect to the database
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # run query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'), (24, 'Jim'), (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET Age = %s WHERE name = %s;",
                           rows)
        connection.commit()
finally:
    # Close the connection to sql,
    # regardless of whether the above was successful
    connection.close()
