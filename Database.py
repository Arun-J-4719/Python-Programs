import mysql.connector
connection=mysql.connector.connect(user='root',password='admin123',host='127.0.0.1',database='Arun')
cursor=connection.cursor()
print "Database Connected Successfully"
query="Select * from Biodata"
cursor.execute(query)
for i in cursor:
	print i
print "Enter the Details:-"
name=raw_input("Enter the Name:")
age=int(raw_input("Enter the Age:"))
city=raw_input("Enter the City:")
cursor.execute("""Insert into Biodata values ('%s','%s','%s')"""%(name,age,city))
connection.commit()
print "Inserted Successfully..."
print "Updated Table:-"
query="Select * from Biodata"
cursor.execute(query)
for i in cursor:
	print i