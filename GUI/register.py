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
        Frame_register=Frame(self.root, bg="white")
        Frame_register.place(x=170, y=100, height=500, width=700)
        var = IntVar()

        title = Label(Frame_register, text="Register on", font=("Sans Serif",20),fg="black", bg="white").place(x=170, y=30)
        title_2 = Label(Frame_register, text="FTMS ", font=("Sans Serif",20, "bold"),fg="#fc6203", bg="white").place(x=330, y=30)
        desc = Label(Frame_register, text="Farmers Transaction Management System ", font=("Sans Serif",10),fg="grey", bg="white").place(x=115, y=70)

        Farmer = Radiobutton(Frame_register, text="Farmer",variable=var, value=1, bg="white",activebackground="#fc6203", height= 6, width=6, bd=0, font=("Sans Serif",20)).place(x=150, y= 170)
        
        Buyer=Radiobutton(Frame_register, text="Buyer",variable=var, value=2,bg="white",activebackground="#fc6203", bd=0, height= 6, width=6, font=("Sans Serif",20)).place(x=350, y= 170)

        Next_Button =Button(self.root, text="Next",bg="#fc6203",fg="white", bd=0, font=("Sans Serif",20)).place(x=640, y= 500)


# Create Tkinter object
root = Tk()

# Make Login object
obj = Register(root)

root.mainloop()


# Register - Ask if farmer/buyer
# Farmer - USERID, PAss, name, location, contact number,  (if farmer/buyer), Which crops (checklist)
# Buyer - USERID, PAss, name, location, contact number,  (if farmer/buyer),