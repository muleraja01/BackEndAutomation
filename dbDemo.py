import mysql.connector
from utilities.Configurations import *
# conn=mysql.connector.connect(host='localhost',database='PythonAutomation',
#                         user='root',password='9327')
conn=getConnection()
print(conn.is_connected())
cursor=conn.cursor()
cursor.execute('select * from CustomerInfo')
# row=cursor.fetchone()
# print(row)
# print(row[3])
# row=cursor.fetchone()
# print(cursor.fetchall())#List of tuples
rows=cursor.fetchall()
print(type(rows))
print(rows)
sum=0
for row in rows:
    print(row[2])
    sum=sum+row[2]
print(sum)

query= "update customerInfo set Location = %s where CourseName = %s"
data=("UK", "Jmeter")
cursor.execute(query,data)
conn.commit()


conn.close()
