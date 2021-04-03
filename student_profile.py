from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import backend
import datetime
 
class student_profile: 
    def __init__(self, window, name, sapid,email,DoB,con1,con2, fine, std_bks):
        self.sap = sapid
        self.window = window
        self.studet_frame = Frame(self.window, bg = 'white', width=700,height=400)
        
        self.label_name = Label(self.studet_frame, text = "Name: " + str(name))
        self.label_name.place(x = 135, y = 60)
        self.label_sapid = Label(self.studet_frame, text = "SAP ID: "+ str(sapid))
        self.label_sapid.place(x = 135, y = 90)
        self.label_email = Label(self.studet_frame, text = "Email ID: " + str(email))
        self.label_email.place(x = 240, y = 60)
        self.label_sapid = Label(self.studet_frame, text = "DoB: "+ str(DoB))
        self.label_sapid.place(x = 240, y = 90)
        self.label_email = Label(self.studet_frame, text = "Contact 1: " + str(con1))
        self.label_email.place(x = 420, y = 60)
        self.label_sapid = Label(self.studet_frame, text = "Contact 2: "+ str(con2))
        self.label_sapid.place(x = 420, y = 90)
        
        self.label_curbk = Label(self.studet_frame,text='Current Books:')
        self.label_curbk.place(x= 95, y = 130)
    
        self.label_curbk = Label(self.studet_frame,text='History:')
        self.tree_books = ttk.Treeview(self.studet_frame)
        columns = ("Book ID","Title","Borrowed On", "Returned On", "Due Date")
        self.tree_books['column'] = columns
        self.tree_books.column("#0", width = 0, minwidth = 0, stretch = NO)
        self.tree_books.heading("#0", text = "", anchor = W)
        for name in columns:
            self.tree_books.column(name, anchor = W, width = 80)
            self.tree_books.heading(name, text = name, anchor = W)
        count = 0
        for items in std_bks:
            self.tree_books.insert(parent='', index = 'end', iid=count, text="", values = (items[0],items[1],items[2],items[3], items[4]))
            count += 1
        self.tree_books.place(x = 100, y = 130, height = 160, width = 500)
        
        self.label_fine = Label(self.studet_frame, text = "Current fine: "+ str(fine))
        self.label_fine.place(x= 95, y = 295)
        
        if fine > 0:
            self.label_fine.config(text = "Current fine: "+ str(fine))
            tkinter.messagebox.showerror("alert", "Student has a pending fine.")
            def pay():
                backend.pay_fine(sapid)
                self.window.destroy()
            self.button_view = Button(self.studet_frame,text='Fine Paid', command = pay)
            self.button_view.place(x=100,y=320,width=100,height=40)
            
        
        self.button_issue = Button(self.studet_frame,text='Return', command = self.rtn)
        self.button_issue.place(x=250,y=320,width=100,height=40)

        self.button_issue = Button(self.studet_frame,text='Issue', command = self.iss)
        self.button_issue.place(x=350,y=320,width=100,height=40)
        
        self.studet_frame.pack()
        self.window.update()
        
    def iss(self):
        backend.stu_issue(self.sap)
        self.window.destroy()
        
    def rtn(self):
        selected=self.tree_books.item(self.tree_books.focus(),'values')
        if selected[3] == "None":
            backend.rtn_bk(selected[0], self.sap, selected[4])
            self.window.destroy()