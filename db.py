import sqlite3

conn = sqlite3.connect('aula_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(25),
            senha VARCHAR(255)
          )
          ''')

conn.commit()