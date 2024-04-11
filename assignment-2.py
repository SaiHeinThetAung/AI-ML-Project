import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='root', 
host='127.0.0.1', database='HEINTHETUNG_6IST_12')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS DOCTOR")

sql ='''CREATE TABLE DOCTOR(
 DOCTOR_ID INT NOT NULL,
 DOCTOR_NAME CHAR(20),
 HOSPITAL_ID INT NOT NULL,
 JOINDATE DATE, 
 SPECIALITY CHAR(20),
 SALARY FLOAT,
 EXPERIENCE CHAR(50) NULL)'''
cursor.execute(sql)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO DOCTOR(DOCTOR_ID,
 DOCTOR_NAME, HOSPITAL_ID, JOINDATE, SPECIALITY,SALARY,EXPERIENCE)
 VALUES (101, 'David',1 , '2005-02-10','Pediatric',40000,NULL)"""

try:
 # Executing the SQL command
 cursor.execute(sql)
 # Commit your changes in the database
 conn.commit()
except:
 # Rolling back in case of error
 conn.rollback()
#Closing the connection
conn.close()