import sqlite3

conn = sqlite3.connect("chat.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL0)""")

cur.execute("""CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    FOREIGN KEY (user_id) REFERENCES users(id))""")




#cur.execute("""INSERT INTO users (name, age) VALUES ('Jan', 33)""")
#cur.execute("""INSERT INTO users (name, age) VALUES (?, ?)""", ("Adam", 23))
cur.execute("""INSERT INTO courses (name, description, capacity) VALUES (?, ?, ?)""", ("Adam", "test",23))

db_insert(cur, "users",
          ["('user1', 'password1')]
           ('user2', 'password2'),
           ('user3', 'password3');])


db_insert(cur, "courses",
          ["name", "description", "capacity"],
          ["Matematika", "Cesta peklem", 23])

conn.commit()

cur.execute("SELECT * FROM courses")
rows = cur.fetchall()
print(rows)
print("-------")
for row in rows:
   print(row[1], row[2])

conn.close()


def db_insert(db_cur, table, cols, vals):
   # check table
   if len(cols) != len(vals):
      return False

   columns = ""
   for item in cols:
      columns += f"{item},"
   """
   values = ""
   for item in vals:
      values += f"'{item}',"
   """

   values = ""
   for item in range(len(vals)):
      values += "?,"

   try:
      query = f"""INSERT INTO {table} ({columns[:-1]}) VALUES ({values[:-1]})"""
      db_cur.execute(query, vals)
   except:
      return False

   return True