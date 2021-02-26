import os
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
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()      # getting the data back
        print(result)
finally:
    # Close the connection to sql,
    # regardless of whether the above was successful
    connection.close()
