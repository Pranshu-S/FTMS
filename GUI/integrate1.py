# Import Tkinter Module
from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk
from tkinter import ttk

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
        redirected=0
        if len(c)!= 0:
            if c[0][1]==self.txt_pass.get():
                redirected=1
                ID=self.txt_user.get()
                farmer_portal=FPortal(self.root)
                root.mainloop()

        else:
            crsr.execute("SELECT * FROM BUYER WHERE B_ID=:USER_ID",
            {
            'USER_ID':self.txt_user.get()
            })
            c=crsr.fetchall()
            if len(c)!= 0:
                if c[0][1]==self.txt_pass.get():
                    redirected=1
                    ID=self.txt_user.get()
                    buyer_portal=BPortal(self.root)
                    root.mainloop()
        conn.commit()
        conn.close()
        if(redirected==0):
            self.popupmsg()

    def open(self):
        Register_window=Register(self.root)
        root.mainloop()

    def popupmsg(self):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text="Invalid UserID or Password")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
  
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

        title = Label(Frame_register, text="Register on", font=("Sans Serif",20),fg="black", bg="white").place(x=170, y=30)
        title_2 = Label(Frame_register, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=330, y=30)
        desc = Label(Frame_register, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=150, y=70)

        Farmer = Button(Frame_register, text="Farmer", bg="white",activebackground="#fc6203", height= 6, width=10, bd=0, command = self.goto_farmer, font=("Sans Serif",20)).place(x=100, y= 170)
        
        Buyer = Button(Frame_register, text="Buyer",bg="white",activebackground="#fc6203", bd=0, height= 6, width=10, command=self.goto_buyer, font=("Sans Serif",20)).place(x=400, y= 170)        

    def goto_buyer(self):
        Buyer_Register=Register_B(self.root)

    def goto_farmer(self):
        Farmer_Register=Register_F(self.root)

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
        crop_list = get_crops()

        self.variable = StringVar()
        self.variable.set(crop_list[0])

        self.crops = OptionMenu(Frame_login, self.variable, *crop_list)
        self.crops.config(bg="#ebedf0", bd=0,width=17, font=("Sans Serif",14))
        self.crops.place(x=400, y=220)     
        Next_Button =Button(self.root, text="Register",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command = self.submit).place(x=640, y= 460)
    
    def submit(self):
        self.txt_crop = get_crop_id(self.variable.get())

        IS_AVAILABLE = 1   
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()

        crsr.execute("SELECT * FROM FARMER WHERE F_ID=:USER_ID",
        {
            'USER_ID':self.txt_user.get()
        })
        c=crsr.fetchall()
        if len(c)== 0:
            crsr.execute("SELECT * FROM BUYER WHERE B_ID=:USER_ID",
            {
            'USER_ID':self.txt_user.get()
            })
            c=crsr.fetchall()
            if len(c) != 0:
                IS_AVAILABLE = 0
        else:
            IS_AVAILABLE = 0

        if IS_AVAILABLE:

            if self.txt_pass.get() == self.txt_conf_pass.get():

                if len(self.txt_contact.get())==10:
                    print(self.txt_crop)
                    if self.txt_crop != None:
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
                                'C_ID':int(self.txt_crop)
                            })

                        conn.commit()
                        conn.close()
                        login1 = Login(self.root)
                    else:
                        self.popupmsg("SELECT CROP!")
                else:
                    self.popupmsg("ENTER VALID PHONE NUMBER!")

            else:
                self.popupmsg("PASSWORDS DO NOT MATCH!")
        
        else:
            self.popupmsg("USERID ALREADY EXISTS!")

        conn.commit()
        conn.close()

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop() 

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
        IS_AVAILABLE = 1   
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()

        crsr.execute("SELECT * FROM FARMER WHERE F_ID=:USER_ID",
        {
            'USER_ID':self.txt_user.get()
        })
        c=crsr.fetchall()
        if len(c)== 0:
            crsr.execute("SELECT * FROM BUYER WHERE B_ID=:USER_ID",
            {
            'USER_ID':self.txt_user.get()
            })
            c=crsr.fetchall()
            if len(c) != 0:
                IS_AVAILABLE = 0
        else:
            IS_AVAILABLE = 0

        if IS_AVAILABLE:

            if self.txt_pass.get() == self.txt_conf_pass.get():

                if len(self.txt_contact.get())==10:
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
                    login = Login(self.root)
                else:
                    self.popupmsg("ENTER VALID PHONE NUMBER!")

            else:
                self.popupmsg("PASSWORDS DO NOT MATCH!")
        
        else:
            self.popupmsg("USERID ALREADY EXISTS!")

        conn.commit()
        conn.close()

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop() 

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
        view_quotations = Button(Frame_login,text="View Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open1).place(x=110, y=160)
        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open2).place(x=110, y=210)
        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20,command=self.open3).place(x=110, y=260)
        Logout = Button(Frame_login, text="Logout",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",15),command = self.logout,width=20,).place(x=110, y= 310)

    def open1(self):
        ViewQ=Show_Q(self.root)
    def open2(self):
        ViewH=Show_H(self.root)
    def open3(self):
        EditF=Edit_F(self.root)
    def logout(self):
        login=Login(self.root)

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
        Make_quotations = Button(Frame_login,text="Make Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20, command=self.make).place(x=110, y=140)
        show_history = Button(Frame_login,text="Show History",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0, width=20, command=self.show_history_b).place(x=110, y=180)
        edit_profile = Button(Frame_login,text="Edit Profile",font=("Sans Serif",15),bg="#fc6203",fg="white",width=20, bd=0, command=self.edit_b).place(x=110, y=220)
        my_quotations = Button(Frame_login,text="My Quotations",font=("Sans Serif",15),bg="#fc6203",fg="white", width=20,bd=0, command=self.my_q).place(x=110, y=260)
        Logout = Button(Frame_login,text="Logout",font=("Sans Serif",15),bg="#fc6203",fg="white", width=20,bd=0, command=self.log_out).place(x=110, y=300)

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

    def log_out(self):
        log = Login(self.root)

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

        title = Label(Frame_login, text="All Avialable", font=("Sans Serif",20),fg="black", bg="white").place(x=270, y=30)
        title_2 = Label(Frame_login, text="Quotations ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=440, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=300, y=70)
        
        self.all_quotes = ttk.Treeview(Frame_login)
        self.all_quotes["columns"]=("Crop","Quote", "Timestamp")
        self.all_quotes.column("#0", width=150, minwidth=150)
        self.all_quotes.column("Crop", width=150, minwidth=150)
        self.all_quotes.column("Quote", width=150, minwidth=150)
        self.all_quotes.column("Timestamp", width=340, minwidth=340)
        self.all_quotes.place(x=50,y = 100)

        self.all_quotes.heading("#0",text="Buyer")
        self.all_quotes.heading("Crop", text="Crop")
        self.all_quotes.heading("Quote", text="Quote")
        self.all_quotes.heading("Timestamp", text="Timestamp")

        # self.all_quotes.pack()
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT CROP_ID FROM CROP_GROWN WHERE F_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        cid=crsr.fetchall()

        for crops in cid:
            crsr.execute("SELECT * FROM QUOTATIONS WHERE CROP_ID=:C_ID",
            {
                'C_ID':crops[0]
            })
            list=crsr.fetchall()

        # self.all_quotes = Listbox(Frame_login)

            for item in list:
                self.all_quotes.insert("", 'end', text=item[0], values=(get_crop_name(item[1]),item[2],item[3]))
                
        conn.commit()
        conn.close()
        Contact = Button(Frame_login,text="Contact Buyer and Generate Transaction",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0,command=self.contact).place(x=70, y=450)
        
        lbl_user = Label(Frame_login,text="Quantity",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=400)
        self.quantity_purchased = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.quantity_purchased.place(x=160,y=400, width=350, height=35)
        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", bd=0,command=self.back).place(x=520, y=450)

    def contact(self):
        Selected = self.all_quotes.item(self.all_quotes.focus())

        if len(Selected['text'])==0:
            popupmsg("No Quote Selected!")
        elif len(self.quantity_purchased.get()) ==0:
            popupmsg("ENTER AMOUNT!")
        else:
            conn=sqlite3.connect('FTMS.db')
            crsr=conn.cursor()
            crsr.execute("SELECT * FROM TRANS")
            s=len(crsr.fetchall())
            crsr.execute("SELECT AMT FROM QUOTATIONS WHERE B_ID=:Br_ID AND CROP_ID=:C_ID",
            {
                'Br_ID':Selected['text'],
                'C_ID':Selected['values'][0]
            })
            amt=crsr.fetchall()
            crsr.execute("INSERT INTO TRANS VALUES(:Tr_ID,:Fr_ID,:Br_ID,:C_ID,:dt)",
            {
                'Tr_ID':s+1,
                'Fr_ID':ID,
                'Br_ID':Selected['text'],
                'C_ID':get_crop_id(Selected['values'][0]),
                'dt':datetime.datetime.now()
            })
            Cost = float(self.quantity_purchased.get())*float(Selected['values'][1])
            print(Cost)
            crsr.execute("INSERT INTO AMOUNTS VALUES(:Tr_ID,:AMT,:QT)",
            {
                'Tr_ID':s+1,
                'QT':self.quantity_purchased.get(),
                'AMT':Cost
            })
            crsr.execute("DELETE FROM QUOTATIONS WHERE B_ID=:Br_ID AND CROP_ID=:C_ID",
            {
                'Br_ID':Selected['text'],
                'C_ID':get_crop_id(Selected['values'][0])
            })
            conn.commit()
            conn.close()
            refresh = Show_Q(self.root)

    def back(self):
        back=FPortal(self.root)

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

        title = Label(Frame_login, text="All Transaction", font=("Sans Serif",20),fg="black", bg="white").place(x=280, y=30)
        title_2 = Label(Frame_login, text="History ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=480, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=300, y=70)
        
        self.all_quotes = ttk.Treeview(Frame_login)
        self.all_quotes["columns"]=("B_ID","CROP","Amount", "Timestamp")
        self.all_quotes.column("#0", width=150, minwidth=150)
        self.all_quotes.column("B_ID", width=120, minwidth=120)
        self.all_quotes.column("CROP", width=120, minwidth=120)
        self.all_quotes.column('Amount',width=120, minwidth=120)
        self.all_quotes.column("Timestamp", width=300, minwidth=300)
        self.all_quotes.place(x=50,y = 100)

        self.all_quotes.heading("#0",text="TRANSACTION ID")
        self.all_quotes.heading("B_ID", text="BUYER ID")
        self.all_quotes.heading("CROP", text="CROP")
        self.all_quotes.heading("Amount",text="AMOUNT")
        self.all_quotes.heading("Timestamp", text="Timestamp")

        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT * FROM TRANS WHERE F_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        list_trans=crsr.fetchall()

        crsr.execute("SELECT T_ID FROM TRANS WHERE F_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        all_id = crsr.fetchall()

        all_id2 = []

        for ids in all_id:
            all_id2.append(ids[0])
        
        amt = []

        for ids in all_id2:  
            crsr.execute("SELECT AMT FROM AMOUNTS WHERE T_ID=:TID",
            {
                'TID':ids
            })
            quote_ret=crsr.fetchall()
            amt.append(quote_ret)

        conn.commit()
        conn.close()
        # self.all_quotes = Listbox(Frame_login)

        final_amt = []

        for costs in amt:
            final_amt.append(costs[0][0])        # final_amt.append(costs[0][1])

        print(final_amt)

        i = 0
        for item in list_trans:
            self.all_quotes.insert("", 'end', text=item[0], values=(item[2],get_crop_name(item[3]),final_amt[i], item[4]))
            i = i + 1

        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", width=10, bd=0,command=self.back).place(x=350, y=450)

    def back(self):
        back=FPortal(self.root)    

class Edit_F:
    global ID
    def __init__(self,root):

        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor() 
        crsr.execute("SELECT * FROM FARMER WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID               
            })
        details = crsr.fetchall()

        self.PWD = details[0][1]
        self.LOCATION = details[0][3]
        self.CONTACT = details[0][4]
        
        crsr.execute("SELECT * FROM CROP_GROWN WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID               
            })
        details = crsr.fetchall()   

        self.CROP = details[0][1]

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

        old_pass = StringVar(value=self.PWD)
        lbl_pass = Label(Frame_login,text="Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*", textvariable=old_pass)
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        old_pass1 = StringVar(value=self.PWD)
        conf_lbl_pass = Label(Frame_login,text="Confirm Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=260)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0",show="*", textvariable=old_pass1)
        self.txt_conf_pass.place(x=70,y=290, width=250, height=35)

        old_location = StringVar(value=self.LOCATION)
        lbl_location = Label(Frame_login,text="Change Location", font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10), textvariable = old_location,bg="#ebedf0")
        self.txt_location.place(x=400,y=140, width=250, height=35)

        old_contact = StringVar(value=self.CONTACT)
        lbl_contact = Label(Frame_login,text="Change Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0",textvariable= old_contact )
        self.txt_contact.place(x=70,y=140, width=250, height=35)

        lbl_crop = Label(Frame_login,text="Add Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        crop_list = get_crops()

        crsr.execute("SELECT CROP_ID FROM CROP_GROWN WHERE F_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        cid=crsr.fetchall()

        conn.commit()
        conn.close()

        avail_crops = []

        for crops in cid:
            avail_crops.append(crops[0])

        for crops in avail_crops:
            crop_list.remove(get_crop_name(crops))

        self.variable = StringVar()
        self.variable.set(crop_list[0])

        self.crops = OptionMenu(Frame_login, self.variable, *crop_list)
        self.crops.config(bg="#ebedf0", bd=0,width=17, font=("Sans Serif",14))
        self.crops.place(x=400, y=220) 

        Save =Button(self.root, text="Save",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.save).place(x=400, y= 500)
        Back =Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.back).place(x=640, y= 500)
   
    def back(self):
        back=FPortal(self.root)
    
    def save(self):
        global ID
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor() 

        if self.txt_conf_pass.get() == self.txt_pass.get():
            crsr.execute("UPDATE FARMER SET PWD = :PWD WHERE F_ID = :USER_ID",
                {
                    'USER_ID':ID,
                    'PWD':self.txt_pass.get()
                })
        else:
            self.popupmsg("PASSWORDS DO NOT MATCH!")


        crsr.execute("UPDATE FARMER SET LOCATION = :LOC WHERE F_ID = :USER_ID",
            {
                'USER_ID':ID,
                'LOC':self.txt_location.get()
                
            })
        
        if len(self.txt_contact.get())==10:
            crsr.execute("UPDATE FARMER SET CONTACT = :con WHERE F_ID = :USER_ID",
                {
                    'USER_ID':ID,
                    'con':self.txt_contact.get()
                    
                })
        else:
            self.popupmsg("INVALID CONTACT NUMBER!")

        if self.variable.get() != 'Select':

            crsr.execute("INSERT INTO CROP_GROWN VALUES(:F_ID,:CROP_ID)",
                {
                    'F_ID':ID,
                    'CROP_ID':get_crop_id(self.variable.get())
                })
        else:
            popupmsg("ENTER VALID CROP")
        
        conn.commit()
        conn.close()
        back=FPortal(self.root)

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop() 

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
        
        title = Label(Frame_login, text="Add ", font=("Sans Serif",20),fg="black", bg="white").place(x=150, y=30)
        title_2 = Label(Frame_login, text="Quotations ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=210, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)

        lbl_crop = Label(Frame_login,text="Crop",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)

        crop_list = get_crops()

        self.variable = StringVar()
        self.variable.set(crop_list[0])

        self.crops = OptionMenu(Frame_login, self.variable, *crop_list)
        self.crops.config(bg="#ebedf0", bd=0,width=26, font=("Sans Serif",14))
        self.crops.place(x=70, y=140) 

        lbl_price = Label(Frame_login,text="Quote (Rs/kg)",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_price = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0")
        self.txt_price.place(x=70,y=220, width=350, height=35)

        Submit_Button=Button(self.root, text="Submit",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.submit).place(x=680, y= 420)
        Back_Button=Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20),command=self.back).place(x=550, y= 420)
    def back(self):
        back=BPortal(self.root)
    def submit(self):
        global ID

        if self.variable.get() == 'Select':
            popupmsg("SELECT CROP")
        else:
            self.txt_crop = get_crop_id(self.variable.get())
            dt=datetime.datetime.now()
            conn=sqlite3.connect('FTMS.db')
            crsr=conn.cursor()
            print(self.txt_crop)
            crsr.execute("INSERT INTO QUOTATIONS VALUES(:USER_ID,:C_ID,:AMT,:DT)",
                {
                    'USER_ID':ID,
                    'C_ID':self.txt_crop,
                    'AMT':self.txt_price.get(),
                    'DT':dt
                })
            conn.commit()
            conn.close()
            popupmsg("QUOTE ADDED!")

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

        title = Label(Frame_login, text="My", font=("Sans Serif",20),fg="black", bg="white").place(x=350, y=30)
        title_2 = Label(Frame_login, text="Quotations ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=400, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=300, y=70)
        
        self.all_quotes = ttk.Treeview(Frame_login)
        self.all_quotes["columns"]=("Crop","Quote", "Timestamp")
        self.all_quotes.column("#0", width=150, minwidth=150)
        self.all_quotes.column("Crop", width=150, minwidth=150)
        self.all_quotes.column("Quote", width=150, minwidth=150)
        self.all_quotes.column("Timestamp", width=340, minwidth=340)
        self.all_quotes.place(x=50,y = 100)

        self.all_quotes.heading("#0",text="Buyer")
        self.all_quotes.heading("Crop", text="Crop")
        self.all_quotes.heading("Quote", text="Quote")
        self.all_quotes.heading("Timestamp", text="Timestamp")

        # self.all_quotes.pack()
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT * FROM QUOTATIONS WHERE B_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        list=crsr.fetchall()
        conn.commit()
        conn.close()
        # self.all_quotes = Listbox(Frame_login)

        for item in list:
            self.all_quotes.insert("", 'end', text=item[0], values=(get_crop_name(item[1]),item[2],item[3]))
                
        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", width=15, bd=0,command=self.back).place(x=300, y=450)

    def back(self):
        goback = BPortal(self.root)

class Edit_B:
    def __init__(self,root):
        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor() 
        crsr.execute("SELECT * FROM BUYER WHERE B_ID = :USER_ID",
            {
                'USER_ID':ID               
            })
        details = crsr.fetchall()

        self.PWD = details[0][1]
        self.LOCATION = details[0][3]
        self.CONTACT = details[0][4] 

        conn.commit()
        conn.close()

        self.root = root
        self.root.title("Edit Buyer Profile")
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

        old_pass = StringVar(value=self.PWD)
        lbl_pass = Label(Frame_login,text="Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=190)
        self.txt_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0", show="*", textvariable=old_pass)
        self.txt_pass.place(x=70,y=220, width=250, height=35)

        old_pass1 = StringVar(value=self.PWD)
        conf_lbl_pass = Label(Frame_login,text="Confirm Change Password",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=190)
        self.txt_conf_pass = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0",show="*", textvariable=old_pass1)
        self.txt_conf_pass.place(x=400,y=220, width=250, height=35)

        old_location = StringVar(value=self.LOCATION)
        lbl_location = Label(Frame_login,text="Change Location", font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=400, y=110)
        self.txt_location = Entry(Frame_login, font=("Sans Serif",10), textvariable = old_location,bg="#ebedf0")
        self.txt_location.place(x=400,y=140, width=250, height=35)

        old_contact = StringVar(value=self.CONTACT)
        lbl_contact = Label(Frame_login,text="Change Contact Number",font=("Sans Serif",15),fg="#fc6203", bg="white").place(x=70, y=110)
        self.txt_contact = Entry(Frame_login, font=("Sans Serif",10),bg="#ebedf0",textvariable= old_contact )
        self.txt_contact.place(x=70,y=140, width=250, height=35)

        Save =Button(self.root, text="Save",bg="#fc6203",fg="white", bd=0, width=15, command=self.save_details, font=("Sans Serif",15)).place(x=400, y= 420)
        Back =Button(self.root, text="Back",bg="#fc6203",fg="white", bd=0, width=15, command=self.goback, font=("Sans Serif",15)).place(x=400, y= 460)
    
    def save_details(self):
        global ID

        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor() 

        if self.txt_conf_pass.get() == self.txt_pass.get():
            crsr.execute("UPDATE BUYER SET PWD = :PWD WHERE B_ID = :USER_ID",
                {
                    'USER_ID':ID,
                    'PWD':self.txt_pass.get()
                })
        else:
            popupmsg("PASSWORDS DO NOT MATCH!")


        crsr.execute("UPDATE BUYER SET LOCATION = :LOC WHERE B_ID = :USER_ID",
            {
                'USER_ID':ID,
                'LOC':self.txt_location.get()
                
            })
        
        if len(self.txt_contact.get())==10:
            crsr.execute("UPDATE BUYER SET CONTACT = :con WHERE B_ID = :USER_ID",
                {
                    'USER_ID':ID,
                    'con':self.txt_contact.get()
                    
                })
        else:
            popupmsg("INVALID CONTACT NUMBER!")
        
        conn.commit()
        conn.close()
        back=BPortal(self.root)

    def goback(self):
        back =BPortal(self.root)

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

        title = Label(Frame_login, text="All Transaction", font=("Sans Serif",20),fg="black", bg="white").place(x=280, y=30)
        title_2 = Label(Frame_login, text="History ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=480, y=30)
        desc = Label(Frame_login, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=300, y=70)
        
        self.all_quotes = ttk.Treeview(Frame_login)
        self.all_quotes["columns"]=("B_ID","CROP","Amount", "Timestamp")
        self.all_quotes.column("#0", width=150, minwidth=150)
        self.all_quotes.column("B_ID", width=120, minwidth=120)
        self.all_quotes.column("CROP", width=120, minwidth=120)
        self.all_quotes.column('Amount',width=120, minwidth=120)
        self.all_quotes.column("Timestamp", width=300, minwidth=300)
        self.all_quotes.place(x=50,y = 100)

        self.all_quotes.heading("#0",text="TRANSACTION ID")
        self.all_quotes.heading("B_ID", text="BUYER ID")
        self.all_quotes.heading("CROP", text="CROP")
        self.all_quotes.heading("Amount",text="AMOUNT")
        self.all_quotes.heading("Timestamp", text="Timestamp")

        conn=sqlite3.connect('FTMS.db')
        crsr=conn.cursor()
        crsr.execute("SELECT * FROM TRANS WHERE B_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        list_trans=crsr.fetchall()

        crsr.execute("SELECT T_ID FROM TRANS WHERE B_ID=:USER_ID",
        {
            'USER_ID':ID
        })
        all_id = crsr.fetchall()

        all_id2 = []

        for ids in all_id:
            all_id2.append(ids[0])
        
        amt = []

        for ids in all_id2:  
            crsr.execute("SELECT AMT FROM AMOUNTS WHERE T_ID=:TID",
            {
                'TID':ids
            })
            quote_ret=crsr.fetchall()
            amt.append(quote_ret)

        conn.commit()
        conn.close()
        # self.all_quotes = Listbox(Frame_login)

        final_amt = []

        for costs in amt:
            final_amt.append(costs[0][0])        # final_amt.append(costs[0][1])

        print(final_amt)

        i = 0
        for item in list_trans:
            self.all_quotes.insert("", 'end', text=item[0], values=(item[1],get_crop_name(item[3]),final_amt[i], item[4]))
            i = i + 1

        Back = Button(Frame_login,text="Back",font=("Sans Serif",15),bg="#fc6203",fg="white", width=10, bd=0,command=self.back).place(x=350, y=450)

    def back(self):
        back=BPortal(self.root)    

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop() 

def get_crop_id(crop_name):
    conn=sqlite3.connect('FTMS.db')
    crsr=conn.cursor()

    crsr.execute("SELECT * FROM CROP")

    list_crops =crsr.fetchall()

    for crops in list_crops:
        if crop_name == crops[1]:
            conn.commit()
            conn.close()
            return crops[0]

def get_crop_name(crop_id):
    conn=sqlite3.connect('FTMS.db')
    crsr=conn.cursor()

    crsr.execute("SELECT * FROM CROP")

    list_crops =crsr.fetchall()
    
    for crops in list_crops:
        if crop_id == crops[0]:
            conn.commit()
            conn.close()
            return crops[1]

def get_crops():

    conn=sqlite3.connect('FTMS.db')
    crsr=conn.cursor()

    crsr.execute("SELECT * FROM CROP")

    list_crops =crsr.fetchall()

    OptionList = ['Select']

    for crops in list_crops:
        OptionList.append(crops[1])

    return OptionList

global root
root=Tk()
obj = Login(root)
root.mainloop()