import sqlite3 as sq

"users.db"
conn = sq.connect("users.db")

records = conn.execute("select * from users")
print(records)
for i in records:
    print(i)