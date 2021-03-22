# Import Tkinter Module
from tkinter import *

from PIL import ImageTk

# Create Login Class
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("FTMS Login")
        self.root.geometry("1024x640")
        self.root.resizable(False,False)
        
        # Background Image
        self.bg =  ImageTk.PhotoImage(file="Login_img.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1 )
        
        # Login Frames
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=450, y=100, height=340, width=500)
        
        title = Label(Frame_login, text="Welcome to ", font=("Sans Serif",20),fg="black", bg="white").place(x=130, y=30)
        title_2 = Label(Frame_login, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=290, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)

        lbl_user = Label(Frame_login,text="Username",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_user = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_user.place(x=70,y=140, width=350, height=35)


        lbl_pass = Label(Frame_login,text="Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_pass.place(x=70,y=220, width=350, height=35)

        forget=Button(Frame_login, text="Forget Password?",bg="white",fg="#fc6203",bd=0, font=("Sans Serif",10)).place(x=100, y= 260)
        new_user=Button(Frame_login, text="Register",bg="white",fg="#fc6203", bd=0, font=("Sans Serif",10)).place(x=280, y= 260)

        Login_Button=Button(self.root, text="Login",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20)).place(x=640, y= 420)


# Create Tkinter object
root = Tk()

# Make Login object
obj = Login(root)

root.mainloop()