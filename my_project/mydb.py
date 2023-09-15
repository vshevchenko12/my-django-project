# Install MySQL on your system
# and install libraries
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = ''
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE my_db")

print("Database created!")