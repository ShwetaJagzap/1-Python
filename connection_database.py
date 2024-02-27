# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:38:22 2023

@author: ACER
"""
'''pg2 - alias name'''

import psycopg2 as pg2

#create a connection with postgresql
#'password' is whether password you set, we set passwoord
# in the install

conn = pg2.connect(database='dvdrental',user='postgres',password='root')

#establish connection and start cursor to be ready to query

cur=conn.cursor()

#pass in a postgresql qury as a string
cur.execute("select * from payment")

#return a tuple of the first row as python objects
cur.fetchone()

#return N NUMBER OF ROWS
cur.fetchmany(10)

#return all rows at ones
cur.fetchall()

#to save the index results assign it to a variable
data=cur.fetchmany(10)

#close the connection
conn.close()

#after installing with pip install 
import psycopg2 as pg2

conn = pg2.connect(database='Testme',user='postgres',password='root')

cur=conn.cursor()
#exicute a commant :create courses table
cur.execute(""" create table courses(
    course_id serial primary key,
    course_name varchar (50) unique not null,
    course_instructor varchar (100) not null,
    topic varchar (20)not null);""")

conn.commit()
cur.close()


##########################################################
#nseriong values in the table
import psycopg2 as pg2
conn = pg2.connect(database='Testme',user='postgres',password='root')
cur=r=conn.cursor()
cur.execute("Insert into courses(course_name,course_instructor,topic)values('Introduction to sql' ,'Ram','julia')")
cur.execute("Insert into courses(course_name,course_instructor,topic)values('Introduction to ChatGpt' ,'Shreya','RK')")
cur.execute("Insert into courses(course_name,course_instructor,topic)values('Introduction to Java' ,'Shweta','JK')")
cur.execute("Insert into courses(course_name,course_instructor,topic)values('Introduction to Python' ,'Sayali','MK')")
cur.execute("Insert into courses(course_name,course_instructor,topic)values('Introduction to database' ,'OM','SS')")

conn.commit()
cur.close
conn.close

########################################################
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()
cur.execute('select * from courses;')
rows=cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)
    
#####################################################
#GROUP BY
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

#GROUP BY 
cur.execute('SELECT course_instructor,count(*) from courses GROUP BY course_instructor')

#make the chaanges to changes to the database persistent 
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)

#ORDER BY
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

#ORDER BY
cur.execute('SELECT course_instructor from courses ORDER BY course_instructor')

#make the chaanges to changes to the database persistent 
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
    
####################################################
import psycopg2 as pg2

conn = pg2.connect(database='Testme',user='postgres',password='root')

cur=conn.cursor()
#exicute a commant :create courses table
cur.execute(""" create table course_adminn(
    course_id serial primary key,
    course_fee varchar (50) unique not null,
    course_duration varchar (100) not null);""")

conn.commit()
cur.close()
#########################################################
#INEER JOINs
import psycopg2 as pg2
conn = pg2.connect(database='Testme',user='postgres',password='root')
cur=r=conn.cursor()
cur.execute("Insert into course_adminn(course_fee,course_duration)values(2000,'2year')")
cur.execute("Insert into course_adminn(course_fee,course_duration)values(4000,'3Month')")
cur.execute("Insert into course_adminn(course_fee,course_duration)values(3000,'4Month')")
cur.execute("Insert into course_adminn(course_fee,course_duration)values(40000,'5month')")
cur.execute("Insert into course_adminn(course_fee,course_duration)values(3500,'2Month')")

conn.commit()
cur.close
conn.close

cur.execute('''select course_name,course_instructor,topic,course_fee,course_duration from courses inner join course_adminn on courses.course_id=course_adminn.course_id''')
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
