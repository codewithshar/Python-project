from tkinter import*
""" tkinter : in built class that has widgests for creating dashboard"""
from PIL import Image,ImageTk
"""pip install pillow, used for gif,jpeg and resize of images"""
from tkinter import ttk
# Window
class employeeClass:
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
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_password = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()


        #search
        SearchFrame=LabelFrame(self.root,text="Search the Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#BCBCEE")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("Times new roman",13))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=("goudy old style",13),bg="white").place(x=200,y=10) #entry for single row entry

        #search button
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",13),bg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #title
        title=Label(self.root,text="Employee Details",font=("goudy old style",13),bg="#7C7CFC").place(x=50,y=100,width=1000)

        #content
        #row 1
        lbl_empid = Label(self.root, text="Emp. ID", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 13), bg="#BCBCEE").place(x=400, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 13), bg="#BCBCEE").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 13), bg="white").place(x=150, y=150,width=180)
        #txt_gender = Entry(self.root, textvariable=self.var_gender, font=("goudy old style", 13), bg="white").place(x=500, y=150,width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Gender", "Male", "Female", "Other"), state='readonly', justify=CENTER,font=("Times new roman", 13))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 13), bg="white").place(x=850, y=150,width=180)

        #row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 13), bg="#BCBCEE").place(x=400, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("goudy old style", 13), bg="#BCBCEE").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 13), bg="white").place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 13), bg="white").place(x=500, y=190,width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 13), bg="white").place(x=850, y=190, width=180)

        #row 3
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=230)
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 13), bg="#BCBCEE").place(x=400, y=230)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 13), bg="#BCBCEE").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 13), bg="white").place(x=150, y=230, width=180)
        txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 13), bg="white").place(x=500, y=230,width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select","Admin","Employee"),state='readonly', justify=CENTER, font=("Times new roman", 13))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        #row 4
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 13), bg="#BCBCEE").place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 13), bg="#BCBCEE").place(x=500, y=270)

        self.txt_desc = Text(self.root, font=("goudy old style", 13), bg="white")
        self.txt_desc.place(x=150,y=270,width=300,height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 13), bg="white").place(x=600,y=270,width=180)

        #buttons
        btn_add = Button(self.root, text="Save", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=500, y=305, width=100, height=30)
        btn_update = Button(self.root, text="Update", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=620, y=305, width=100, height=30)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=740, y=305, width=100, height=30)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=860, y=305, width=100, height=30)

        #employee details

        empframe=Frame(self.root,bd=3,relief=RIDGE)
        empframe.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(empframe,orient=VERTICAL)
        scrollx = Scrollbar(empframe, orient = HORIZONTAL)

        #treeview
        self.emptable=ttk.Treeview(empframe,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) #columns are case sensitive. Should be same as database entries

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.emptable.xview)
        scrolly.config(command=self.emptable.yview)

        self.emptable.heading("eid",text="EMP ID")
        self.emptable.heading("name", text="Name")
        self.emptable.heading("email", text="Email")
        self.emptable.heading("gender", text="Gender")
        self.emptable.heading("contact", text="Contact")
        self.emptable.heading("dob", text="D.O.B")
        self.emptable.heading("doj", text="D.O.J")
        self.emptable.heading("password", text="Password")
        self.emptable.heading("utype", text="User Type")
        self.emptable.heading("address", text="Address")
        self.emptable.heading("salary", text="Salary")
        self.emptable["show"]="headings"

        self.emptable.column("eid", width =90)
        self.emptable.column("name", width =90)
        self.emptable.column("email", width =90)
        self.emptable.column("gender", width =90)
        self.emptable.column("contact", width =90)
        self.emptable.column("dob", width =90)
        self.emptable.column("doj", width=90)
        self.emptable.column("password", width =90)
        self.emptable.column("utype", width =90)
        self.emptable.column("address", width =200)
        self.emptable.column("salary", width =90)

        self.emptable.pack(fill=BOTH,expand=1)




if __name__ == "__main__":  # as we are accesing multiple python files, we dont want all files to contradict so we defined file "dashboard" as main()
    root = Tk()  # object : root, Tk : class of tkinter to use the widgets, only by using the object of class Tk  can we use further classes
    obj = employeeClass(root)
    root.mainloop()