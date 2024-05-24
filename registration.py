from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from login import Login_Window

class registration():
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("1600x900+0+0")

        #======================== VARIABLES ====================================
        self.var_Fname=StringVar()
        self.var_Lname=StringVar()
        self.var_User=StringVar()
        self.var_Email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_Password=StringVar()
        self.var_Confirm=StringVar()

#============= BG IMAGE ====================================================
        self.bg_image01 = Image.open(r"D:\OOP images\bgtel.jpg")
        self.bg_image01 = self.bg_image01.resize((1600, 900), Image.LANCZOS)
        self.bg_image01 = ImageTk.PhotoImage(self.bg_image01)

        lbl_bg = Label(self.root, image=self.bg_image01)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

#=============== left image ==============================================
        self.bg_image02=Image.open(r"D:\OOP images\otel.jpg")
        self.bg_image02= ImageTk.PhotoImage(self.bg_image02)
        left_lbl=Label(self.root,image=self.bg_image02)
        left_lbl.place(x=50, y=90, width=470, height=423)

#=================== FRAME =================================================
        frame = Frame(self.root, bg="#0F1035")
        frame.place(x=520, y=90, width=800, height=423)


        register_lbl=Label(frame,text="REGISTER HERE", 
        font=("Cambria",18,"bold"),fg="white",bg="black")
        register_lbl.place(x=20, y=20)

#==================== LABEL AND ENTRY =====================================
        
        fname=Label(frame,text="First Name",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        fname.place(x=50, y=70)

        fname_entry=ttk.Entry(frame,textvariable=self.var_Fname,
        font=("Cambria",13,"bold"))
        fname_entry.place(x=50, y=100, width=250)
        #------------------------------------------------------------
        lname=Label(frame,text="Last Name",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        lname.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_Lname,
        font=("Cambria",13,"bold"))
        self.txt_lname.place(x=370, y=100, width=250)

        #-------------------------------------------------------------
        user=Label(frame,text="Username",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        user.place(x=50,y=140)

        self.txt_user=ttk.Entry(frame,textvariable=self.var_User,
        font=("Cambria",13,"bold"))
        self.txt_user.place(x=50, y=170, width=250)

        #---------------------------------------------------------------------
        email=Label(frame,text="Email Address",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        email.place(x=370,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_Email,
        font=("Cambria",13,"bold"))
        self.txt_email.place(x=370, y=170, width=250)

        #--------------------------------------------------------------------
        security_q=Label(frame,text="Security Question",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        security_q.place(x=50,y=200)

        self.txt_security_q=ttk.Entry(frame,textvariable=self.var_SecurityQ,
        font=("Cambria",13,"bold"))
        self.txt_security_q.place(x=50, y=230, width=250)

        #-------------------------------------------------------------------
        security_a=Label(frame,text="Security Answer",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        security_a.place(x=370,y=200)

        self.txt_security_a=ttk.Entry(frame,textvariable=self.var_SecurityA,
        font=("Cambria",13,"bold"))
        self.txt_security_a.place(x=370, y=230, width=250)

        #-----------------------------------------------------------------------
        passw=Label(frame,text="Password",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        passw.place(x=50,y=260)

        self.txt_passw=ttk.Entry(frame,textvariable=self.var_Password,
        font=("Cambria",13,"bold"))
        self.txt_passw.place(x=50, y=290, width=250)

        #---------------------------------------------------------------------
        confirm_pass=Label(frame,text="Confirm Password",font=("Cambria",13,"bold"),
        fg="white",bg="black")
        confirm_pass.place(x=370,y=260)

        self.txt_confirm_pass=ttk.Entry(frame,textvariable=self.var_Confirm,
        font=("Cambria",13,"bold"))
        self.txt_confirm_pass.place(x=370, y=290, width=250)

        #======================= BUTTONS =====================================
        register_txt=Label(frame,text="Register your account now:",
        font=("Cambria",12,"bold"),bg="black",fg="white")
        register_txt.place(x=50,y=330)

        register_btn=Button(frame,text="Register Account",
        font=("Cambria",12,"bold"),bg="black",fg="white", command=self.register_acc)
        register_btn.place(x=50, y=380, width=250)

        login_txt=Label(frame,text="Already have an account? Login instead:",
        font=("Cambria",12,"bold"),bg="black",fg="white")
        login_txt.place(x=370,y=330)

        login_btn = Button(frame, text="Login", command=self.open_login_window,
        font=("Cambria", 12, "bold"), bg="black", fg="white")
        login_btn.place(x=370, y=380, width=250)

#======================== FUNCTIONS =============================================================
    def register_acc(self):
        if self.var_Fname.get()=="" or self.var_Email.get()=="" or self.var_SecurityQ=="":
            messagebox.showerror("Error!","All fields are required")
        elif self.var_Password.get() != self.var_Confirm.get():
            messagebox.showerror("Error!","Password and Confirm Password must be the same")
        else: 
             conn = mysql.connector.connect(
             host="localhost",
             username="root",
             password="",
             database="OOP")
             my_cursor = conn.cursor()
             query=("SELECT * FROM registration WHERE Email=%s")
             value=(self.var_Email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row != None:
                 messagebox.showerror("Error","User already exists. Please try another email")
             else:
                 my_cursor.execute("INSERT INTO registration values (%s,%s,%s,%s,%s,%s,%s)",
                (self.var_Fname.get(),
                self.var_Lname.get(),
                self.var_User.get(),
                self.var_Email.get(),
                self.var_SecurityQ.get(),
                self.var_SecurityA.get(),
                self.var_Password.get()))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success!","Registration Complete!")

    def open_login_window(self):
        self.root.destroy()  # Close the registration window
        login_win = Tk()
        app = Login_Window(login_win)
        login_win.mainloop()


if __name__ == "__main__":
    root=Tk()
    app=registration(root)
    root.mainloop()