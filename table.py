import sqlite3
import os
os.system("clear")
conn=sqlite3.connect('movie.db')  #create db
c=conn.cursor()



c.execute("""CREATE TABLE MOVIES(
    actor_name text,
    movie_name text,
    director_name text) 
""")
c.execute("SELECT * FROM MOVIES")
items=c.fetchall()
for item in items:
    print(item[0])
c.execute("INSERT INTO MOVIES VALUES('AKSHAY','BROTHERS','UDAY')")
conn.commit
conn.close()
