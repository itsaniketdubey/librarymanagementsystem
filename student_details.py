from tkinter import *
import tkinter.messagebox
import backend

class student_details:
    def __init__(self, window):
        self.window = window
        self.studet_frame = Frame(self.window, bg = 'white', width=400,height=370)
        
        self.label = Label(self.studet_frame,text='Details', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=80,y=50,width=250,height=50)

        self.label_name = Label(self.studet_frame, text='Name', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_name.place(x=80,y=160,width=100,height=30)
        self.name_text=StringVar(self.studet_frame)
        self.entry_name = Entry(self.studet_frame, fg='gray',textvariable=self.name_text,width=25,font=('Arial',12,'bold'))
        self.entry_name.place(x=200,y=160,width=150,height=30)

        self.label_sapid = Label(self.studet_frame, text='SAP ID', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_sapid.place(x=80,y=210,width=100,height=30)
        self.sapid_text=StringVar(self.studet_frame)
        self.entry_sapid = Entry(self.studet_frame, fg='gray',textvariable=self.sapid_text,width=25,font=('Arial',12,'bold'))
        self.entry_sapid.place(x=200,y=210,width=150,height=30)
        
        self.button_subit = Button(self.studet_frame, text = "Enter", command = self.submit)
        self.button_subit.place(x=150, y=300,width=120,height=40)
        
        self.studet_frame.pack()
        
    def submit(self):
        if len(self.name_text.get()) ==0: 
            tkinter.messagebox.showinfo("ERROR", "Student name is empty")
        elif len(self.sapid_text.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "SAP ID is empty")
        else: 
            self.window.destroy() 
            backend.student_sub(self.name_text.get(),self.sapid_text.get())
