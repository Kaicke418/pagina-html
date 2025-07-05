import sqlite3 as sql
import tkinter as tk
from login.logins import login as log

Login = log()

canva = tk.Tk()
Login.interface(canva)
canva.mainloop()