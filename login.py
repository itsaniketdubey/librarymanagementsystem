from tkinter import *
import tkinter.messagebox
import backend

class login:  
    def __init__(self,window):
        self.window = window
        self.login_frame = Frame(self.window, bg = 'white', width=400,height=370)
            
        self.label = Label(self.login_frame,text='Login', bg = 'white',relief = SUNKEN,font=('Georgia',30,'bold'))
        self.label.place(x=80,y=50,width=250,height=50)

        self.label_user = Label(self.login_frame, text='Username', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_user.place(x=80,y=160,width=100,height=30)
        self.user_text=StringVar(self.login_frame)
        self.entry_user = Entry(self.login_frame, fg='gray',textvariable=self.user_text,width=25,font=('Arial',12,'bold'))
        self.entry_user.place(x=200,y=160,width=150,height=30)
        self.pass_show = IntVar(self.login_frame)
        self.pass_check = Checkbutton(self.login_frame, text = "Show password", var = self.pass_show, onvalue = 1, offvalue = 0, command = self.show_pass)
        self.pass_check.place(x=200,y=250)

        self.label_pass = Label(self.login_frame, text='Password', bg = 'white',relief = SUNKEN,font=('Georgia',14,'bold'))
        self.label_pass.place(x=80,y=210,width=100,height=30)
        self.pass_text=StringVar(self.login_frame)
        self.entry_pass = Entry(self.login_frame,show = "*", fg='gray',textvariable=self.pass_text,width=25,font=('Arial',12,'bold'))
        self.entry_pass.place(x=200,y=210,width=150,height=30)

        self.button_request = Button(self.login_frame, text='Login', command = self.login)
        self.button_request.place(x=150, y=300,width=150,height=30)

        self.login_frame.pack()
    
    def show_pass(self):
        if self.pass_show.get() == 1:
            self.entry_pass.config(show="")
        elif self.pass_show.get() == 0:
            self.entry_pass.config(show="*")
        
    def login(self):
        if len(self.user_text.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Username is empty")
        elif len(self.pass_text.get()) == 0: 
            tkinter.messagebox.showinfo("ERROR", "Password is empty")
        else: 
            self.window.destroy()
            backend.check(self.user_text.get(),self.pass_text.get())
       
window = Tk()
window.title('login')
window.minsize(400, 370)
window.maxsize(400, 370) 
window.geometry('400x370')
obj = login(window)
window.mainloop()