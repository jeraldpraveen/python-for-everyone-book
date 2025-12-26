import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('./15-databases/51-example.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Tracks')
cursor.execute('''CREATE TABLE Tracks (
        title TEXT,
        plays INTEGER
    )''')
print("Table 'Tracks' created successfully.")

cursor.execute(
    'INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Song', 100))
cursor.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
               ('Another Song', 150))
conn.commit()

print("Track records inserted successfully.")
cursor.execute('SELECT * FROM Tracks')
rows = cursor.fetchall()
print("Tracks in the database:")
for row in rows:
    print(row)
# Close the connection
conn.close()
# The program creates a SQLite database file named 'example.db' and
# creates a table named 'Tracks' with two columns: 'title' (TEXT) and 'plays' (INTEGER).
