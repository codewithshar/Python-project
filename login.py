from tkinter import*
from tkinter import messagebox
import os
class Login_System:
  def __init__(self,root):#===constructor===
      self.root=root
      self.root.title("Login System ")
      self.root.geometry("1350x700+0+0") 
      #--images--
      #self.phone_image= ImageTK.photoImage(file="images/phone.jpg")
       #---login_frame---
      self.employee_id=StringVar()
      self.password=StringVar()
      Login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
      Login_frame.place(x=650,y=90,width=350,height=460)     
      #--employee_id--
      title=Label(Login_frame,text="Login System",font=("elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
      lbl_user=Label(Login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
      txt_usename=Entry(Login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="white").place(x=50,y=140,width=250)
     #----password---
      lbl_pass=Label(Login_frame,text="password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
      txt_pass=Entry(Login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="white").place(x=50,y=240,width=230)
     #---login button----
      btn_login=Button(Login_frame,command=self.Login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg ="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
     # ----forget password
      hr=Label(Login_frame,bg="lightgrey").place(x=50,y=380,width=250,height=2)
      #---or between line ---
      or_=Label(Login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=365)
      #--btn forget--
      btn_forget=Button(Login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=100,y=390)
      #==frame2 (didn't have an account)
      register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
      register_frame.place(x=650,y=570,width=350,height=40)  
      #===dint have an account
      
      lbl_reg=Label(register_frame,text="Don't have an account ?",font=("times new roman ",13),bg="white").place(x=20,y=10)
      btn_signup=Button(register_frame,text="signup",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=200,y=5)


  def Login(self): 
     con=sqlite3.connect(database=r'ims.db')
     cur=con.cursor()
     try:
        if self.employee_id.get()=="" or self.password.get()=="":
             messagebox.showerror('Error',"All fields are required",parent=self.root)
        else:
            cur.execute("select* from employee where eid=? AND  pass=?",(self.employee_id.get(),self.password.get()))
            user=cur.fetchall()
            if user==None:
               messagebox.showerror('Error',"Invalid Employee_id/password",parent=self.root)
            else:
               self.root.destroy()
               os.system(("python dashboard.py"))
                     
     except Exception as ex:
        messagebox.showerror("Error","Error due to : {str(ex)}",parent=self.root)

   
root =Tk()
obj=Login_System(root)
root.mainloop()        