import sqlite3 as sq

"users.db"
conn = sq.connect("users.db")

query = '''create table users(pp_no int not null,f_id int not null,
      destination text not null,date text not null,class text not null,bill int not null,cont int not null,name text)'''

conn.execute(query)
conn.commit()
