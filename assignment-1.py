import mysql.connector as mysql

# Creating connection object
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="root"
)
if(mydb.is_connected):
    print('connected to db.')

#Creating a cursor object using the cursor() method
cursor = mydb.cursor()
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the conection
mydb.close()

# #Doping database MYDATABASE if already exists.
# cursor.execute("DROP database IF EXISTS HEINTHETUNG_6IST_12")

# #Preparing query to create a database
# sql = "CREATE database HEINTHETUNG_6IST_12"

# #Creating a database
# cursor.execute(sql)

#Retrieving the list of databases 


