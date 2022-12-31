import sqlite3 as lite
con=lite.connect('mtica.db')

cur = con.cursor()
cur.execute("Drop TABLE IF EXISTS Cars")
cur.execute('''CREATE  TABLE     Cars( Id INT ,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'audi',1015)")
cur.execute("INSERT INTO Cars VALUES(2,'volvo',10124)")
cur.execute("INSERT INTO Cars VALUES(3,'maruthi',10153)")
cur.execute("INSERT INTO Cars VALUES(4,'beng',10157)")
cur.execute("INSERT INTO Cars VALUES(5,'hummer',101537)")
cur.execute("INSERT INTO Cars VALUES(6,'skoda',10154)")
con.commit()
print("values in table car inserted.") 




import sqlite3 as lite
con=lite.connect('mtica.db')

cur = con.cursor()
cur.execute("SELECT * FROM Cars")
rows=cur.fetchall()
for row in rows:
    print(row)






