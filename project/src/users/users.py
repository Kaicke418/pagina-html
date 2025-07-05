import sqlite3 as sql

def connect():
    sql.connect()

class users():
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    