import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')
fh = open('mbox-short.txt')
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))  #the "?" prevents SQL injection (cybersecurity vulnerabilty); the email in the tuple replaces the "?"; the comma is there to make it a tuple
    row = cur.fetchone() #row is tuple of the first one in the table; removes tuple from the selected set, but leaves database untouched
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,)) #str and tuple must be included
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit() #saves to hard drive; allows sqlite to update with new information
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1]) #row is a tuple
cur.close()
