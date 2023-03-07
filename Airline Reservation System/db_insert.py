import sqlite3 as sq

"flights.db"
conn = sq.connect("flights.db")

q = '''
    insert into flights values(127,'SpiceJet',6,2,'Canada','2023-02-12','Business Class',30000)'''
conn.execute(q)
conn.commit()
q = '''insert into flights values(123,'Vistara',4,3,'Canada','2023-02-14','Economy Class',15000)'''
conn.execute(q)
conn.commit()
q='''insert into flights values(121,'Air India Express',7,6,'USA','2023-02-12','First Class',12000)'''
conn.execute(q)
conn.commit()
q = '''insert into flights values(125,'Indigo',8,6,'USA','2023-02-14','Business Class',14000)'''
conn.execute(q)
conn.commit()
q= '''insert into flights values(128,'Vistara',3,1,'USA','2023-02-16','Economy Class',11000)'''
conn.execute(q)
conn.commit()
q='''insert into flights values(129,'Go Air',2,0,'USA','2023-02-16','Economy Class',10000)'''
conn.execute(q)
conn.commit()
q='''insert into flights values(122,'SpiceJet',5,2,'Australia','2023-02-12','First Class',16000) '''
conn.execute(q)
conn.commit()
q='''insert into flights values(124,'Go Air',9,8,'Australia','2023-02-14','Business Class',14000) '''
conn.execute(q)
conn.commit()
q='''insert into flights values(126,'Air India Express',2,0,'Australia','2023-02-14','Economy Class',12000) '''
conn.execute(q)
conn.commit()




