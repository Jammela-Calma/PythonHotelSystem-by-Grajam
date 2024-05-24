from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

from pls1 import customer_frame
from reservation import Reservation

class HotelManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL GUEST RESERVATION SYSTEM BY: GRAJAM")
        self.root.geometry("1560x900")
        #====================image01========================================
        img01=Image.open(r"D:\OOP images\hotel ril.jpg")
        img01=img01.resize((1550,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img01)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=150)

        #===================logopic========================================
        img02=Image.open(r"D:\OOP images\logoo\2.png")
        img02=img02.resize((230,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img02)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=150)

        #================title===================================================================
        title=Label(self.root,text="HOTEL GUEST RESERVATION SYSTEM",font=("Times New Roman",30,
        "bold"),bg="black",fg="#F8F0E5",bd=4,relief=RIDGE)
        title.place(x=0,y=150,width=1550,height=50)

        #======================frame===============================================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #=========================menu===========================================================
        lblmenu=Label(main_frame, text="MENU", font=("Times New Roman", 20, "bold"),fg="#F8F0E5", 
        bg="black", bd=4, relief= RIDGE)
        lblmenu.place(x=0, y=0, width=235)

        #================================BUTTONS====================================================
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=235, height=210)

        cstmr_button=Button(btn_frame, width= 22,height=2,text="CUSTOMER DETAILS", font=("Times New Roman", 14,"bold"), 
        bg="black", fg="#F8F0E5", relief=RIDGE, command=self.customer_details)
        cstmr_button.pack(pady=2)
      #  cstmr_button.grid(row=0, column=0, pady=1)

        rsrvtn_button=Button(btn_frame, width= 22,height=2,text="RESERVATION", font=("Times New Roman", 14,"bold"), 
        bg="black", fg="#F8F0E5", relief=RIDGE, command=self.Reservation)
        rsrvtn_button.pack(pady=2)

        logout_button=Button(btn_frame, width= 22,height=2,text="LOGOUT", font=("Times New Roman", 14,"bold"), 
        bg="black", fg="#F8F0E5", relief=RIDGE,command=self.logout)
        logout_button.pack(pady=2)

        #==============================right picture=============================================================\
        r_img=Image.open(r"D:\OOP images\lb1.jpg")
        r_img=r_img.resize((1310,590),Image.LANCZOS)
        self.photor_img=ImageTk.PhotoImage(r_img)

        lblimg=Label(main_frame,image=self.photor_img,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

        #=========================================other images===============================================
        room_img=Image.open(r"D:\OOP images\otel.jpg")
        room_img=room_img.resize((230,235),Image.LANCZOS)
        self.photoroom_img=ImageTk.PhotoImage(room_img)

        lblimg=Label(main_frame,image=self.photoroom_img,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=220,width=230,height=235)

    #===================== CUSTOMER DETAILS ========================
    def customer_details(self):
     self.new_frame=Toplevel(self.root)
     self.app=customer_frame(self.new_frame)

    #==================CUSTOMER RESERVATION==========================
    def Reservation(self):
     self.new_frame=Toplevel(self.root)
     self.app=Reservation(self.new_frame)
    #====================== LOG OUT ===============================
    def logout(self):
       self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

