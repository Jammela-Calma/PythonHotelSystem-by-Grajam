from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

from time import strftime
from datetime import datetime

class Reservation():
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM RESERVATION")
        self.root.geometry("1050x540+220+220")

#======================== VARIABLES ====================================
        self.var_CONTACT=StringVar()
        self.var_CHECK_IN=StringVar()
        self.var_CHECK_OUT=StringVar()
        self.var_ROOM_TYPE=StringVar()
        self.var_AVAIL=StringVar()
        self.var_ADD_ONS=StringVar()
        self.var_NO_DAYS=StringVar()
        self.var_T_COST=StringVar()


 #===================== TITLE ======================================
        title=Label(self.root,text="ROOM RESERVATION",font=("Times New Roman",20,
        "bold"),bg="black",fg="#F8F0E5",bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1280,height=35)

#===================== LABEL FRAME ==============================
        labelframeleft=LabelFrame(self.root, bd=2,relief=RIDGE, 
        text="RESERVATION DETAILS",padx=2, font=("Times New Roman",12, "bold"))
        labelframeleft.place(x=5, y=50, width=450, height=420)

#================== LABELS AND ENTRYS ==================================
#=======Customer Contact Number:
        lbl_cust_mobile= Label(labelframeleft, text="Customer Contact No.:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_cust_mobile.grid(row=0, column=0, sticky=W)

        entry_mobile=Entry(labelframeleft, width=29, textvariable=self.var_CONTACT,
        font=("Times New Roman",12, "bold"))
        entry_mobile.grid(row=0, column=1,sticky=W)

        #======= Fetch data butoon: ========================
        btn_fetch=Button(labelframeleft, text="FETCH DATA", 
        font=("Times New Roman",8, "bold"), fg="#F8F0E5", bg="black", 
        width=9, command=self.fetch_contact)
        btn_fetch.place(x=355, y=3.7)

#=======Check In:
        lbl_checkin= Label(labelframeleft, text="Check In Date:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_checkin.grid(row=1, column=0, sticky=W)
        txt_checkin=ttk.Entry(labelframeleft, textvariable=self.var_CHECK_IN,
        font=("Times New Roman",12, "bold"), width=29)
        txt_checkin.grid(row=1, column=1)

#=========Check Out:
        lbl_checkout= Label(labelframeleft, text="Check Out Date:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_checkout.grid(row=2, column=0, sticky=W)
        txt_checkout=ttk.Entry(labelframeleft,textvariable=self.var_CHECK_OUT,
        font=("Times New Roman",12, "bold"), width=29)
        txt_checkout.grid(row=2, column=1)

#=======Room Type:
        lbl_roomtype= Label(labelframeleft, text="Room Type:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft, textvariable=self.var_ROOM_TYPE,
        font=("Times New Roman",11, "bold"),state="readonly", width=29)
        combo_roomtype["value"]=("Single Room (Standard)","Single Room (Luxury)",
        "Double Room (Standard)","Double Room (Luxury)", "Twin Room (Standard)",
        "Twin Room (Luxury)","Family Room (Standard)","Family Room (Luxury)")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

#=======Room Number:
        lbl_room= Label(labelframeleft, text="Room Number:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_room.grid(row=4, column=0, sticky=W)
        txt_room=ttk.Entry(labelframeleft, textvariable=self.var_AVAIL,
        font=("Times New Roman",12, "bold"), width=29)
        txt_room.grid(row=4, column=1)

#=======Add Ons:
        lbl_addons= Label(labelframeleft, text="Add Ons:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_addons.grid(row=5, column=0, sticky=W)

        combo_addons=ttk.Combobox(labelframeleft, textvariable=self.var_ADD_ONS,
        font=("Times New Roman",11, "bold"),
        state="readonly", width=29)
        combo_addons["value"]=("Dinner","Breakfast", "Dinner and Breakfast",
        "Access to Private Swimming Pool","Access to Gaming Room",
        "Access to Massage Room","Access to Sauna","Access to Private Bar")
        combo_addons.current(0)
        combo_addons.grid(row=5,column=1)

#=======Number of Days Staying in the hotel:
        lbl_days= Label(labelframeleft, text="Number of Days:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_days.grid(row=6, column=0, sticky=W)
        txt_days=ttk.Entry(labelframeleft, textvariable=self.var_NO_DAYS,
        font=("Times New Roman",12, "bold"), width=29)
        txt_days.grid(row=6, column=1)

#=======Total Cost of Stay:
        lbl_cost= Label(labelframeleft, text="Total Amount to be Paid:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_cost.grid(row=7, column=0, sticky=W)
        txt_cost=ttk.Entry(labelframeleft, textvariable=self.var_T_COST,
        font=("Times New Roman",12, "bold"), width=29)
        txt_cost.grid(row=7, column=1)


        #======================= BUTTONS=====================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=310, width=335, height=38)

        btn_Add=Button(btn_frame, text="ADD", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.add_reservation)
        btn_Add.grid(row=0, column=0, pady=2)

        btn_update=Button(btn_frame, text="UPDATE", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.update_reserv)
        btn_update.grid(row=0, column=1, pady=2)

        btn_delete=Button(btn_frame, text="DELETE", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.delete_reserv)
        btn_delete.grid(row=0, column=2, pady=2)

        btn_reset=Button(btn_frame, text="RESET", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.reset_reserv)
        btn_reset.grid(row=0, column=3, pady=2)

        btn_bill=Button(labelframeleft, text="BILL", font=("Times New Roman",9, "bold"), 
        fg="black", bg="#BFCFE7", width=8, command=self.total)
        btn_bill.place(x=2, y=280)

#================  search system ============================
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
        font=("Times New Roman",12, "bold"), pady=2)
        table_frame.place(x=460, y=200, width=570, height=420)

        lblsearch=Label(table_frame,font=("Times New Roman", 12, "bold"),text="Search By:",
        bg="pink", fg="black")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame, textvariable=self.search_var,
        font=("Times New Roman",12), width= 15, state="readonly")
        combo_search["value"]=("CONTACT", "ROOM")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,
         font=("Times New Roman",12), width=20)
        txtsearch.grid(row=0, column=2, padx=2)

        btn_search=Button(table_frame, text="SEARCH", font=("Times New Roman",10, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.search_reserv)
        btn_search.grid(row=0, column=3, padx=5)

        btn_show=Button(table_frame, text="SHOW ALL", font=("Times New Roman",10, "bold"), 
        fg="#F8F0E5", bg="black", width=9, command=self.fetch_data)
        btn_show.grid(row=0, column=4, padx=5)

        #=========================== DATA TABLE ========================================
        data_tab=Frame(table_frame,bd=2, relief=RIDGE)
        data_tab.place(x=0, y=50, width=550, height=150)

        scroll_x=ttk.Scrollbar(data_tab, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_tab, orient=VERTICAL)

        self.reserv_table=ttk.Treeview(data_tab, column=("CONTACT","CHECK_IN","CHECK_OUT", 
        "ROOM_TYPE","AVAIL", "ADD_ONS",'NO_DAYS',"T_COST"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.reserv_table.xview)
        scroll_y.config(command=self.reserv_table.yview)

        self.reserv_table.heading("CONTACT", text="Contact No.")
        self.reserv_table.heading("CHECK_IN", text="Check In Date")
        self.reserv_table.heading("CHECK_OUT", text="Check Out Date")
        self.reserv_table.heading("ROOM_TYPE", text="Room Type")
        self.reserv_table.heading("AVAIL", text="Room Number")
        self.reserv_table.heading("ADD_ONS", text="Add Ons")
        self.reserv_table.heading("NO_DAYS", text="No. of Days")
        self.reserv_table.heading("T_COST", text="Total Cost")

        self.reserv_table["show"]="headings"

        self.reserv_table.column("CONTACT", width=150, anchor=CENTER)
        self.reserv_table.column("CHECK_IN", width=150, anchor=CENTER)
        self.reserv_table.column("CHECK_OUT", width=150, anchor=CENTER)
        self.reserv_table.column("ROOM_TYPE", width=150, anchor=CENTER)
        self.reserv_table.column("AVAIL", width=150, anchor=CENTER)
        self.reserv_table.column("ADD_ONS", width=150, anchor=CENTER)
        self.reserv_table.column("NO_DAYS", width=150, anchor=CENTER)
        self.reserv_table.column("T_COST", width=150, anchor=CENTER)

        self.reserv_table.pack(fill=BOTH, expand=1)
        self.reserv_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        
#================= add data ==============================

    def add_reservation(self):
        if self.var_CONTACT.get() == "" or self.var_CHECK_IN.get() == "" or self.var_CHECK_OUT.get() == "" or self.var_AVAIL.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="OOP"
            )
                my_cursor = conn.cursor()

            # Check if the contact number already exists
                my_cursor.execute("SELECT * FROM reservation WHERE CONTACT=%s", (self.var_CONTACT.get(),))
                contact_row = my_cursor.fetchone()

            # Check if the room number already exists
                my_cursor.execute("SELECT * FROM reservation WHERE AVAIL=%s", (self.var_AVAIL.get(),))
                room_row = my_cursor.fetchone()

                if contact_row is not None:
                    messagebox.showerror("Error", "Contact number already exists!", parent=self.root)
                elif room_row is not None:
                    messagebox.showerror("Error", "Room number already exists!", parent=self.root)
                else:
                    my_cursor.execute(
                    "INSERT INTO reservation (CONTACT, CHECK_IN, CHECK_OUT, ROOM_TYPE, AVAIL, ADD_ONS, NO_DAYS, T_COST) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_CONTACT.get(),
                        self.var_CHECK_IN.get(),
                        self.var_CHECK_OUT.get(),
                        self.var_ROOM_TYPE.get(),
                        self.var_AVAIL.get(),
                        self.var_ADD_ONS.get(),
                        self.var_NO_DAYS.get(),
                        self.var_T_COST.get()
                    )
                )
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Room reservation complete!", parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong! {str(es)}", parent=self.root)


# fetch method: ============================================================================
    def fetch_data(self):
       conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="OOP"
            )
       my_cursor = conn.cursor()
       my_cursor.execute("select * from reservation")
       rows=my_cursor.fetchall()
       if len(rows) != 0:
          self.reserv_table.delete(*self.reserv_table.get_children())
          for i in rows:
             self.reserv_table.insert("", END, values=i)
          conn.commit()
       conn.close()

#========= get cursor: 
    def get_cursor(self,event=""):
       cursor_row=self.reserv_table.focus()
       content=self.reserv_table.item(cursor_row)
       row=content["values"]

       self.var_CONTACT.set(row[0])
       self.var_CHECK_IN.set(row[1])
       self.var_CHECK_OUT.set(row[2])
       self.var_ROOM_TYPE.set(row[3])
       self.var_AVAIL.set(row[4])
       self.var_ADD_ONS.set(row[5])
       self.var_NO_DAYS.set(row[6])
       self.var_T_COST.set(row[7])

#============= update: 
    def update_reserv(self):
        if self.var_CONTACT.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP"
        )
        my_cursor = conn.cursor()
        query = """
            UPDATE reservation 
            SET CHECK_IN=%s, CHECK_OUT=%s, ROOM_TYPE=%s, AVAIL=%s, 
            ADD_ONS=%s, NO_DAYS=%s, T_COST=%s WHERE CONTACT=%s
        """
        values = (
            self.var_CHECK_IN.get(),
            self.var_CHECK_OUT.get(),
            self.var_ROOM_TYPE.get(),
            self.var_AVAIL.get(),
            self.var_ADD_ONS.get(),
            self.var_NO_DAYS.get(),
            self.var_T_COST.get(),
            self.var_CONTACT.get())
        my_cursor.execute(query, values)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer reservation have been updated successfully!", parent=self.root)

#========================== delete :
    def delete_reserv(self):
        mdelete = messagebox.askyesno("Confirmation", "Do you want to delete this reservation?", parent=self.root)
        if mdelete:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP"
        )
            my_cursor = conn.cursor()
            query = "DELETE FROM reservation WHERE CONTACT=%s"
            value = (self.var_CONTACT.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete", "Customer reservation have been deleted successfully!", parent=self.root)
    
        else:
          return
        
#================= reset:
    def reset_reserv(self):
        self.var_CONTACT.set("")
        self.var_CHECK_IN.set("")
        self.var_CHECK_OUT.set("")
        self.var_ROOM_TYPE.set("")
        self.var_AVAIL.set("")
        self.var_ADD_ONS.set("")
        self.var_NO_DAYS.set("")
        self.var_T_COST.set("")

#================================= FETCH DATA ==================================

    def fetch_contact(self):
         if self.var_CONTACT.get()=="":
             messagebox.showerror("Erro!","Please enter contact number", parent=self.root)
         else:
             conn = mysql.connector.connect(
             host="localhost",
             username="root",
             password="",
             database="OOP")
             my_cursor = conn.cursor()
             query=("SELECT NAME FROM customers where MOBILE=%s")
             value=(self.var_CONTACT.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             if row==None:
                 messagebox.showerror("Error","This number cannot be found", 
                parent=self.root)
             else:
                 conn.commit()
                 conn.close()

                 showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                 showDataframe.place(x=470,y=55.2,width=300,height=130)

#====================== FETCH NAME ==================================
                 lblName=Label(showDataframe,text="Name:",font=("Times New Roman",12,"bold"))
                 lblName.place(x=0,y=0)
                 
                 lbl=Label(showDataframe,text=row,font=("Times New Roman",12,"bold"))
                 lbl.place(x=90,y=0)

#=================================== FETCH GENDER ======================================
                 conn = mysql.connector.connect(
                 host="localhost",
                 username="root",
                 password="",
                 database="OOP")
                 my_cursor = conn.cursor()
                 query=("SELECT GENDER FROM customers where MOBILE=%s")
                 value=(self.var_CONTACT.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 lblGender=Label(showDataframe,text="Gender:",font=("Times New Roman",12,"bold"))
                 lblGender.place(x=0,y=30)
                 
                 lbl=Label(showDataframe,text=row,font=("Times New Roman",12,"bold"))
                 lbl.place(x=90,y=30)

#============================ FETCH EMAIL =======================================
                 conn = mysql.connector.connect(
                 host="localhost",
                 username="root",
                 password="",
                 database="OOP")
                 my_cursor = conn.cursor()
                 query=("SELECT EMAIL FROM customers where MOBILE=%s")
                 value=(self.var_CONTACT.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 lblEmail=Label(showDataframe,text="Email:",font=("Times New Roman",12,"bold"))
                 lblEmail.place(x=0,y=60)
                 
                 lbl=Label(showDataframe,text=row,font=("Times New Roman",12,"bold"))
                 lbl.place(x=90,y=60)


                 conn = mysql.connector.connect(
                 host="localhost",
                 username="root",
                 password="",
                 database="OOP")
                 my_cursor = conn.cursor()
                 query=("SELECT COUNTRY FROM customers where MOBILE=%s")
                 value=(self.var_CONTACT.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 lblCountry=Label(showDataframe,text="Home Country:",
                 font=("Times New Roman",12,"bold"))
                 lblCountry.place(x=0,y=90)
                 
                 lbl=Label(showDataframe,text=row,font=("Times New Roman",12,"bold"))
                 lbl.place(x=110,y=90)


#============ TOTAL COST and NUMBER OF DAYS ==========================================
    def total(self):
        InDate=self.var_CHECK_IN.get() 
        OutDate=self.var_CHECK_OUT.get()
        InDate=datetime.strptime(InDate,"%m-%d-%Y")
        OutDate=datetime.strptime(OutDate,"%m-%d-%Y")
        self.var_NO_DAYS.set(abs(OutDate-InDate).days)

        #single room (standard)
        s1=float(1500)
        #single room (luxury)
        s2=float(2200)
        #double room (standard)
        d1=float(3100)
        #double room (luxury)
        d2=float(4150)
        #Twin room (standard)
        t1=float(5103.00)
        #Twin room (luxury)
        t2=float(6435)
        #Family Room (standard)
        f1=float(7400.08)
        #Family Room (luxury)
        f2=float(9193.65)
        #-------- Add ons-------
        #Dinner:
        z1=float(550)
        #Breakfast:
        z2=float(550)
        #Dinner and breakfast:
        z3=float(1100)
        #swimming pool
        z4=float(840)
        #gaming room
        z5=float(630)
        #massage room:
        z6=float(965)
        #sauna:
        z7=float(530)
        #bar:
        z8=float(1200)

        total_cost = 0.0
        d=float(self.var_NO_DAYS.get())
        room_type = self.var_ROOM_TYPE.get()
        add_ons = self.var_ADD_ONS.get()

    #Single Room (Standard) Costs:
        if room_type == "Single Room (Standard)":
            if add_ons == "Dinner":
                q1= float(s1+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(s1+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(s1+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(s1+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(s1+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(s1+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(s1+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(s1+z8)
                total_cost =float(q1*d)

    #Single Room (Luxury) Costs:
        elif room_type == "Single Room (Luxury)":
            if add_ons == "Dinner":
                q1= float(s2+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(s2+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(s2+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(s2+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(s2+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(s2+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(s2+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(s2+z8)
                total_cost =float(q1*d)

    #Double Room (Standard) Costs:
        elif room_type == "Double Room (Standard)":
            if add_ons == "Dinner":
                q1= float(d1+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(d1+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(d1+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(d1+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(d1+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(d1+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(d1+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(d1+z8)
                total_cost =float(q1*d)

    #Double Room (Luxury):
        elif room_type == "Double Room (Luxury)":
            if add_ons == "Dinner":
                q1= float(d2+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(d2+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(d2+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(d2+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(d2+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(d2+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(d2+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(d2+z8)
                total_cost =float(q1*d)

    #Twin Room (Standard):
        elif room_type == "Twin Room (Standard)":
            if add_ons == "Dinner":
                q1= float(t1+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(t1+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(t1+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(t1+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(t1+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(t1+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(t1+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(t1+z8)
                total_cost =float(q1*d)

    #Twin Room (Luxury):
        elif room_type == "Twin Room (Luxury)":
            if add_ons == "Dinner":
                q1= float(t2+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(t2+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(t2+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(t2+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(t2+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(t2+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(t2+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(t2+z8)
                total_cost =float(q1*d)

    #Family Room (Standard):
        elif room_type == "Family Room (Standard)":
            if add_ons == "Dinner":
                q1= float(f1+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(f1+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(f1+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(f1+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(f1+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(f1+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(f1+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(f1+z8)
                total_cost =float(q1*d)

     #Family Room (Luxury):
        elif room_type == "Family Room (Luxury)":
            if add_ons == "Dinner":
                q1= float(f2+z1)
                total_cost = float(q1*d)
            elif add_ons == "Breakfast":
                q1=float(f2+z2)
                total_cost =float(q1*d)
            elif add_ons == "Dinner and Breakfast":
                q1=float(f2+z3)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Swimming Pool":
                q1=float(f2+z4)
                total_cost =float(q1*d)
            elif add_ons == "Access to Gaming Room":
                q1=float(f2+z5)
                total_cost =float(q1*d)
            elif add_ons == "Access to Massage Room":
                q1=float(f2+z6)
                total_cost =float(q1*d)
            elif add_ons == "Access to Sauna":
                q1=float(f2+z7)
                total_cost =float(q1*d)
            elif add_ons == "Access to Private Bar":
                q1=float(f2+z8)
                total_cost =float(q1*d)

        self.var_T_COST.set(total_cost)

# ==================== SEARCH SYSTEM ===============================
    def search_reserv(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="OOP"
    )
        my_cursor = conn.cursor()

        search_column = self.search_var.get()
        search_value = "%" + self.txt_search.get() + "%"

        query = "SELECT * FROM reservation WHERE `{}` LIKE %s".format(search_column)
        my_cursor.execute(query, (search_value,))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.reserv_table.delete(*self.reserv_table.get_children())
        for row in rows:
            self.reserv_table.insert("", END, values=row)

        conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Reservation(root)
    root.mainloop()