from multiprocessing import connection
import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table= "CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)

# for one user
user=(1, 'Julie', 'Nakie')
insert_query="INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)

# for many users
users=[
    (2, 'Jeff', 'Sebz'),
    (3, 'Hubby', 'Hate'),
    (4, 'Maggie', 'iamawinner'),
    ]
cursor.executemany(insert_query, users)

# to select all users
select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row) 

connection.commit()
connection.close()