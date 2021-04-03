# Import Tkinter Module
from tkinter import *
from PIL import ImageTk
from tkinter import ttk

# Create Login Class
class Register:
    def __init__(self,root):

        self.root = root
        self.root.title("Register User")
        self.root.geometry("1024x640")
        self.root.resizable(False,False)
        
        # Background Image
        self.bg =  ImageTk.PhotoImage(file="Login_img.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1 )
        
        # Login Frames
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=50, y=50, height=550, width=900)

        title = Label(Frame_login, text="Register on", font=("Sans Serif",20),fg="black", bg="white").place(x=170, y=30)
        title_2 = Label(Frame_login, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=330, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)
        
        self.all_quotes = ttk.Treeview(Frame_login)
        self.all_quotes["columns"]=("Quote","Timestamp")
        self.all_quotes.column("#0", width=270, minwidth=270)
        self.all_quotes.column("Quote", width=150, minwidth=150)
        self.all_quotes.column("Timestamp", width=400, minwidth=200)
        self.all_quotes.place(x=50,y = 100)


        self.all_quotes.heading("#0",text="Buyer")
        self.all_quotes.heading("Quote", text="Quote")
        self.all_quotes.heading("Timestamp", text="Timestamp")
        # self.all_quotes.pack()

        self.all_quotes.insert("", 'end', buyer="a123", values=("12","23-Jun-17 11:25"))

        More_Details = Button(Frame_login,text="Show Details",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, command = self.select).place(x=70, y=400)

        Contact = Button(Frame_login,text="Contact",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=450)

        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=500)

        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)

    def select(self):
        X = self.all_quotes.item(self.all_quotes.focus())
        print(X)
        print(X['text'])
        print(X['values'][0])

# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()

# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),