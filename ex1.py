import psycopg2
from faker import Faker
import random

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.85.128", port="5432")
print("Database connected")
cur = con.cursor()
cur.execute('''CREATE TABLE customers_1
       (id INT PRIMARY KEY NOT NULL,
       name TEXT NOT NULL,
       address TEXT NOT NULL,
       age INT NOT NULL,
       review TEXT);''')
cur.execute('''CREATE TABLE customers_2
       (id INT PRIMARY KEY NOT NULL,
       name TEXT NOT NULL,
       address TEXT NOT NULL,
       age INT NOT NULL,
       review TEXT);''')


fake = Faker()

for i in range(1000000):
	if i%1000 == 0:
		print(i)
	cur.execute("INSERT INTO customers_1 (id,name,address,age,review) VALUES('"+str(i) +"','"+fake.name()+"','"+fake.address()+"','"+str(random.randint(14,90))+"','"+fake.text()+"')")
	con.commit()
	cur.execute("INSERT INTO customers_2 (id,name,address,age,review) VALUES('"+str(i) +"','"+fake.name()+"','"+fake.address()+"','"+str(random.randint(14,90))+"','"+fake.text()+"')")
	con.commit()