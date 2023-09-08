from tkinter import*
#""" tkinter : in built class that has widgests for creating dashboard"""
from PIL import Image,ImageTk
#"""pip install pillow, used for gif,jpeg and resize of images"""
from tkinter import ttk
# Window
class supplierClass:
    def __init__(self,root): #default constructor, Object : root
        self.root=root #to initialise the object root of Tk. Self is used for defining the object if the class
        self.root.geometry("1100x500+220+130") #to give dimensions to the running window ("width,height+ top where to start from+gap from bottom)
        self.root.title("I.T.S Inventory Management System | Developed by ITS Students")
        self.root.config(bg="#BCBCEE")
        self.root.focus_force()

        #all variables======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()


        #search
        SearchFrame=LabelFrame(self.root,text="Search the Supplier",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#BCBCEE")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #options
        lbl_search=Label(SearchFrame, text="Search by Invoice Number",bg="#BCBCEE",font=("Times new roman",13))
        lbl_search.place(x=10,y=10)

        # search
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=("goudy old style",13),bg="white").place(x=200,y=10) #entry for single row entry
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",13),bg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #title
        title=Label(self.root,text="Supply Details",font=("goudy old style",13),bg="#7C7CFC").place(x=50,y=100,width=1000)

        #content
        #row 1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=150)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 13), bg="white").place(x=150, y=150,width=180)


        #row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 13), bg="white").place(x=150, y=190, width=180)


        #row 3
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 13), bg="white").place(x=150, y=230, width=180)


        #row 4
        lbl_address = Label(self.root, text="Description", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=270)
        self.txt_desc = Text(self.root, font=("goudy old style", 13), bg="white")
        self.txt_desc.place(x=150,y=270,width=300,height=60)

        #buttons
        btn_add = Button(self.root, text="Save", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=500, y=305, width=100, height=30)
        btn_update = Button(self.root, text="Update", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=620, y=305, width=100, height=30)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=740, y=305, width=100, height=30)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=860, y=305, width=100, height=30)

        #employee details

        supframe=Frame(self.root,bd=3,relief=RIDGE)
        supframe.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(supframe,orient=VERTICAL)
        scrollx = Scrollbar(supframe, orient = HORIZONTAL)

        #treeview
        self.supplierTable=ttk.Treeview(supframe,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) #columns are case sensitive. Should be same as database entries

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice",text="Invoice")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice", width =90)
        self.supplierTable.column("name", width =90)
        self.supplierTable.column("contact", width =90)
        self.supplierTable.column("desc", width =90)
        self.supplierTable.pack(fill=BOTH,expand=1)





if __name__ == "__main__":  # as we are accesing multiple python files, we dont want all files to contradict so we defined file "dashboard" as main()
    root = Tk()  # object : root, Tk : class of tkinter to use the widgets, only by using the object of class Tk  can we use further classes
    obj = supplierClass(root)
    root.mainloop()