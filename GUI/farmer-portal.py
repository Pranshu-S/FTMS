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
        
        view_quotations = Button(Frame_login,text="View Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=110)

        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=190)

        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=260)

# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()


# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),