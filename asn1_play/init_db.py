import sqlite3

connection = sqlite3.connect('db/database.db')

with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('Open source Tools', 'All the Tools provided here are open source. Code can be found at Github.', 'Admin')
            )

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('Asn1Play', 'I am using this tool from couple of years & it helps me boost my Productivity', 'Pratik')
            )

connection.commit()
connection.close()
