import tkinter as tk
import sqlite3 as sql

def conect():
    sql.connect()

class login():
    def __init__(self):
       pass

    def interface(self, canva):
        canva.title('login')
        canva.geometry('800x600')

        label_name = tk.Label(canva, text='Digite seu nome')
        label_name.grid(row=3, column=3, padx=10, pady=10)
        entry_name = tk.Entry(canva)
        entry_name.grid(row=3, column=4,padx=10, pady=10)
        label_password = tk.Label(canva, text='Digite sua senha')
        label_password.grid(row=4, column=3, padx=10, pady=10)
        entry_password = tk.Entry(canva)
        entry_password.grid(row=4, column=4, padx=10, pady=10)
        label_email = tk.Label(canva, text='digite seu email')
        label_email.grid(row=5, column=3, padx=10, pady=10)
        entry_email = tk.Entry(canva)
        entry_email.grid(row=5, column=4, padx=10, pady=10)