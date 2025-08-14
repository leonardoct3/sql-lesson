# Script to create a sample SQLite database for the lesson
import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    content TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
''')

# Insert sample data
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?);', [
    ('Alice', 22),
    ('Bob', 30),
    ('Charlie', 17)
])

cursor.executemany('INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?);', [
    (1, 'Hello World', 'This is Alice\'s first post!'),
    (2, 'Bob\'s Thoughts', 'Bob shares his thoughts.'),
    (1, 'Another Post', 'Alice writes again.')
])

conn.commit()
conn.close()
print('Database created as sample.db')
