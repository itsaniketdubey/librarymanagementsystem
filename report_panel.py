from tkinter import *
import tkinter.messagebox
import backend

class report_panel:
    def __init__(self, window):
        self.window = window
        self.report_frame = Frame(self.window, bg = "white", width = 450, height = 300)
        
        self.button_1 = Button(self.report_frame, text = 'Students Database', command = backend.std) 
        self.button_1.place(x = 20, y = 50, width = 200, height = 100) 
        
        self.button_2 = Button(self.report_frame, text = 'Books Database', command = backend.book)
        self.button_2.place(x = 230, y = 50, width = 200, height = 100)
        
        self.button_3 = Button(self.report_frame, text = 'Statistics', command = backend.stats)
        self.button_3.place(x = 120, y = 160, width = 200, height = 100)
        
        self.report_frame.pack()
        