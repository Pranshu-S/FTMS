# Import Tkinter Module
from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk
ID='a'
class Login:
    global ID
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
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*")
        self.txt_pass.place(x=70,y=220, width=350, height=35)

        new_user=Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.open).place(x=550, y= 420)
        Login_Button=Button(self.root, text="Login",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.check).place(x=750, y= 420)

    def check(self):
        global ID
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT * FROM FARMER WHERE F_ID=:USER_ID",
        {
            'USER_ID':self.txt_user.get()
        })
        c=crsr.fetchall()
        if len(c) != 0:
            if c[0][1]==self.txt_pass.get():
                ID=self.txt_user.get()
                farmer_portal=FPortal(self.root)
                root.mainloop()

        else:
            crsr.execute("SELECT * FROM BUYER WHERE B_ID=:USER_ID",
            {
            'USER_ID':self.txt_user.get()
            })
            c=crsr.fetchall()
            if c != 0:
                if c[0][1]==self.txt_pass.get():
                    ID=self.txt_user.get()
                    buyer_portal=BPortal(self.root)
                    root.mainloop()

        conn.commit()
        conn.close()

    def open(self):
        Register_window=Register(self.root)
        root.mainloop()
  
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
        desc = Label(Frame_register, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=150, y=70)

        Farmer = Radiobutton(Frame_register, text="Farmer",variable=var, value=1, bg="white",activebackground="#fc6203", height= 6, width=10, bd=0, font=("Sans Serif",20)).place(x=100, y= 170)
        
        Buyer=Radiobutton(Frame_register, text="Buyer",variable=var, value=2,bg="white",activebackground="#fc6203", bd=0, height= 6, width=10, font=("Sans Serif",20)).place(x=400, y= 170)

        Next_Button =Button(self.root, text="Next",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command = lambda: self.clicked(var.get())).place(x=640, y= 500)
        
    def clicked(self, value):
        if value==1:
            Farmer_Register=Register_F(self.root)
        else:
            Buyer_Register=Register_B(self.root)

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

        title = Label(Frame_login, text="FARMER", font=("Sans Serif",20),fg="black", bg="white").place(x=180, y=30)
        title_2 = Label(Frame_login, text="REGISTERATION ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=310, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=200, y=70)
        
        lbl_user = Label(Frame_login,text="Username",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_user = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_user.place(x=70,y=140, width=250, height=35)

        lbl_pass = Label(Frame_login,text="Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*")
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        conf_lbl_pass = Label(Frame_login,text="Confirm Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=270)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0",show="*")
        self.txt_conf_pass.place(x=70,y=300, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=350)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=70,y=380, width=250, height=35)

        lbl_location = Label(Frame_login,text="Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=270)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=400,y=300, width=250, height=35)

        lbl_name = Label(Frame_login,text="Name",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_name = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_name.place(x=400,y=140, width=250, height=35)

        lbl_crop = Label(Frame_login,text="Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_crop = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_crop.place(x=400,y=220, width=250, height=35)
        
        Next_Button =Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command = self.submit).place(x=640, y= 460)
    
    def submit(self):
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
        crsr.execute("INSERT INTO CROP_GROWN VALUES(:USER_ID,:C_ID)",
            {
                'USER_ID':self.txt_user.get(),
                'C_ID':int(self.txt_crop.get())
            })

        conn.commit()
        conn.close()
        login1 = Login(self.root)

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

        title = Label(Frame_login, text="BUYER", font=("Sans Serif",20),fg="black", bg="white").place(x=180, y=30)
        title_2 = Label(Frame_login, text="REGISTERATION ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=310, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=200, y=70)
        
        lbl_user = Label(Frame_login,text="Username",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_user = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_user.place(x=70,y=140, width=250, height=35)

        lbl_pass = Label(Frame_login,text="Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*")
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        conf_lbl_pass = Label(Frame_login,text="Confirm Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=260)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*")
        self.txt_conf_pass.place(x=70,y=290, width=250, height=35)

        lbl_location = Label(Frame_login,text="Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=260)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=400,y=290, width=250, height=35)

        lbl_name = Label(Frame_login,text="Name",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_name = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_name.place(x=400,y=140, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=400,y=220, width=250, height=35)
        
        Next_Button =Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.submit).place(x=450, y= 480)           

    def submit(self):
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
        buyer_portal = BPortal(self.root)

class FPortal:
    def __init__(self,root):
        self.root = root
        self.root.title("Farmer Portal")
        self.root.geometry("1024x640")
        self.root.resizable(False,False)
        
        self.bg =  ImageTk.PhotoImage(file="Login_img.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1 )
        
        # Login Frames
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=450, y=100, height=400, width=500)

        title = Label(Frame_login, text="FARMER", font=("Sans Serif",20),fg="black", bg="white").place(x=150, y=30)
        title_2 = Label(Frame_login, text="PORTAL", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=270, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=130, y=70)
        view_quotations = Button(Frame_login,text="View Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open1).place(x=100, y=170)
        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open2).place(x=100, y=220)
        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open3).place(x=100, y=270)
    def open1(self):
        ViewQ=Show_Q(self.root)
    def open2(self):
        ViewH=Show_H(self.root)
    def open3(self):
        EditF=Edit_F(self.root)

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
        Frame_login.place(x=450, y=100, height=400, width=500)

        title = Label(Frame_login, text="BUYER", font=("Sans Serif",20),fg="black", bg="white").place(x=160, y=30)
        title_2 = Label(Frame_login, text="PORTAL", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=260, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=130, y=70) 
        Make_quotations = Button(Frame_login,text="Make Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20, command=self.make).place(x=110, y=120)
        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20).place(x=110, y=180)
        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white",width=20, bd=0, command=self.edit_b).place(x=110, y=240)
        my_quotations = Button(Frame_login,text="My Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", width=20,bd=0, command=self.my_q).place(x=110, y=300)

    def make(self):
        Make_quote = Make_Q(self.root)
        root.mainloop()

    def my_q(self):
        My_quotation = My_Q(self.root)

    def edit_b(self):
        edit_buyer = Edit_B(self.root)
        root.mainloop()

    def show_history_b(self):
        hist = Show_H_B(self.root)

class Show_Q:
    global ID
    def __init__(self,root):

        self.root = root
        self.root.title("Quotations")
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
        global S
        print(ID)
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT CROP_ID FROM CROP_GROWN WHERE F_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        cid=crsr.fetchall()
        
        print(cid)
        crsr.execute("SELECT * FROM QUOTATIONS WHERE CROP_ID=:C_ID",
        {
            'C_ID':cid[0][0]
        })
        list=crsr.fetchall()
        print(type(self.all_quotes))
        # self.all_quotes = Listbox(Frame_login)

        for item in list:
            self.all_quotes.insert(END, item)

        More_Details = Button(Frame_login,text="Show Details",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, command = self.select).place(x=70, y=400)

        Contact = Button(Frame_login,text="Contact",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=450)

        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0,command=self.back).place(x=70, y=500)
        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)
    def back(self):
        back=FPortal(self.root)
    def select(self):
        self.display_label.config(text=self.all_quotes.get(ANCHOR))

class Show_H:
    def __init__(self,root):

        self.root = root
        self.root.title("History")
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
        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0,command=self.back).place(x=70, y=500)
        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)
    def back(self):
        back=FPortal(self.root)    
    def select(self):
        self.display_label.config(text=self.all_quotes.get(ANCHOR))

class Edit_F:
    global ID
    def __init__(self,root):
        self.root = root
        self.root.title("Edit Farmer Profile")
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

        lbl_pass = Label(Frame_login,text="Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        conf_lbl_pass = Label(Frame_login,text="Confirm Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=260)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_conf_pass.place(x=70,y=290, width=250, height=35)

        lbl_location = Label(Frame_login,text="Change Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=400,y=140, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Change Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=70,y=140, width=250, height=35)

        lbl_crop = Label(Frame_login,text="Change Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_crop = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_crop.place(x=400,y=220, width=250, height=35)

        Save =Button(self.root, text="Save",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.save).place(x=640, y= 420)
        Back =Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.back).place(x=640, y= 500)
    def back(self):
        back=FPortal(self.root)
    def save(self):
        global ID
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor() 
        crsr.execute("UPDATE FARMER SET PWD = :PWD WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID,
                'PWD':self.txt_pass.get()
                
            })
        crsr.execute("UPDATE FARMER SET LOCATION = :LOC WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID,
                'LOC':self.txt_location.get()
                
            })
        crsr.execute("UPDATE FARMER SET CONTACT = :con WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID,
                'con':self.txt_contact.get()
                
            })
        crsr.execute("  UPDATE CROP_GROWN SET CROP_ID = :C_ID WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID,
                'C_ID':int(self.txt_crop.get())
            })
        conn.commit()
        conn.close()

class Make_Q:
    global ID
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

        lbl_crop = Label(Frame_login,text="Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_crop = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_crop.place(x=70,y=140, width=350, height=35)


        lbl_price = Label(Frame_login,text="Quote (Rs/kg)",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_price = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_price.place(x=70,y=220, width=350, height=35)

        Submit_Button=Button(self.root, text="Submit",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.submit).place(x=680, y= 420)
        Back_Button=Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.back).place(x=550, y= 420)
    def back(self):
        back=BPortal(self.root)
    def submit(self):
        global ID
        dt=datetime.datetime.now()
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("INSERT INTO QUOTATIONS VALUES(:USER_ID,:C_ID,:AMT,:DT)",
            {
                'USER_ID':ID,
                'C_ID':int(self.txt_crop.get()),
                'AMT':self.txt_price.get(),
                'DT':dt
            })
        conn.commit()
        conn.close()

class My_Q:
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
        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=500)

        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)

    def select(self):
        self.display_label.config(text=self.all_quotes.get(ANCHOR))

class Edit_B:
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
        

        lbl_pass = Label(Frame_login,text="Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        conf_lbl_pass = Label(Frame_login,text="Confirm Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_conf_pass.place(x=400,y=220, width=250, height=35)

        lbl_location = Label(Frame_login,text="Change Location",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_location.place(x=400,y=140, width=250, height=35)

        lbl_contact = Label(Frame_login,text="Change Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_contact.place(x=70,y=140, width=250, height=35)

        Save =Button(self.root, text="Save",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20)).place(x=640, y= 420)
        Back =Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20)).place(x=640, y= 500)

class Show_H_B:
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
        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0).place(x=70, y=500)

        self.display_label = Label(Frame_login,text='')
        self.display_label.place(x=400, y=400)

    def select(self):
        self.display_label.config(text=self.all_quotes.get(ANCHOR))


global root
root=Tk()
obj = Login(root)
root.mainloop()


