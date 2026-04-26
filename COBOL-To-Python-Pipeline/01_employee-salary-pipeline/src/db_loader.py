import sqlite3

conn = sqlite3.connect(r"C:\cobol-to-python-pipeline\output\employee.db")
cursor = conn.cursor()

print("Database connected successfully!")
