from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import backend

class books:
    def __init__(self, window, all_bks):
        self.window = window
        self.books_frame = Frame(self.window, bg = 'white', width=600,height=700)
        
        self.label = Label(self.books_frame,text='BOOKS', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=180,y=50,width=250,height=50)
        
        self.tree_books = ttk.Treeview(self.books_frame)
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
        self.tree_books.place(x = 17, y = 130, height = 470)
        
        self.label_total = Label(self.books_frame, text = "Total books: " + str(self.count))
        self.label_total.place(x = 15, y = 600)
        
        self.button_view = Button(self.books_frame,text='Search', command = self.search)
        self.button_view.place(x=150,y=630,width=100,height=40)

        self.button_search = Button(self.books_frame,text='Add', command = self.add_bk)
        self.button_search.place(x=250,y=630,width=100,height=40)

        self.button_request = Button(self.books_frame, text='Remove', command = self.remove)
        self.button_request.place(x=350, y=630,width=100,height=40)
        
        self.books_frame.pack()
    
    def search(self):
        root = Tk()
        root.title("Enter a book")
        search_frame = Frame(root)
        
        id_label = Label(search_frame, text = "ID")
        id_label.grid(row = 0, column = 0)
        title_label = Label(search_frame, text = "Title")
        title_label.grid(row = 0, column = 1)
        author_entry = Label(search_frame, text = "Author")
        author_entry.grid(row = 0, column = 2)
        
        id_var = IntVar(search_frame)
        id_entry = Entry(search_frame, textvariable = id_var)
        id_entry.grid(row = 1, column = 0)
        title_var = StringVar(search_frame)
        title_entry = Entry(search_frame, textvariable = title_var)
        title_entry.grid(row = 1, column = 1)
        author_var = StringVar(search_frame)
        author_entry = Entry(search_frame, textvariable = author_var)
        author_entry.grid(row = 1, column = 2)
        
        def chk():
            self.selections = []
            for child in self.tree_books.get_children():
                    if (id_var.get() and title_var.get() and author_var.get()) in self.tree_books.item(child)['values']:
                        self.selections.append(child)
                        self.tree_books.selection_set(self.selections)
                        root.destroy()
            
        submit_button = Button(search_frame, text = "Submit", command = chk)
        submit_button.grid(row = 2, column = 0, columnspan = 3)
        
        search_frame.pack(pady = 20)
        root.mainloop()
    
    def add_bk(self):
        add_ = Tk()
        add_.title("Enter a book")
        add_frame = Frame(add_)
        
        title_label = Label(add_frame, text = "Title")
        title_label.grid(row = 0, column = 1)
        author_entry = Label(add_frame, text = "Author")
        author_entry.grid(row = 0, column = 2)
        genre_label= Label(add_frame, text = "Genre ID")
        genre_label.grid(row = 0, column = 3)
        publisher_label= Label(add_frame, text = "Publisher")
        publisher_label.grid(row = 0, column = 5)
        price_label= Label(add_frame, text = "Price")
        price_label.grid(row = 0, column = 6)
        
        title_entry = Entry(add_frame)
        title_entry.grid(row = 1, column = 1)
        author_entry = Entry(add_frame)
        author_entry.grid(row = 1, column = 2)
        genreid_entry= Entry(add_frame)
        genreid_entry.grid(row = 1, column = 3)
        publisher_entry= Entry(add_frame)
        publisher_entry.grid(row = 1, column = 5)
        price_entry= Entry(add_frame)
        price_entry.grid(row = 1, column = 6)
        
        def add():
            if '-' in genreid_entry.get():
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            if '-' in author_entry.get():
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            if "-" in publisher_entry.get():
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            if price_entry.get() < 0:
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            else: 
                a = backend.add_bk(title_entry.get(),author_entry.get(),genreid_entry.get(), 
                    publisher_entry.get(), price_entry.get())
                if (a[1]): 
                    self.tree_books.insert(parent='', index = 'end', iid=self.count, text="", values = (
                        a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7]
                    ))
                    self.count += 1
                    title_entry.delete(0, END)
                    author_entry.delete(0, END)
                    genreid_entry.delete(0, END)
                    publisher_entry.delete(0, END)
                    price_entry.delete(0, END)
                    add_.destroy()
                    self.label_total.config(text = "Total books: " + str(self.count))
                else: 
                    tkinter.messagebox.showerror("ERROR", "Book already exists.")
                    add_.destroy()
        
        submit_button = Button(add_frame, text = "Submit", command = add)
        submit_button.grid(row = 2, column = 0, columnspan = 6)
        
        add_frame.pack(pady = 20)
        
        add_.mainloop()
    
    def remove(self):
        if len(self.tree_books.selection()) == 1:
            q = tkinter.messagebox.askquestion("Warning", "Do you really want to delete the selected record(s) from the Database?")
            if q == 'yes':
                selected=self.tree_books.item(self.tree_books.focus(),'values')
                backend.rmv_bk(selected[0])
                x = self.tree_books.selection()[0]
                self.tree_books.delete(x)
                self.count -= 1
                self.label_total.config(text = "Total Books: " + str(self.count))
        else:
            tkinter.messagebox.showerror("ERROR", "Select one record to remove.")