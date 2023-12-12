import tkinter as tk

from tkinter import Tk, Button, RAISED, GROOVE, CENTER
from utils.notepad import Notepad
from utils.calcu import Calculator
from utils.converter import Converter


class App:
    def __init__(self):     

# Initialize the main window

        self.window = Tk()
        self.window.title('Ridas MultiFunction Application')
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.configure(bg="Pink")

# Create the title label

        title_label=tk.Label(self.window,text='Please choose a function',font = ("Helvetica", 15, "bold"), justify = CENTER, bg="pink", fg="black")
        title_label.place(x=70,y=20)

# Create the main UI buttons

        self.create_main_ui_buttons()

    def create_main_ui_buttons(self):

# Unit Converter Button

        self.convbtn = Button(self.window, text="UNIT CONVERTER", bg="gray" , fg="white",font = ("Helvetica", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=self.converter_open)
        self.convbtn.place(x=55,y=200)

# Calculator Button
        self.calcbtn = Button(self.window, text="CALCULATOR", bg="gray" , fg="white",font = ("Helvetica", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=self.calcu_open)
        self.calcbtn.place(x=85,y=120)

# Notepad Button
        self.notebtn = Button(self.window, text="NOTEPAD", bg="gray" , fg="white",font = ("Helvetica", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command=self.notepad_open)
        self.notebtn.place(x=110,y=280)

# Exit Button
        self.exitbtn = Button(self.window, text="EXIT", bg="gray", fg="white",font = ("Helvetica", 20, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "red", activeforeground="white", command=self.window.destroy)
        self.exitbtn.place(x=150,y=360)

# Label for the developer's name
        title_label=tk.Label(self.window,text='Rida Amjed',font = ("Helvetica", 8, "bold"), justify = CENTER, bg="pink", fg="black")
        title_label.place(x=300,y=640)
    
# Method to open the calculator

    def calcu_open(self):
        Calculator()
        self.window.destroy()
        
# Method to open the unit converter
 
    def converter_open(self):
        self.window.destroy()
        Converter()
    
# Method to open the notepad

    def notepad_open(self):
        self.window.destroy()
        Notepad()

# Method to start the main event loop

    def run(self):
        self.window.mainloop()

# Create an instance of the App class when the script is run

if __name__ == "__main__":
    app = App()
    app.run()

