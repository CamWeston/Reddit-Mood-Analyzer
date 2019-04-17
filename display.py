import sqlite3

conn = sqlite3.connect('Reddit-Mood-Analyzer.db')

c = conn.cursor()

res = c.execute("SELECT * FROM user;")

for user in res:
	print(user)
