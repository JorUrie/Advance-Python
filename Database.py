# Connecting to the database
# importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(host = 'host', user = 'root@localhost', passwd = 'Segundodesayuno')
print(db)
# it will print a connection object if everything is fine