from tkinter import *
import tkinter.messagebox
from tkcalendar import Calendar
from datetime import datetime
import backend

class add_student:
    def __init__(self, window):
        self.window = window
        self.studet_frame = Frame(self.window, bg = 'white', width=700,height=400)
        
        self.label = Label(self.studet_frame,text='Details', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=150,y=50,width=400,height=50)

        self.label_name = Label(self.studet_frame, text='Name', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_name.place(x=70,y=160,width=100,height=30)
        self.name_text = StringVar(self.studet_frame)
        self.entry_name = Entry(self.studet_frame,textvariable = self.name_text, fg='gray', width=25,font=('Arial',12,'bold'))
        self.entry_name.place(x=180,y=160,width=150,height=30)

        self.label_sapid = Label(self.studet_frame, text='SAP ID', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_sapid.place(x=70,y=210,width=100,height=30)
        self.sapid_text = StringVar(self.studet_frame)
        self.entry_sapid = Entry(self.studet_frame, fg='gray',textvariable = self.sapid_text,width=25,font=('Arial',12,'bold'))
        self.entry_sapid.place(x=180,y=210,width=150,height=30)
        
        self.label_email = Label(self.studet_frame, text='Email', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_email.place(x=360,y=160,width=100,height=30)
        self.email_text = StringVar(self.studet_frame)
        self.entry_email = Entry(self.studet_frame, fg='gray',textvariable = self.email_text,width=25,font=('Arial',12,'bold'))
        self.entry_email.place(x=470,y=160,width=150,height=30)
        
        self.label_dob = Label(self.studet_frame, text='DOB', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_dob.place(x=360,y=210,width=100,height=30)
        self.dob_text = StringVar(self.studet_frame)
        self.entry_dob = Entry(self.studet_frame, fg='gray',textvariable = self.dob_text,width=25,font=('Arial',12,'bold'))
        self.entry_dob.place(x=470,y=210,width=150,height=30)
        self.entry_dob.bind('<Button-1>', self.cal)
        
        self.label_con1 = Label(self.studet_frame, text='Contact 1', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_con1.place(x=70,y=260,width=100,height=30)
        self.con1_text = StringVar(self.studet_frame)
        self.entry_con1 = Entry(self.studet_frame, fg='gray',textvariable = self.con1_text,width=25,font=('Arial',12,'bold'))
        self.entry_con1.place(x=180,y=260,width=150,height=30)
        
        self.label_con2 = Label(self.studet_frame, text='Contact 2', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_con2.place(x=360,y=260,width=100,height=30)
        self.con2_text = StringVar(self.studet_frame)
        self.entry_con2 = Entry(self.studet_frame, fg='gray',textvariable = self.con2_text,width=25,font=('Arial',12,'bold'))
        self.entry_con2.place(x=470,y=260,width=150,height=30)
        
        self.button_subit = Button(self.studet_frame, text = "Enter", command = self.submit)
        self.button_subit.place(x=280, y=310,width=120,height=40)
        
        self.studet_frame.pack()
        
    def cal(self, event):
        def return_date():
            self.entry_dob.delete(0 ,END)
            self.entry_dob.insert(END, self.cal.selection_get())
            root.destroy()
        root = Tk();root.title("Select a date")
        self.cal = Calendar(root, font="Arial 14", selectmode='day', year=2021, month=4, day=10)
        self.cal.pack(fill="both", expand=True)
        cal_button = Button(root, text="Okay", command = return_date).pack()
        root.mainloop()
    
    def submit(self):
        if len(self.entry_name.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Student name is empty")
        elif len(self.entry_sapid.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "SAP ID is empty")
        elif len(self.entry_email.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Email ID is empty")
        elif len(self.entry_dob.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "DOB is empty")
        elif len(self.entry_con1.get()) == 0 and len(self.entry_con2.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Contact is empty")
        else: 
            if '-' in self.entry_name.get():
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            if '-' in self.entry_sapid.get():
                tkinter.messagebox.showerror("ERROR", "Enter valid inputs")
            if "@" and ".com" in self.entry_email.get():
                pass
            if len(self.entry_con1.get()) == 10 and len(self.entry_con2.get())==10: 
                pass
                self.window.destroy()
                backend.add_stu(self.name_text.get(), self.sapid_text.get(), self.email_text.get(),
                                    self.cal.selection_get(),self.con1_text.get(), self.con2_text.get())
            else: tkinter.messagebox.showerror("ERROR", "Enter valid inputs")