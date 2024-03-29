import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE users (
	UID	INTEGER PRIMARY KEY AUTOINCREMENT,
	user_name TEXT NOT NULL,
	contact TEXT,
	Book TEXT,
	IssuedDate text,
	SubmissionDate text
);'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()