from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from datetime import date
from datetime import datetime
from datetime import timedelta
import random
import backend

class issue_book:
    def __init__(self,window, all_bks, sapid):
        self.bks = list(all_bks)
        self.sap = str(sapid)
        self.window = window
        self.main_frame = Frame(self.window, bg = 'white',relief = SUNKEN, width=700,height=400)

        self.label = Label(self.main_frame,text='Books', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=150,y=20,width=400,height=50)

        self.label_bkid = Label(self.main_frame, text='BOOK ID:',font=('Georgia',14,'bold'))
        self.label_bkid.place(x=10,y=100)
        self.bkid_text=StringVar(self.main_frame)
        self.entry_bkid = Entry(self.main_frame, fg='gray',textvariable=self.bkid_text,width=25,font=('Arial',12,'bold'))
        self.entry_bkid.place(x=95,y=100,width=120)
        
        self.label_title = Label(self.main_frame, text='TITLE:',font=('Georgia',14,'bold'))
        self.label_title.place(x=220,y=100)
        self.title_text=StringVar(self.main_frame)
        self.entry_title = Entry(self.main_frame, fg='gray',textvariable=self.title_text,width=25,font=('Arial',12,'bold'))
        self.entry_title.place(x=280,y=100,width=120)

        self.label_author = Label(self.main_frame, text='AUTHOR:',font=('Georgia',14,'bold'))
        self.label_author.place(x=410,y=100)
        self.author_text=StringVar(self.main_frame)
        self.entry_author = Entry(self.main_frame, fg='gray',textvariable=self.author_text,width=25,font=('Arial',12,'bold'))
        self.entry_author.place(x=500,y=100,width=120)
        
        self.tree_books = ttk.Treeview(self.main_frame)
        columns = ("ID", "Title", "Author", "Status", "Genre", "Publisher", "Price")
        self.tree_books['column'] = columns
        self.tree_books.column("#0", width = 0, minwidth = 0, stretch = NO)
        self.tree_books.heading("#0", text = "", anchor = W)
        for name in columns:
            self.tree_books.column(name, anchor = W, width = 80)
            self.tree_books.heading(name, text = name, anchor = W)
        self.count = 0
        for items in all_bks:
            self.tree_books.insert(parent='', index = 'end', iid=self.count, text="", values = (items[0],items[1],items[2],items[3],items[4],items[5],items[6]))
            self.count += 1
        self.tree_books.place(x = 60, y = 140, height = 200)
        
        self.button_view = Button(self.main_frame,text='Recommend', command = self.recc)
        self.button_view.place(x=80,y=350,width=100,height=40)

        self.button_view = Button(self.main_frame,text='Search', command = self.search)
        self.button_view.place(x=180,y=350,width=100,height=40)

        self.button_issue = Button(self.main_frame,text='Issue', command = self.issue)
        self.button_issue.place(x=280, y=350,width=100,height=40)

        self.button_issue = Button(self.main_frame, text='Clear Fields', command = self.clear)
        self.button_issue.place(x=380, y=350,width=100,height=40)
        
        self.button_issue = Button(self.main_frame, text='Surprise Me', command = self.rand)
        self.button_issue.place(x=480, y=350,width=100,height=40)
        
        self.main_frame.pack()

    def rand(self):
        print(self.bks)
        a = random.choice(self.bks)
        print(a)
        self.tree_books.selection_set(a[0])
    
    def clear(self):
        self.entry_bkid.delete(0, END)
        self.entry_title.delete(0, END)
        self.entry_author.delete(0, END)
        
    def search(self):
        self.selections = []
        for child in self.tree_books.get_children():
            if (self.bkid_text.get() and self.title_text.get() and self.author_text.get()) in self.tree_books.item(child)['values']:
                self.selections.append(child)
                self.tree_books.selection_set(self.selections)
        
    def issue(self):
        selected = self.tree_books.item(self.tree_books.focus(),'values')
        if int(selected[3]) == 1:
            tkinter.messagebox.showerror("ERROR", "Book aready issued.")
        elif int(selected[3]) == 0:
            borrow = date.today()
            due = borrow + timedelta(days=7)
            backend.assign_bk(borrow,due,selected[0],self.sap)
            self.window.destroy()
    
    def recc(self):
        root = Tk()
        root.title("Recommendations")
        
        try:
            a = backend.recc(self.sap)
        except:
            tkinter.messagebox.showerror("ERROR", "Borrow at least one book.")
        else:
            for i in a:
                L1 = Label(root, text = f"Book ID: {i[0]}").pack()
                L2 = Label(root, text = f"Book Title: {i[1]}").pack()
                L3 = Label(root, text = f"NOTI: {i[2]}").pack()
                L4 = Label(root, text = " ").pack()
            
            root.mainloop()