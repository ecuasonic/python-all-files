import sqlite3

class Person:

    def __init__(self, id=-1, first='', last='', age=-1):
        self.id = id
        self.first = first
        self.last = last
        self.age = age

        self.conn = sqlite3.connect('mydata.db') # creates the database
        self.cur = self.conn.cursor()

    def load_person(self, id):
        self.cur.execute('''
        SELECT * FROM persons
                       WHERE id = ?
        ''', (id,))

        results = self.cur.fetchone()

        self.id = id
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
        self.conn.close()

    def insert_person(self):
        self.cur.execute('''
        INSERT INTO persons (first_name, last_name, age) VALUES
                         (?,?,?)
        ''', (self.first, self.last, self.age))
        self.conn.commit()
        self.conn.close()

p1 = Person()
p1.load_person(1)
print(p1.first, p1.last, p1.age)

p2 = Person(7, "Alex", "Robbins", 30)
p2.insert_person()

conn = sqlite3.connect('mydata.db') # creates the database
cur = conn.cursor()

cur.execute('SELECT * FROM persons')
rows = cur.fetchall()
print(rows)

cur.execute('''
DROP TABLE IF EXISTS persons 
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS persons (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT,
            last_name TEXT, 
            age INTEGER
)
''')

cur.execute('''
INSERT INTO persons (first_name, last_name, age) VALUES
            ('Paul', 'Smith', 24),
            ('Mark', 'Johnson', 42),
            ('Anna', 'Smith', 34)
''')

cur.execute('''
SELECT * FROM persons
''')

rows = cur.fetchall()
print(rows)


conn.commit()
conn.close()