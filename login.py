from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

from hotel2 import HotelManagementSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #======================== VARIABLES ====================================
        self.var_Fname=StringVar()
        self.var_Lname=StringVar()
        self.var_User=StringVar()
        self.var_Email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_Password=StringVar()
        self.var_Confirm=StringVar()
        

        # Load the background image
        self.bg_image = Image.open(r"D:\OOP images\bg.jpg")
        self.bg_image = self.bg_image.resize((1550, 800), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)

        # Set the background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame
        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=130, width=340, height=450)

        # Load the header image
        img01 = Image.open(r"D:\OOP images\headpic.png")
        img01 = img01.resize((100, 100), Image.LANCZOS)
        self.photoimage01 = ImageTk.PhotoImage(img01)
        lblimg01 = Label(frame, image=self.photoimage01, bg="black", borderwidth=0)
        lblimg01.place(x=125, y=10)

        get_str=Label(frame,text="Get Started",font=("Microsoft YaHei UI Light",18,"bold"),
        fg="white", bg="black")
        get_str.place(x=103, y=100)

        #LABEL
        username=Label(frame,text="Username",font=("Microsoft YaHei UI Light",12,"bold"),
        fg="white", bg="black")
        username.place(x=40, y=140)

        self.txtuser=ttk.Entry(frame,font=("Microsoft YaHei UI Light",12,"bold"))
        self.txtuser.place(x=40, y=170, width=270)

        password=Label(frame,text="Password",font=("Microsoft YaHei UI Light",12,"bold"),
        fg="white", bg="black")
        password.place(x=40, y=210)

        self.txtpassword=ttk.Entry(frame,font=("Microsoft YaHei UI Light",12,"bold"))
        self.txtpassword.place(x=40, y=240, width=270)

        #LOGIN BUTTON
        loginbtn=Button(frame,text="LOGIN",font=("Microsoft YaHei UI Light",12,"bold"),
        bd=3, relief=RIDGE,fg="white", bg="#00215E", activeforeground="black",
        activebackground="#FF5580", command=self.login)
        loginbtn.place(x=110, y=300,width=120, height=35)


        #FORGOT PASSWORD
        forgotbtn=Button(frame,text="I Forgot My Password",font=("Microsoft YaHei UI Light",10,"bold"),
        bd=0,fg="white", bg="black", activeforeground="white",
        activebackground="#00215E",command=self.forgot_password_window)
        forgotbtn.place(x=20, y=350,width=160)

    #============================== FUNCTIONS ================================
    def registration_window(self):
        self.new_window=Toplevel(self.root)
        self.app=registration(self.new_window)

#---------------------------------------------------------------------------------
        #Login function
    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error!", "All fields are required")
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM registration WHERE User=%s and Password=%s",
            (self.txtuser.get(),
             self.txtpassword.get()))
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yes or No","Access the admin only")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return

                conn.commit()
                conn.close()


#---------------------------------------------------------------------------------------
    def reset_pass(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="OOP"
    )
        my_cursor = conn.cursor()
        query = "SELECT * FROM registration WHERE User=%s"
        value = (self.txtuser.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "User not found", parent=self.root2)
        else:
            if self.txt_security_q.get() == "":
                messagebox.showerror("Error", "Set a security question", parent=self.root2)
            elif self.txt_security_a.get() == "":
                messagebox.showerror("Error", "Please enter answer", parent=self.root2)
            elif self.txt_security_a.get() != row[5]: 
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = "UPDATE registration SET Password=%s WHERE User=%s"
                value = (self.txt_new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)
 
                conn.commit()
                conn.close() 
                messagebox.showinfo("Success", "Your password has been reset. Please login using new password", parent=self.root2)
                self.root2.destroy()

#-----------------------------------------------------------------------------------------------------------------------------------------

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter Username to reset password")
        elif self.txtpassword.get() != "":
            messagebox.showerror("Error", "Please clear the password field")
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP")
            my_cursor = conn.cursor()
            query = "SELECT * FROM registration WHERE User=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x400+610+170")
                self.root2.configure(bg="black")

                l = Label(self.root2, text="Set a New Password",
                font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="#DFF5FF")
                l.place(x=0, y=10, relwidth=1)

                security_q = Label(self.root2, text="Security Question",
                font=("Microsoft YaHei UI Light", 13, "bold"), fg="black", bg="#DFF5FF")
                security_q.place(x=50, y=80)

                self.txt_security_q = ttk.Entry(self.root2,
                font=("Microsoft YaHei UI Light", 13, "bold"))
                self.txt_security_q.place(x=50, y=110, width=250)

                security_a = Label(self.root2, text="Security Answer",
                font=("Microsoft YaHei UI Light", 13, "bold"), fg="black", bg="#DFF5FF")
                security_a.place(x=50, y=150)

                self.txt_security_a = ttk.Entry(self.root2,
                font=("Microsoft YaHei UI Light", 13, "bold"))
                self.txt_security_a.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password",
                font=("Microsoft YaHei UI Light", 13, "bold"), fg="black", bg="#DFF5FF")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2,
                font=("Microsoft YaHei UI Light", 13, "bold"))
                self.txt_new_password.place(x=50, y=250, width=250)

                button = Button(self.root2, text="Set New Password",
                font=("Microsoft YaHei UI Light", 13, "bold"), fg="black", bg="#DFF5FF",
                command=self.reset_pass)
                button.place(x=90, y=300)

if __name__ == "__main__":
    main()
