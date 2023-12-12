import tkinter as tk

from tkinter import Tk, Toplevel, StringVar, ttk, Label, Button, OptionMenu, IntVar, Entry
from tkinter import RAISED, CENTER, GROOVE, BOTH, E, W, NW
from utils.app2 import App

class Login:
    def __init__(self):     
        self.window = Tk()
        self.window.title('New_Login')
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.configure(bg="Pink")

        title_label=Label(self.window,text='Welcome User',font = ("Helvetica", 20), justify = CENTER, bg="Pink", fg="black")
        title_label.place(x=80,y=20)


        self.username = StringVar()
        self.password = StringVar()
        self.error1 = StringVar()


        self.username.set('')
        self.password.set('')
        self.error1.set('')
        
        
        usernameLabel = Label (self.window, text = "Username: ", font = ("Helvetica", 16), bg="Pink", fg = "white")
        usernameLabel.place(x=2,y=70)
        passwordLabel = Label (self.window, text = "Password: ", font = ("Helvetica", 16), bg="Pink", fg = "white")
        passwordLabel.place(x=2,y=100)
        errorLabel = Label (self.window, textvariable = self.error1, font = ("Helvetica", 16), bg="Pink", fg = "white")
        errorLabel.place(x=2,y=200)
        
        usernameEntry = Entry (self.window, font = ("Helvetica", 15), width = 20, bd = 5, textvariable = self.username)
        usernameEntry.place(x=120,y=70)

        passwordEntry = Entry (self.window, show = '*', font = ("Helvetica", 15), width = 20, bd = 5, textvariable = self.password)
        passwordEntry.place(x=120,y=100)


        self.tempbtn = Button(self.window, text="Login", bg="gray" , fg="white",font = ("Helvetica", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.checkuser)
        self.tempbtn.place(x=120,y=150)



    def checkuser(self):
        username=self.username.get()
        password=self.password.get()
        if username=="" and password == "":
        
            self.window.destroy()
            App()
        else:
            self.error1.set('Incorrect Password')
        
    def run(self):
        self.window.mainloop()
        
        
if __name__ == "__main__":
    app = Login()
    app.run()
