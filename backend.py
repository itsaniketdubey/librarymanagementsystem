import mysql.connector as mysqlConnector
from tkinter import *
import tkinter.messagebox
from datetime import date
from datetime import datetime
from datetime import timedelta
from admin_panel import admin_panel
from report_panel import report_panel
from add_admin import add_admin
from add_student import add_student
from student_details import student_details
from student_profile import student_profile
from issue_book import issue_book
from books import books
from students_data import students_data
from monthly_reports import monthly_reports

def check(name, passoword):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND pass = %s",(name, passoword))
    for row in cursor: 
        if name in row and passoword in row:
            window = Tk()
            window.title('admin_panel')
            window.minsize(700, 250)
            window.maxsize(700, 250) 
            window.geometry('700x250')
            obj = admin_panel(window, name)
            window.mainloop()
            cursor.close();conn.close()
            return
    tkinter.messagebox.showerror("Error", "Invalid Username or Passowrd.")
    cursor.close();conn.close()
 
def admin_add():
    window = Tk()
    window.title('admin_details')
    window.minsize(400, 370)
    window.maxsize(400, 370) 
    window.geometry('400x370')
    obj = add_admin(window)
    window.mainloop()

def new_admin(user, passwd):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s",(user,))
    for row in cursor: 
        if user in row:
            tkinter.messagebox.showerror("Error", "Admin already exists.")
            cursor.close();conn.close()
            return
    cursor.execute("INSERT INTO users (username, pass) VALUES(%s,%s)", (user, passwd,))
    conn.commit()
    cursor.close();conn.close()
    tkinter.messagebox.showinfo("Success", "Admin has been created successfully.")

def student():
    window = Tk()
    window.title('student_details')
    window.minsize(400, 370)
    window.maxsize(400, 370) 
    window.geometry('400x370')
    obj = student_details(window)
    window.mainloop()

def new_student():
    window = Tk()
    window.title('student_details')
    window.minsize(700, 400)
    window.maxsize(700, 400) 
    window.geometry('700x400')
    obj = add_student(window)
    window.mainloop()

def add_stu(name, sapid, email, dob, con1, con2):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE sap_id = %s",(sapid,))
    for row in cursor: 
        if sapid in row:
            tkinter.messagebox.showerror("Error", "Student already exists.")
            cursor.close();conn.close()
            return
    cursor.execute("INSERT INTO student (stu_name, sap_id, email, dob, contact1, contact2) VALUES(%s,%s,%s,%s,%s,%s)", (name, sapid, email, dob, con1, con2,))
    conn.commit()
    cursor.close();conn.close()
    tkinter.messagebox.showinfo("Success", "Student has been created successfully.")

def student_sub(name, sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE stu_name = %s AND sap_id = %s",(name, sapid))
    for row in cursor: 
        email = row[2];DoB = row[3];con1 = row[4];con2 = row[5];fine = row[6]
        if name in row and sapid in row:
            cursor.execute("SELECT books.book_id,title,borrowed_date,return_date,due_date FROM books INNER JOIN borrowes ON books.book_id = borrowes.book_id where sap_id = %s;",(sapid,))
            std_bks = cursor.fetchall()
            for x in std_bks:
                if x[2] == 'None':
                    tkinter.messagebox.showerror("Error", "Student not returned a book.")
            window = Tk()
            window.title('student_profile')
            window.minsize(700, 400)
            window.maxsize(700, 400) 
            window.geometry('700x400')
            obj = student_profile(window, name, sapid,email,DoB,con1,con2,fine,std_bks)
            window.mainloop()
            cursor.close();conn.close()
            return 
    tkinter.messagebox.showerror("Error", "Student not found.")
    cursor.close();conn.close()

def stu_issue(sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("select * FROM books")
    all_bks = cursor.fetchall()
    window = Tk()
    window.title('issue_book')
    window.minsize(700, 400)
    window.maxsize(700, 400) 
    window.geometry('700x400')
    obj = issue_book(window, all_bks, sapid)
    window.mainloop()
    cursor.close();conn.close()

def reports():
    window = Tk()
    window.title('report')
    window.minsize(450, 300)
    window.maxsize(450, 300) 
    window.geometry('450x300')
    obj = report_panel(window)
    window.mainloop()
    
def stats():
    window = Tk()
    window.title('monthly_genre')
    window.minsize(700, 500)
    window.maxsize(700, 500) 
    window.geometry('700x500')
    obj = monthly_reports(window)
    window.mainloop()
    
def book():
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("select * FROM books")
    all_bks = cursor.fetchall()
    window = Tk()
    window.title('books')
    window.minsize(600, 700)
    window.maxsize(600, 700) 
    window.geometry('600x700')
    obj = books(window, all_bks)
    window.mainloop()
    cursor.close();conn.close()

def std():
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("select * FROM student")
    all_stds = cursor.fetchall()
    window = Tk()
    window.title('students')
    window.minsize(600, 700)
    window.maxsize(600, 700) 
    window.geometry('600x700')
    obj = students_data(window, all_stds)
    window.mainloop()
    cursor.close();conn.close()

def add_bk(title, author, genreid, publisher, price):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    for row in cursor: 
        if title in row and author in row:
            tkinter.messagebox.showerror("Error", "Book already exists.")
            cursor.close();conn.close()
            return False
    cursor.execute("INSERT INTO books (title, author, genreid, publisher, price) VALUES(%s,%s,%s,%s,%s)", 
                   (title, author, genreid, publisher, price,))
    conn.commit()
    cursor.execute("SELECT * FROM books WHERE title = %s and author = %s",(title, author,))
    for row in cursor.fetchall(): 
        return row, True
    cursor.close();conn.close()
    tkinter.messagebox.showinfo("Success", "Book has been added successfully.")
    
def rmv_bk(bookid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = %s",(bookid,))
    conn.commit()
    cursor.close();conn.close()

def rmv_std(sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE sap_id = %s",(sapid,))
    conn.commit()
    cursor.close();conn.close()
    
def pay_fine(sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("UPDATE student set fine = 0 WHERE sap_id = %s",(sapid,))
    conn.commit()
    cursor.close();conn.close()

def assign_bk(borrow,due,bookid,sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO borrowes (borrowed_date, due_date, book_id, sap_id) VALUES(%s,%s,%s,%s)",(borrow,due,bookid,sapid,))
    conn.commit()
    cursor.execute("UPDATE books SET stat = 1 WHERE book_id = %s",(bookid,))
    conn.commit()
    cursor.execute("UPDATE books SET noti = noti + 1 WHERE book_id = %s",(bookid,))
    conn.commit()
    cursor.close();conn.close()
    
def rtn_bk(bookid, sapid, due):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    rtn_date = date.today()
    cursor.execute("UPDATE borrowes SET return_date = %s WHERE book_id = %s",(rtn_date,bookid,))
    conn.commit()
    cursor.execute("UPDATE books SET noti = noti + 1 WHERE book_id = %s",(bookid,))
    conn.commit()
    cursor.execute("select datediff(return_date,due_date) from borrowes WHERE book_id = %s",(bookid,))
    a = cursor.fetchall()
    diff = a[0][0]
    if diff > 7:
        cursor.execute("UPDATE student SET fine = fine + 5*%s WHERE sap_id = %s",(diff,sapid,))
        conn.commit()
    cursor.close();conn.close()

def recc(sapid):
    conn = mysqlConnector.connect(host='localhost',user='root',passwd='rootpass',database = 'project_test3')
    cursor = conn.cursor()
    cursor.execute("select genreid from books inner join borrowes on books.book_id = borrowes.book_id where sap_id = %s limit 1;",(sapid,))
    a = cursor.fetchall()
    cursor.execute("select book_id,title,noti from books where genreid = %s and stat = 0 order by noti desc LIMIT 3;",(a[0][0],))
    return cursor.fetchall()
    
    
    