from tkinter import*
#""" tkinter : in built class that has widgests for creating dashboard"""
from PIL import Image,ImageTk
#"""pip install pillow, used for gif,jpeg and resize of images"""
from Employee import employeeClass
from Supplier import supplierClass
from Category import categoryClass
from Product import productClass

# Window
class dash:
    def __init__(self,root): #default constructor, Object : root
        self.root=root #to initialise the object root of Tk. Self is used for defining the object if the class
        self.root.geometry("1350x700+0+0") #to give dimensions to the running window ("width,height+ top where to start from+gap from bottom)
        self.root.title("I.T.S Inventory Management System | Developed by ITS Students")
        self.root.config(bg="#BCBCEE")

        #Title
        self.icon_title= PhotoImage(file="C:\Major Project\Icon2.png")
        title= Label(self.root, text = "Inventory Management System",image=self.icon_title,compound = LEFT, font = ("Orator Std",40,"bold"),bg="#7F7FFF",fg="White",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # root= is the frame. Label is a type of class in tkinter for giving tkinter that gives tools similar to html websiter dev. .place is

        #Logout Button
        btn_logout=Button(self.root,text="Logout",font=("Orator Std",15,"bold"),bg="#52528B",cursor="hand2").place(x=1170,y=10,height=50,width=150)

        #Time
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date : DD-MM-YYYY\t\t  Time: HH: MM : SS",font=("Orator Std", 15), bg="#000000", fg="White")
        self.lbl_clock.place(x=0, y=70,relwidth=1,height=30)

        #Left Menu : need to make frames
        self.menulogo=Image.open("C:\Major Project\menuicon3.png")
        self.menulogo.resize((100,100),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        lmenu=Frame(self.root,bd=2,relief=RIDGE,bg="#9797FF")
        #Relief : Border Style
        lmenu.place(x=0,y=117,width=260,height=510)

        lblmenu=Label(lmenu,image=self.menulogo)
        lblmenu.pack(side=TOP,fill=X)
        lblmenu = Label(lmenu, text="Menu", font=("Orator Std", 20, "bold"), bg="#52528B").pack(side=TOP,fill=X)

        #Menu buttons
        btnemp = Button(lmenu, text="Employee", command =self.employee,font=("Orator Std", 20, "bold"), bg="#9797FF",bd=2, cursor ="hand2").pack(side=TOP, fill=X)
        btnsup = Button(lmenu, text="Supplier",command =self.supplier,font=("Orator Std", 20, "bold"), bg="#9797FF", bd=2,cursor="hand2").pack(side=TOP, fill=X)
        btncat = Button(lmenu, text="Category",command =self.category, font=("Orator Std", 20, "bold"), bg="#9797FF", bd=2,cursor="hand2").pack(side=TOP, fill=X)
        btnpro = Button(lmenu, text="Product", command=self.product,font=("Orator Std", 20, "bold"), bg="#9797FF", bd=2,cursor="hand2").pack(side=TOP, fill=X)
        btnsal = Button(lmenu, text="Sales", font=("Orator Std", 20, "bold"), bg="#9797FF", bd=2,cursor="hand2").pack(side=TOP, fill=X)
        btnext = Button(lmenu, text="Exit", font=("Orator Std", 20, "bold"), bg="#9797FF", bd=2,cursor="hand2").pack(side=TOP, fill=X)

        # Footer
        lbl_foot = Label(self.root,text="Inventory Management System | Developed by I.T.S. Students\nFor any Technichal Issue Contact : 123456789", font=("Orator Std", 12), bg="#000000", fg="White").pack(side=BOTTOM,fill=X)

        #content boxes
        self.lblemp=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#7C7CFC",fg="white",font=("goudy old style",20,"bold"))
        self.lblemp.place(x=300,y=120,height=150,width=300)

        self.lblsup = Label(self.root, text="Supply\n[0]", bd=5, relief=RIDGE, bg="#7C7CFC", fg="white",font=("goudy old style", 20, "bold"))
        self.lblsup.place(x=650, y=120, height=150, width=300)

        self.lblcat = Label(self.root, text="Category\n[0]", bd=5, relief=RIDGE, bg="#7C7CFC", fg="white",font=("goudy old style", 20, "bold"))
        self.lblcat.place(x=1000, y=120, height=150, width=300)

        self.lblpro = Label(self.root, text="Product\n[0]", bd=5, relief=RIDGE, bg="#7C7CFC", fg="white",font=("goudy old style", 20, "bold"))
        self.lblpro.place(x=300, y=300, height=150, width=300)

        self.lblsal = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#7C7CFC", fg="white",font=("goudy old style", 20, "bold"))
        self.lblsal.place(x=650, y=300, height=150, width=300)

    def employee(self):
        self.new_win=Toplevel(self.root) #so that a new window opens when we click "employee" button
        self.new_obj= employeeClass(self.new_win) #object for the employee class in employee.py

    def supplier(self):
        self.new_win=Toplevel(self.root) #so that a new window opens when we click "employee" button
        self.new_obj= supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root) #so that a new window opens when we click "employee" button
        self.new_obj= categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root) #so that a new window opens when we click "employee" button
        self.new_obj= productClass(self.new_win)



if __name__=="__main__": # as we are accesing multiple python files, we dont want all files to contradict so we defined file "dashboard" as main()
    root = Tk() # object : root, Tk : class of tkinter to use the widgets, only by using the object of class Tk  can we use further classes
    obj=dash(root)
    root.mainloop()



