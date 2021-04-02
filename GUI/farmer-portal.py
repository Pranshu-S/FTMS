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
        Frame_login.place(x=450, y=100, height=400, width=500)

        title = Label(Frame_login, text="FARMER", font=("Sans Serif",20),fg="black", bg="white").place(x=150, y=30)
        title_2 = Label(Frame_login, text="PORTAL", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=270, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=130, y=70)
        
        view_quotations = Button(Frame_login,text="View Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20).place(x=100, y=170)

        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20).place(x=100, y=220)

        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20).place(x=100, y=270)

# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()


# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),