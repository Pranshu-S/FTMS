# Import Tkinter Module
from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk
from tkinter import ttk

conn=sqlite3.connect('FTMS.db')
crsr=conn.cursor()

crsr.execute("SELECT * FROM CROP")

c=crsr.fetchall()

print(c)

x = 'Rice'
n = -1

for crops in c:
    if x == crops[1]:
        n = crops[0]
        break
print(n)


x = 3

for crops in c:
    if x == crops[0]:
        n = crops[1]
        break

print(n)

conn.commit()
conn.close()

OptionList = []

for crops in c:
    OptionList.append(crops[1])

app = Tk()

app.geometry('100x200')

variable = StringVar(app)
variable.set(OptionList[0])

opt = OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()