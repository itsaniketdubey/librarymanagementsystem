from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import backend

class students_data:
    def __init__(self, window, all_stds):
        self.window = window
        self.std_db = Frame(self.window, bg = 'white', width=600,height=700)
        
        self.label = Label(self.std_db,text='STUDENTS', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=180,y=50,width=250,height=50)
        
        self.tree_stds = ttk.Treeview(self.std_db)
        columns = ("Name", "SAP ID", "Email ID", "DoB", "Contact 1", "Contact 2", "Fine")
        self.tree_stds['column'] = columns
        self.tree_stds.column("#0", width = 0, minwidth = 0, stretch = NO)
        self.tree_stds.heading("#0", text = "", anchor = W)
        for name in columns:
            self.tree_stds.column(name, anchor = W, width = 80)
            self.tree_stds.heading(name, text = name, anchor = W)
        self.count = 0
        for items in all_stds:
            self.tree_stds.insert(parent='', index = 'end', iid=self.count, text="", values = (items[0],items[1],items[2],items[3],items[4],items[5],items[6]))
            self.count += 1
        self.tree_stds.place(x = 17, y = 130, height = 470)
        
        self.label_total = Label(self.std_db, text = "Total Students: " + str(self.count))
        self.label_total.place(x = 15, y = 600)
        
        self.button_view = Button(self.std_db,text='Search', command = self.search)
        self.button_view.place(x=150,y=630,width=100,height=40)

        self.button_request = Button(self.std_db, text='Remove', command = self.remove)
        self.button_request.place(x=250,y=630,width=100,height=40)
        
        self.std_db.pack()
    
    def search(self):
        root = Tk()
        root.title("Enter Name and SAP ID")
        search_frame = Frame(root)
        
        name_label = Label(search_frame, text = "Name")
        name_label.grid(row = 0, column = 0)
        sapid_label = Label(search_frame, text = "SAP ID")
        sapid_label.grid(row = 0, column = 1)
        email_label = Label(search_frame, text = "EMAIL ID")
        email_label.grid(row = 0, column = 2)

        
        name_var = StringVar(search_frame)
        name_entry = Entry(search_frame, textvariable = name_var)
        name_entry.grid(row = 1, column = 0)
        sapid_var = StringVar(search_frame)
        sapid_entry = Entry(search_frame, textvariable = sapid_var)
        sapid_entry.grid(row = 1, column = 1)
        email_var = StringVar(search_frame)
        email_entry = Entry(search_frame, textvariable = email_var)
        email_entry.grid(row = 1, column = 2)
        
        def chk():
            self.selections = []
            for child in self.tree_stds.get_children():
                if (name_var.get() and sapid_var.get() and email_var.get()) in self.tree_stds.item(child)['values']:
                    self.selections.append(child)
                    self.tree_stds.selection_set(self.selections)
                    root.destroy()
            
        submit_button = Button(search_frame, text = "Submit", command = chk)
        submit_button.grid(row = 2, column = 0, columnspan = 3)
        
        search_frame.pack(pady = 20)
        root.mainloop()
    
    def remove(self):
        if len(self.tree_stds.selection()) == 1:
            q = tkinter.messagebox.askquestion("Warning", "Do you really want to delete the selected record(s) from the Database?")
            if q == 'yes':
                selected = self.tree_stds.item(self.tree_stds.focus(),'values')
                backend.rmv_std(selected[1])
                x = self.tree_stds.selection()[0]
                self.tree_stds.delete(x)
                self.count -= 1
                self.label_total.config(text = "Total Students: " + str(self.count))
        elif len(self.tree_stds.selection()) > 1: 
            q = tkinter.messagebox.askquestion("Warning", "Do you really want to delete the selected record(s) from the Database?")
            if q == 'yes':
                x = self.tree_stds.selection()
                for data in x:
                    self.tree_stds.delete(data)
                    self.count -= 1
                self.label_total.config(text = "Total Students: " + str(self.count))
        else:
            tkinter.messagebox.showerror("ERROR", "Select at least one record to remove.")