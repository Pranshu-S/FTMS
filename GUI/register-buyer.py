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
        Frame_login.place(x=170, y=100, height=500, width=700)

        title = Label(Frame_login, text="Register on", font=("Sans Serif",20),fg="black", bg="white").place(x=170, y=30)
        title_2 = Label(Frame_login, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=330, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)
        
        lbl_user = Label(Frame_login,text="Username",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_user = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_user.place(x=70,y=140, width=250, height=35)

        lbl_pass = Label(Frame_login,text="Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        conf_lbl_pass = Label(Frame_login,text="Confirm Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=260)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_conf_pass.place(x=70,y=290, width=250, height=35)

        lbl_location = Label(Frame_login,text="Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=260)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=400,y=290, width=250, height=35)

        lbl_name = Label(Frame_login,text="Name",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_head = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_head.place(x=400,y=140, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=400,y=220, width=250, height=35)

        Next_Button =Button(self.root, text="Next",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20)).place(x=640, y= 420)


# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()


# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),