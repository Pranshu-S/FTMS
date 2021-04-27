# Import Tkinter Module
from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk
from tkinter import ttk

conn=sqlite3.connect('FTMS.db')
crsr=conn.cursor()
tables = ['FARMER', 'CROP_GROWN', 'BUYER', 'QUOTATIONS', 'TRANS', 'AMOUNTS']
# crsr.execute("DELETE FROM AMOUNTS")

for items in tables:
    crsr.execute("DELETE FROM "+ items)

conn.commit()
conn.close()
