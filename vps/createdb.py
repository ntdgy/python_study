import sqlite3
db = sqlite3.connect('file.db')
cursor = db.cursor()
cursor.execute('ALTER TABLE Words ADD COLUMN id int')
# cursor.execute('insert into words (word) values ("戴菜菜无信息处理功能，望周知")')
# cursor.execute('insert into words (word) values ("Frankss is our best seller!")')
# cursor.execute('insert into words (word) values ("Froster强强！")')
# cursor.execute('CREATE TABLE jichou( id INTEGER PRIMARY KEY, record TEXT)')
db.commit()
