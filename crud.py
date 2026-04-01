import mysql.connector

#connect to database server
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port="3306",
        database="indigo"
    )
    mycursor = conn.cursor()
    print("Connected to database")
except mysql.connector.Error as e:
    print(f"Connection error: {e}")

#create database in server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

#crete a table
#airport -> airport id,code,city,name
#mycursor.execute("""
#create table airport
#(
#    airport_id integer primary key,
#    code varchar(10)  not null,
#    city varchar(50)  not null,
#    name varchar(255) not null
#)
# """)
# conn.commit()

#inseet data in table
mycursor.execute("""
insert ignore into airport values 
    (1,'ktm','kathmandu','tv'),
    (2,'pkr','pokhara','pia'),
    (3,'brt','biratnagar','bia')
""")
conn.commit()

#search/retrieve
# mycursor.execute("select * from airport where airport_id>1")
# data=mycursor.fetchall()
# print(data)
#
# for i in data:
#     print(i[3])

#update
# mycursor.execute("""
# update airport
# set name='tia'
# where airport_id=1
#                  """)
# conn.commit()

#search/retrieve


#delete
mycursor.execute("delete from airport where airport_id=1")
conn.commit()

mycursor.execute("select * from airport")
data=mycursor.fetchall()
print(data)