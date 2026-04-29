import sqlite3 
import pandas as pd 

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT,
        salary REAL,
        contract TEXT
    )
""")

data = [
   ("ali", "casablanca", 5000, "CDI"),
   ("sara", "rabat", 4500, "CDD"),
   ("omar", "fes", 6000, "CDI"),
   ("lina", "casablanca", 3500, "CDI"),
   ("ahmed", "rabat", 5500, "CDD")
]

cursor.executemany("""
    INSERT INTO employees (name, city, salary, contract)
    VALUES (?, ?, ?, ?)
""", data)

conn.commit()

print("=== all data ===")
print(pd.read_sql("SELECT * FROM employees", conn))

print(pd.read_sql("SELECT * FROM employees WHERE city = 'casablanca'", conn))
print(pd.read_sql("SELECT * FROM employees WHERE salary > 5000", conn))
print(pd.read_sql("SELECT * FROM employees ORDER BY salary DESC", conn))

conn.close()