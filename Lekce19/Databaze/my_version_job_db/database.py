import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

#adding section
#cur.execute("""create table users(
#            ID INTEGER PRIMARY KEY,
#            name TEXT,
#            job TEXT,
#            experience INTEGER)""")

#cur.execute("INSERT INTO users VALUES (1, 'John', 'Developer', 5)")
#cur.execute("INSERT INTO users VALUES (2, 'Mary', 'Designer', 10)")
#cur.execute("INSERT INTO users VALUES (3, 'Mike', 'Manager', 2)")

#conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("all users in database:")
for row in rows:
    print(row)

for row in rows:
    print(row[1])

print("Users with more than 4 years of experience via python function:")
for row in rows:
    if row[3] > 4:
     print(row[0], row[1])

print("Users with more than 4 years of experience via SQL cmnd:")
cur.execute("SELECT * FROM users WHERE experience > 4")
rows = cur.fetchall()
for row in rows:
    print(row[1])

conn.close()

