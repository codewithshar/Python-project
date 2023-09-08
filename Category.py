from tkinter import*
""" tkinter : in built class that has widgests for creating dashboard"""
from PIL import Image,ImageTk
"""pip install pillow, used for gif,jpeg and resize of images"""
from tkinter import ttk
# Window
class categoryClass:
    def __init__(self,root): #default constructor, Object : root
        self.root=root #to initialise the object root of Tk. Self is used for defining the object if the class
        self.root.geometry("1100x500+220+130") #to give dimensions to the running window ("width,height+ top where to start from+gap from bottom)
        self.root.title("I.T.S Inventory Management System | Developed by ITS Students")
        self.root.config(bg="#BCBCEE")
        self.root.focus_force()

        #variables
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #Title
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",25),bg="#7F7FFF").pack(side=TOP,fill=X,padx=10,pady=10)

        #label
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",13),bg="#BCBCEE").place(x=30,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",13)).place(x=30,y=130,width=200)

        btn_add = Button(self.root, text="ADD",font=("goudy old style",13),bg="white",cursor="hand2").place(x=300, y=128,width=150,height=30)
        btn_delete = Button(self.root, text="DELETE", font=("goudy old style", 13), bg="white", cursor="hand2").place(x=470,y=128,width=150,height=30)

        #tree view

        catframe = Frame(self.root, bd=3, relief=RIDGE)
        catframe.place(x=650, y=128, width=420, height=360)

        scrolly = Scrollbar(catframe, orient=VERTICAL)
        scrollx = Scrollbar(catframe, orient=HORIZONTAL)

        # treeview
        self.categoryTable = ttk.Treeview(catframe, columns=("cid", "name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  # columns are case sensitive. Should be same as database entries

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid", text="C.ID")
        self.categoryTable.heading("name", text="Name")
        self.categoryTable["show"] = "headings"

        self.categoryTable.column("cid", width=90)
        self.categoryTable.column("name", width=90)
        self.categoryTable.pack(fill=BOTH, expand=1)

        #image

        #img 1

        self.im1=Image.open("C:\Major Project\Category.jpg")
        self.im1=self.im1.resize((300,270),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50, y=200)

        #img 2

        self.im2 = Image.open("C:\Major Project\category 2.jpg")
        self.im2 = self.im2.resize((130,130), Image.ANTIALIAS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=400, y=200)

        #img 3

        self.im3 = Image.open("C:\Major Project\category3.jpg")
        self.im3 = self.im3.resize((130, 130), Image.ANTIALIAS)
        self.im3 = ImageTk.PhotoImage(self.im3)

        self.lbl_im3 = Label(self.root, image=self.im3,bd=2,relief=RAISED)
        self.lbl_im3.place(x=400, y=340)





if __name__ == "__main__":  # as we are accesing multiple python files, we dont want all files to contradict so we defined file "dashboard" as main()
    root = Tk()  # object : root, Tk : class of tkinter to use the widgets, only by using the object of class Tk  can we use further classes
    obj = categoryClass(root)
    root.mainloop()