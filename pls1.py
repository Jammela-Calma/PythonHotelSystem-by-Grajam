from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class customer_frame():
    def __init__(self,root):
        self.root=root
        self.root.title("CUSTOMER DETAILS")
        self.root.geometry("1050x540+220+220")

    #====================== VARIABLES =============================
        self.var_REF=StringVar()
        x=random.randint(1000,9999)
        self.var_REF.set(str(x))

        self.var_NAME=StringVar()
        self.var_GENDER=StringVar()
        self.var_POST=StringVar()
        self.var_MOBILE=StringVar()
        self.var_EMAIL=StringVar()
        self.var_HOME=StringVar()

     #===================== TITLE ======================================
        title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Times New Roman",20,
        "bold"),bg="black",fg="#F8F0E5",bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1280,height=35)

        ################ LABEL FRAME #############
        labelframeleft=LabelFrame(self.root, bd=2,relief=RIDGE, text="CUSTOMER DETAILS",
        padx=2, font=("Times New Roman",12, "bold"))
        labelframeleft.place(x=5, y=50, width=400, height=420)

        #================== LABELS AND ENTRYS ==================================
        lbl_cust_left= Label(labelframeleft, text="Customer Ref. No.:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        lbl_cust_left.grid(row=0, column=0, sticky=W)

        entry_ref=Entry(labelframeleft, textvariable=self.var_REF, width=25, 
        font=("Times New Roman",12, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        cust_name= Label(labelframeleft, text="Customer Name:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)
        entry_name=Entry(labelframeleft, textvariable=self.var_NAME, width=25, font=("Times New Roman",12))
        entry_name.grid(row=1, column=1)

        label_gender=Label(labelframeleft,text="Gender:", font=("Times New Roman",12,
        "bold"), padx=2, pady=6)
        label_gender.grid(row=2, column=0)
        combo_gender=ttk.Combobox(labelframeleft, textvariable=self.var_GENDER, font=("Times New Roman",12), 
        width= 26, state="readonly")
        combo_gender["value"]=("Male", "Female")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)

        postcode= Label(labelframeleft, text="Post Code:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        postcode.grid(row=3, column=0, sticky=W)
        entry_pcode=Entry(labelframeleft, textvariable=self.var_POST, width=25, font=("Times New Roman",12))
        entry_pcode.grid(row=3, column=1)

        mobile_no= Label(labelframeleft, text="Mobile Number:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        mobile_no.grid(row=4, column=0, sticky=W)
        entry_no=Entry(labelframeleft, textvariable=self.var_MOBILE, width=25, font=("Times New Roman",12))
        entry_no.grid(row=4, column=1)

        email= Label(labelframeleft, text="Email Address:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        email.grid(row=5, column=0, sticky=W)
        entry_email=Entry(labelframeleft, textvariable=self.var_EMAIL, width=25, font=("Times New Roman",12))
        entry_email.grid(row=5, column=1)

        country= Label(labelframeleft, text="Home Country:", 
        font=("Times New Roman",12, "bold"),padx=2, pady=6)
        country.grid(row=6, column=0, sticky=W)
        entry_country=Entry(labelframeleft, textvariable=self.var_HOME, width=25, font=("Times New Roman",13))
        entry_country.grid(row=6, column=1)

        #======================= BUTTONS ================================================================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=370, height=38)

        btn_Add=Button(btn_frame, text="ADD", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.add_data)
        btn_Add.grid(row=0, column=0, pady=2)

        btn_update=Button(btn_frame, text="UPDATE", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.update)
        btn_update.grid(row=0, column=1, pady=2)

        btn_delete=Button(btn_frame, text="DELETE", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.mdelete)
        btn_delete.grid(row=0, column=2, pady=2)

        btn_reset=Button(btn_frame, text="RESET", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.reset)
        btn_reset.grid(row=0, column=3, pady=2)

        #==================== TABLE FRAME =================================
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
        font=("Times New Roman",12, "bold"), pady=2)
        table_frame.place(x=435, y=50, width=600, height=420)

        lblsearch=Label(table_frame,font=("Times New Roman", 12, "bold"),text="Search By:",
        bg="pink", fg="black")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame, textvariable=self.search_var,
        font=("Times New Roman",12), width= 15, state="readonly")
        combo_search["value"]=("REF", "MOBILE")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,
         font=("Times New Roman",12), width=20)
        txtsearch.grid(row=0, column=2, padx=2)

        btn_search=Button(table_frame, text="SEARCH", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=8, command=self.search)
        btn_search.grid(row=0, column=3, padx=5)

        btn_show=Button(table_frame, text="SHOW ALL", font=("Times New Roman",11, "bold"), 
        fg="#F8F0E5", bg="black", width=9, command=self.fetch_data)
        btn_show.grid(row=0, column=4, padx=5)

        #=========================== DATA TABLE ========================================
        data_tab=Frame(table_frame,bd=2, relief=RIDGE)
        data_tab.place(x=0, y=50, width=590, height=300)

        scroll_x=ttk.Scrollbar(data_tab, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_tab, orient=VERTICAL)

        self.cust_data=ttk.Treeview(data_tab, column=("REF","NAME","GENDER", "POST CODE",
        "EMAIL", "MOBILE NO.",'HOME COUNTRY'),xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_data.xview)
        scroll_y.config(command=self.cust_data.yview)

        self.cust_data.heading("REF", text="Reference No.")
        self.cust_data.heading("NAME", text="Customer name")
        self.cust_data.heading("GENDER", text="Gender")
        self.cust_data.heading("POST CODE", text="Post Code")
        self.cust_data.heading("MOBILE NO.", text="Mobile Number")
        self.cust_data.heading("EMAIL", text="Email Address")
        self.cust_data.heading("HOME COUNTRY", text="Home Country")

        self.cust_data["show"]="headings"

        self.cust_data.column("REF", width=100)
        self.cust_data.column("NAME", width=100)
        self.cust_data.column("GENDER", width=100)
        self.cust_data.column("POST CODE", width=100)
        self.cust_data.column("MOBILE NO.", width=100)
        self.cust_data.column("EMAIL", width=100)
        self.cust_data.column("HOME COUNTRY", width=100)

        self.cust_data.pack(fill=BOTH, expand=1)
        self.cust_data.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#================================ FUNCTIONS =========================================================
    def add_data(self):
        if self.var_MOBILE.get() == "" or self.var_EMAIL.get() == "" or self.var_HOME.get() == "":
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

                # Check if the reference number already exists
                query = "SELECT * FROM customers WHERE REF = %s"
                value = (self.var_REF.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "Reference number already exists", parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO customers (REF, NAME, GENDER, POST, MOBILE, EMAIL, COUNTRY) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_REF.get(),
                    self.var_NAME.get(),
                    self.var_GENDER.get(),
                    self.var_POST.get(),
                    self.var_MOBILE.get(),
                    self.var_EMAIL.get(),
                    self.var_HOME.get()
                ))
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Customer details successfully added", parent=self.root)

                    conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong! {str(es)}", parent=self.root)

#--------------------------------------------------------------------------------------------------------------
    def fetch_data(self):
       conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="OOP"
            )
       my_cursor = conn.cursor()
       my_cursor.execute("select * from customers")
       rows=my_cursor.fetchall()
       if len(rows) != 0:
          self.cust_data.delete(*self.cust_data.get_children())
          for i in rows:
             self.cust_data.insert("", END, values=i)
          conn.commit()
       conn.close()
    
#-----------------------------------------------------------------------------------------------
    def get_cursor(self,event=""):
       cursor_row=self.cust_data.focus()
       content=self.cust_data.item(cursor_row)
       row=content["values"]

       self.var_REF.set(row[0])
       self.var_NAME.set(row[1])
       self.var_GENDER.set(row[2])
       self.var_POST.set(row[3])
       self.var_MOBILE.set(row[4])
       self.var_EMAIL.set(row[5])
       self.var_HOME.set(row[6])

#-------------------------------------------------------------------------------------------------------
    def reset(self):
        self.var_NAME.set("")
        self.var_GENDER.set("")
        self.var_POST.set("")
        self.var_MOBILE.set("")
        self.var_EMAIL.set("")
        self.var_HOME.set("")

        x = random.randint(1000, 9999)
        self.var_REF.set(str(x))

#-------------------------------------------------------------------------------------------------------------
    def update(self):
        if self.var_MOBILE.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP"
        )
        my_cursor = conn.cursor()
        query = """
            UPDATE customers 
            SET NAME=%s, GENDER=%s, POST=%s, MOBILE=%s, EMAIL=%s, COUNTRY=%s 
            WHERE REF=%s
        """
        values = (
            self.var_NAME.get(),
            self.var_GENDER.get(),
            self.var_POST.get(),
            self.var_MOBILE.get(),
            self.var_EMAIL.get(),
            self.var_HOME.get(),
            self.var_REF.get()
        )
        my_cursor.execute(query, values)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer details have been updated successfully!", parent=self.root)

#----------------------------------------------------------------------------------------------------------------------------
    def mdelete(self):
        mdelete = messagebox.askyesno("Confirmation", "Do you want to delete this customer info?", parent=self.root)
        if mdelete:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="OOP"
        )
            my_cursor = conn.cursor()
            query = "DELETE FROM customers WHERE ref=%s"
            value = (self.var_REF.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete", "Customer details have been deleted successfully!", parent=self.root)
    
        else:
          return

#-----------------------------------------------------------------------------------------------------------------
    def search(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="OOP"
    )
        my_cursor = conn.cursor()

        search_column = self.search_var.get()
        search_value = "%" + self.txt_search.get() + "%"

        query = "SELECT * FROM customers WHERE `{}` LIKE %s".format(search_column)
        my_cursor.execute(query, (search_value,))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.cust_data.delete(*self.cust_data.get_children())
        for row in rows:
            self.cust_data.insert("", END, values=row)

        conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=customer_frame(root)
    root.mainloop()
