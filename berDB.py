import sqlite3

con = sqlite3.connect("ber.db")
print("Database opened successfully")

con.execute(
    "create table Ber (id INTEGER PRIMARY KEY NOT NULL, nev TEXT NOT NULL, brutto INTEGER NOT NULL, netto NUMERIC NOT NULL)")

print("Table created successfully")

con.close()