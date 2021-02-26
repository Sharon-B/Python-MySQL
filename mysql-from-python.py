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
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), Age int, DOB datetime);""")
        # Note that the above will display a warning (not error) if
        # the table already exists
finally:
    # Close the connection to sql,
    # regardless of whether the above was successful
    connection.close()
