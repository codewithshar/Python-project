from tkinter import*
#""" tkinter : in built class that has widgests for creating dashboard"""
from PIL import Image,ImageTk
#"""pip install pillow, used for gif,jpeg and resize of images"""
from tkinter import ttk
# Window
class productClass:
    def __init__(self,root): #default constructor, Object : root
        self.root=root #to initialise the object root of Tk. Self is used for defining the object if the class
        self.root.geometry("1100x500+220+130") #to give dimensions to the running window ("width,height+ top where to start from+gap from bottom)
        self.root.title("I.T.S Inventory Management System | Developed by ITS Students")
        self.root.config(bg="#BCBCEE")
        self.root.focus_force()

        #variables
        self.var_cat=StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        #frame

        product_Frame=Frame(self.root,bd=2,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)

        #title
        title = Label(product_Frame, text="Manage Product Detail", font=("goudy old style", 15), bg="#7C7CFC").pack(side=TOP,fill=X)

        #label

        lbl_Category = Label(product_Frame, text="Category", font=("goudy old style", 15)).place(x=30,y=60)
        lbl_Supplier = Label(product_Frame, text="Supplier", font=("goudy old style", 15)).place(x=30,y=110)
        lbl_Product_name = Label(product_Frame, text="Name", font=("goudy old style", 15)).place(x=30, y=160)
        lbl_Price = Label(product_Frame, text="Price", font=("goudy old style", 15)).place(x=30, y=210)
        lbl_Quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 15)).place(x=30, y=260)
        lbl_Status = Label(product_Frame, text="Status", font=("goudy old style", 15)).place(x=30, y=310)

        #entry
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=("Select"),state='readonly', justify=CENTER, font=("Times new roman", 13))
        cmb_cat.place(x=150, y=60, width=180)
        cmb_cat.current(0)
        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=("Select"), state='readonly',justify=CENTER, font=("Times new roman", 13))
        cmb_sup.place(x=150, y=110, width=180)
        cmb_sup.current(0)
        txt_Product_name = Entry(product_Frame, text="Name", font=("goudy old style", 15)).place(x=150, y=160)
        txt_Price = Entry(product_Frame, text="Price", font=("goudy old style", 15)).place(x=150, y=210)
        txt_Quantity = Entry(product_Frame, text="Quantity", font=("goudy old style", 15)).place(x=150, y=260)
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status,values=("Active", "Inactive"), state='readonly', justify=CENTER,font=("Times new roman", 13))
        cmb_status.place(x=150, y=310, width=180)
        cmb_status.current(0)

        #button

        btn_add = Button(product_Frame, text="Save", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=20,y=400, width=70, height=30)
        btn_update = Button(product_Frame, text="Update", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=130, y=400, width=70, height=30)
        btn_delete = Button(product_Frame, text="Delete", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=240, y=400, width=70, height=30)
        btn_clear = Button(product_Frame, text="Clear", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=350, y=400, width=70, height=30)

        # search
        SearchFrame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 14, "bold"), bd=4,relief=RIDGE, bg="#BCBCEE")
        SearchFrame.place(x=480, y=20, width=600, height=80)

        # options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,values=("Select", "Category", "Name", "Supplier"), state='readonly', justify=CENTER,font=("Times new roman", 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 13),bg="white").place(x=200, y=10)  # entry for single row entry

        # search button
        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 13), bg="white", cursor="hand2").place( x=410, y=9, width=150, height=30)

        #product Details

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        #tree view

        self.product_table = ttk.Treeview(p_frame, columns=("pid", "category", "supplier","name", "price", "quantity", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  # columns are case sensitive. Should be same as database entries

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="P.ID")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("quantity", text="Quantity")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=50)
        self.product_table.column("category", width=50)
        self.product_table.column("supplier", width=50)
        self.product_table.column("name", width=50)
        self.product_table.column("price", width=50)
        self.product_table.column("quantity", width=50)
        self.product_table.column("status", width=50)

        self.product_table.pack(fill=BOTH, expand=1)











if __name__ == "__main__":  # as we are accesing multiple python files, we dont want all files to contradict so we defined file "dashboard" as main()
    root = Tk()  # object : root, Tk : class of tkinter to use the widgets, only by using the object of class Tk  can we use further classes
    obj =productClass(root)
    root.mainloop()