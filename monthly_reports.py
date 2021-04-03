from tkinter import *
import tkinter.messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector as mysqlConnector
import backend

class monthly_reports:
    def __init__(self, window):
        self.window = window
        self.monthly_frame = Frame(self.window, bg = "white", width = 450, height = 200)
        
        conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
        cursor = conn.cursor()
        df4 = pd.read_sql_query(
           'select genre_name, count(books.genreid) as " " from genre inner join books on books.genreid = genre.genreid group by books.genreid;',conn)
        df4.set_index("genre_name", inplace=True)
        figure1 = plt.Figure(figsize=(9, 10), dpi=120)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.monthly_frame)
        bar1.get_tk_widget().pack(side=TOP, fill=BOTH)
        df4.plot(kind='pie', legend=False, subplots=True, ax=ax1, autopct='%1.1f%%', startangle=15, shadow=True)#,colors=my_colors
        ax1.set_title('Monthly Genre Distribution')

        self.monthly_frame.pack()