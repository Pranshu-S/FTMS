# Import Tkinter Module
from tkinter import *

from PIL import ImageTk

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
        
        self.all_quotes = Listbox(Frame_login,bg="white",fg="#fc6203", bd=0,height=14,width=100)
        self.all_quotes.place(x=50,y = 100)
        # self.all_quotes.pack()


        print(type(self.all_quotes))
        # self.all_quotes = Listbox(Frame_login)
        my_list = [100,200,300,400,500]

        for item in my_list:
            self.all_quotes.insert(END, item)

        More_Details = Button(Frame_login,text="Show Details",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, command = self.select).place(x=70, y=400)

        Contact = Button(Frame_login,text="Contact",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=450)

        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=500)

        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)

    def select(self):
        self.display_label.config(text=self.all_quotes.get(ANCHOR))

# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()

# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),