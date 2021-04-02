# Import Tkinter Module
from tkinter import *
import sqlite3
from PIL import ImageTk
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
        new_user=Button(Frame_login, text="Register",bg="white",fg="#fc6203", bd=0, font=("Sans Serif",10),command=open).place(x=280, y= 260)
        def check():
            conn=sqlite3.connect('FTMS.db')
            crsr=conn.cursor()
            crsr.execute("SELECT * FROM FARMER WHERE F_ID=:USER_ID",
            {
                'USER_ID':self.txt_user.get()
            })
            c=crsr.fetchall()
            if len(c) != 0:
                if c[0][1]==self.txt_pass.get():
                    top2=Toplevel()
                    obj3=FPortal(top2)
            else:
                crsr.execute("SELECT * FROM BUYER WHERE B_ID=:USER_ID",
                {
                'USER_ID':self.txt_user.get()
                })
                c=crsr.fetchall()
                if c != 0:
                    if c[0][1]==self.txt_pass.get():
                        top2=Toplevel()
                        obj3=BPortal(top2)


            conn.commit()
            conn.close()

        Login_Button=Button(self.root, text="Login",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=check).place(x=640, y= 420)
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
        Frame_register=Frame(self.root, bg="white")
        Frame_register.place(x=170, y=100, height=500, width=700)
        var = IntVar()

        title = Label(Frame_register, text="Register on", font=("Sans Serif",20),fg="black", bg="white").place(x=170, y=30)
        title_2 = Label(Frame_register, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=330, y=30)
        desc = Label(Frame_register, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)

        Farmer = Radiobutton(Frame_register, text="Farmer",variable=var, value=1, bg="white",fg="#fc6203",bd=0, font=("Sans Serif",10)).place(x=100, y= 260)
        
        Buyer=Radiobutton(Frame_register, text="Buyer",variable=var, value=2,bg="white",fg="#fc6203", bd=0, font=("Sans Serif",10)).place(x=280, y= 260)

        Next_Button =Button(self.root, text="Next",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command = lambda: clicked(var.get())).place(x=640, y= 420)
        def clicked(value):
            global top
            top=Toplevel()
            if value==1:
                obj2=Register_F(top)
            else:
                obj2=Register_B(top)
class Register_F:
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

        lbl_name = Label(Frame_login,text="Name",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=340)
        self.txt_name = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_name.place(x=70,y=360, width=250, height=35)

        lbl_location = Label(Frame_login,text="Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=400)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=70,y=430, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=400,y=140, width=250, height=35)

        lbl_crop = Label(Frame_login,text="Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_crop = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_crop.place(x=400,y=220, width=250, height=35)
        def submit():
            conn=sqlite3.connect('FTMS.db')
            crsr=conn.cursor()
            crsr.execute("INSERT INTO FARMER VALUES(:USER_ID,:PWD, :NAME, :LOC ,:CONTACT)",
                {
                    'USER_ID':self.txt_user.get(),
                    'PWD':self.txt_pass.get(),
                    'NAME':self.txt_name.get(),
                    'LOC':self.txt_location.get(),
                    'CONTACT':self.txt_contact.get()
                })
            conn.commit()
            conn.close()
            top.destroy()
            top1.destroy()
        
        Next_Button =Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command = submit).place(x=640, y= 420)
        
class Register_B:
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

        lbl_name = Label(Frame_login,text="Name",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=340)
        self.txt_name = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_name.place(x=70,y=360, width=250, height=35)

        lbl_location = Label(Frame_login,text="Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=400)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=70,y=430, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=400,y=140, width=250, height=35)
        def submit():
            conn=sqlite3.connect('FTMS.db')
            crsr=conn.cursor()
            crsr.execute("INSERT INTO BUYER VALUES(:USER_ID,:PWD, :NAME, :LOC ,:CONTACT)",
                {
                    'USER_ID':self.txt_user.get(),
                    'PWD':self.txt_pass.get(),
                    'NAME':self.txt_name.get(),
                    'LOC':self.txt_location.get(),
                    'CONTACT':self.txt_contact.get()
                })
            conn.commit()
            conn.close()
            top.destroy()
            top1.destroy()
        Next_Button =Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=submit).place(x=640, y= 420)           
class FPortal:
    def __init__(self,root):
        self.root = root
        self.root.title("FARMER PORTAL")
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
class BPortal:
        def __init__(self,root):
            self.root = root
            self.root.title("BUYER PORTAL")
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
        
            Make_quotations = Button(Frame_login,text="Make Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=110)

            show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=190)

            edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=260)

            my_quotations = Button(Frame_login,text="My Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=330)

def open():
    global top1
    top1=Toplevel()
    obj1=Register(top1)
root=Tk()
obj = Login(root)
root.mainloop()


