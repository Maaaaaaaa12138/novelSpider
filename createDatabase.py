import sqlite3

db = sqlite3.connect("novel.db")

cursor = db.cursor()

cursor.execute("create table chapter(id integer primary key autoincrement, title varchar(255), content text, novel integer, foreign key(novel) references novel(id))")
cursor.execute("create table novel(id integer primary key, name varchar(255), author varchar(255), type varchar(255))")
db.commit()
db.close()