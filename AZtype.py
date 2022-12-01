import os
import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox

MyLoginForm = mytk.Tk()
MyLoginForm.title('Login For My_Typing Game')
# Set Form Size
MyLoginForm.geometry("380x200")


def ClicktoLogin():
    # MYSQL ConnectionString
    mydb = mysqlconnector.connect(host="localhost", user="root", password="", database="py_login")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(
        "SELECT * FROM login where username = '" + UserTxt.get() + "' and password = '" + PassTxt.get() + "';")
    myresult = mycursor.fetchone()
    if myresult == None:
        mymessagebox.showerror("Error", "Invalid User Name And Password")

    else:
        # mymessagebox.showinfo("Success", "Successfully Login")
        os.system('python setup.py')


    mydb.close()
    mycursor.close()


# Set Tkinter Widget Size Location and Style
Bannerlabel = Label(MyLoginForm, text="Login Form......", width=40, bg='yellow')
Bannerlabel.place(x=20, y=20)

UserLabel = Label(MyLoginForm, text="User Name:", width=10)
UserLabel.place(x=20, y=60)

UserTxt = Entry(MyLoginForm, width=27, relief="flat")
UserTxt.place(x=120, y=60)

# Set Focus on User Entrybox in Tkinter
UserTxt.focus()

PassLabel = Label(MyLoginForm, text="Password :", width=10)
PassLabel.place(x=20, y=90)

PassTxt = Entry(MyLoginForm, width=27, relief="flat")
PassTxt.place(x=120, y=90)

# Set Password Char in Entry Widget
PassTxt.config(show="*");

LoginBtn = Button(MyLoginForm, text="Login", command=ClicktoLogin, relief="groove", fg='blue')
LoginBtn.place(x=280, y=140)

MyLoginForm.configure(background='#54596d')
MyLoginForm.mainloop()