import tkinter
from tkinter import messagebox
from tkinter import *
login_form=tkinter.Tk()        
login_form.title("Login Form")
login_form.geometry('550x250')
get=tkinter.StringVar()
gets=tkinter.StringVar()
def login():
    user=get.get()
    passw=gets.get()
    if (user=="Cyber Norse" and passw=="cyber_norse"):
        messagebox.askokcancel(title="Successful Login",message='Username and Password are Correct!')
    elif (user!="Cyber Norse" and passw!="cyber_norse"):
        messagebox.askokcancel(title="Login Failed",message='Username and Password are Incorrect! or you left the TextBox Empty')
        
def exits():
    login_form.destroy()

login_lab1=tkinter.Label(login_form,text='LOGIN FORM',fg='burlywood4').place(x=34,y=33)
login_lab2=tkinter.Label(login_form,text='Username',fg='dark cyan').place(x=34,y=80)
login_lab3=tkinter.Label(login_form,text='Password',fg='dark cyan').place(x=34,y=140)
login_entry1=tkinter.Entry(login_form,textvariable=get).place(x=150,y=80)
login_entry2=tkinter.Entry(login_form,show='*',textvariable=gets).place(x=150,y=140)
login_button1=tkinter.Button(login_form,text='LOGIN',width=9,height=2,command=login,relief=FLAT,bg='light cyan').place(x=320,y=190)
login_button2=tkinter.Button(login_form,text='EXIT',width=9,height=2,command=exits,relief=FLAT,bg='light cyan').place(x=440,y=190)
login_form.mainloop()
