from tkinter import *
import tkinter.messagebox
import backend

class admin_panel:
    def __init__(self, window, user):
        self.window = window
        self.panel_frame = Frame(self.window, bg = "white", width = 700, height = 250)
        
        self.label = Label(self.panel_frame, text = "User: " + str(user))
        self.label.place(x = 25, y = 20)
        
        self.button_1 = Button(self.panel_frame, text = 'Report', command = backend.reports)
        self.button_1.place(x = 25, y = 70, width = 200, height = 100)
        
        self.button_4 = Button(self.panel_frame, text = 'Add New Student', command = backend.new_student)
        self.button_4.place(x = 235, y = 70, width = 200, height = 100)
        
        self.button_5 = Button(self.panel_frame, text = 'Existing Student', command = backend.student)
        self.button_5.place(x = 445, y = 70, width = 200, height = 100)
        
        self.button_3 = Button(self.panel_frame, text = 'Add Admin', command = backend.admin_add)
        self.button_3.place(x = 25, y = 200, width = 150, height = 30)
        
        self.button_logout = Button(self.panel_frame, text = 'Logout', command = self.window.destroy)
        self.button_logout.place(x=495 ,y=200,width=150,height=30)
        
        self.panel_frame.pack()     