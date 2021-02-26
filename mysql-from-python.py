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
        list_of_names = ['Jim', 'Bob']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        connection.commit()
finally:
    # Close the connection to sql,
    # regardless of whether the above was successful
    connection.close()
