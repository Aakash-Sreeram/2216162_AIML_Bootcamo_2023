import sqlite3 as sq

"flights.db"
conn = sq.connect("flights.db")

query = '''create table flights(f_id int primary key,f_name text not null,T_seats int not null,b_seats int,
        destination text not null,date text not null,class text not null,bill int not null)'''

conn.execute(query)
conn.commit()
