import sqlite3

# conn = connection
conn = sqlite3.connect('s2_ex1.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)'''
)

fh = open(input('Enter file name: '))

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cursor.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()