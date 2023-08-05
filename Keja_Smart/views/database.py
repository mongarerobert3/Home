import sqlite3

# Connect to the SQLite database
global conn
conn = sqlite3.connect("users.db")
global cursor
cursor = conn.cursor()
