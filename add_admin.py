from tkinter import *
import tkinter.messagebox
import backend

class add_admin:
    def __init__(self, window):
        self.window = window
        self.add_frame = Frame(self.window, bg = 'white', width=400,height=370)
        
        self.label = Label(self.add_frame,text='Details', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=80,y=50,width=250,height=50)

        self.label_user = Label(self.add_frame, text='Username', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_user.place(x=80,y=140,width=100,height=30)
        self.user_text=StringVar(self.add_frame)
        self.entry_user = Entry(self.add_frame, fg='gray',textvariable=self.user_text,width=25,font=('Arial',12,'bold'))
        self.entry_user.place(x=200,y=140,width=150,height=30)
        
        self.pass_show = IntVar(self.add_frame)
        self.pass_check = Checkbutton(self.add_frame, text = "Show password", var = self.pass_show, onvalue = 1, offvalue = 0, command = self.show_pass)
        self.pass_check.place(x=200,y=270)

        self.label_pass1 = Label(self.add_frame, text='Password', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_pass1.place(x=80,y=190,width=100,height=30)
        self.pass1=StringVar(self.add_frame)
        self.entry_pass1 = Entry(self.add_frame,show = "*", fg='gray',textvariable=self.pass1,width=25,font=('Arial',12,'bold'))
        self.entry_pass1.place(x=200,y=190,width=150,height=30)
        
        self.label_pass2 = Label(self.add_frame, text='Re-Enter', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_pass2.place(x=80,y=240,width=100,height=30)
        self.pass2=StringVar(self.add_frame)
        self.entry_pass2 = Entry(self.add_frame,show = "*", fg='gray',textvariable=self.pass2,width=25,font=('Arial',12,'bold'))
        self.entry_pass2.place(x=200,y=240,width=150,height=30)
        
        self.button_subit = Button(self.add_frame, text = "Enter", command = self.submit)
        self.button_subit.place(x=150, y=300,width=120,height=40)
        
        self.add_frame.pack()  
    
    def show_pass(self):
        if self.pass_show.get() == 1:
            self.entry_pass1.config(show="")
            self.entry_pass2.config(show="")
        elif self.pass_show.get() == 0:
            self.entry_pass1.config(show="*")
            self.entry_pass2.config(show="*")
        
    def submit(self):
        if len(self.user_text.get()) ==0 : 
            tkinter.messagebox.showinfo("ERROR", "Enter valid username")
        elif len(self.pass1.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Enter valid Password")
        elif len(self.pass2.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Enter valid Password")
        elif self.pass1.get() != self.pass2.get(): 
            tkinter.messagebox.showinfo("ERROR", "Password mismatch")
        else: 
            self.window.destroy() 
            backend.new_admin(self.user_text.get(),self.pass2.get())