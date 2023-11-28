import tkinter as tk

from tkinter import Tk, Toplevel, StringVar, ttk, Label, Button, OptionMenu, IntVar, Entry
from tkinter import RAISED, CENTER, GROOVE, BOTH, E, W, NW


class Converter:
    def __init__(self):     
        self.window = Tk()
        self.window.title('UNIT CONVERTER')
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.configure(bg="Pink")

# Create title label

        title_label=Label(self.window,text='SELECT A CONVERSION:',font = ("Helvetica", 20), justify = CENTER, bg="Pink", fg="black")
        title_label.place(x=40,y=20)

# Method to create the menu buttons

        self.create_menu_buttons()

# Method to create the menu buttons   

    def create_menu_buttons(self):
        self.tempbtn = Button(self.window, text="TEMPERATURE", bg="gray" , fg="white",font = ("Helvetica", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.open_temp)
        self.tempbtn.place(x=110,y=120)
        self.lenbtn = Button(self.window, text="LENGTH", bg="gray" , fg="white",font = ("Helvetica", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.open_len)
        self.lenbtn.place(x=145,y=180)
        self.weighbtn = Button(self.window, text="WEIGHT", bg="gray" , fg="white",font = ("Helvetica", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.open_weigh)
        self.weighbtn.place(x=145,y=240)
        self.backbtn = Button(self.window, text="←", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=self.back_buttoncmd)
        self.backbtn.place(x=5,y=10)


# Weight conversion setup

    def WeightConverter(self):
        self.factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
        self.ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "Gram" : 'g', "Centigram" : 'cg', "Milligram" : 'mg'}
        
        self.weigh_window = Tk()
        self.weigh_window.title("Weight Converter")
        self.weigh_window.geometry("375x667")
        self.weigh_window.resizable(False, False)
        
        self.weigh_frame = tk.Frame(self.weigh_window, bg="Pink")
        self.weigh_frame.pack(fill=BOTH, expand=1)
        self.titleLabel = Label (self.weigh_frame, text = "WEIGHT CONVERSION", font = ("Helvetica", 20), justify = CENTER, bg = "Pink", fg="white")
        self.titleLabel.grid(column=1,row=2)

        self.in_amt = StringVar()
        self.in_amt.set('0')
        self.out_amt = StringVar()

        self.in_unit = StringVar()
        self.out_unit = StringVar()
        self.in_unit.set('Select Unit')
        self.out_unit.set('Select Unit')

        self.in_field = ttk.Entry(self.weigh_frame, width=20, textvariable=self.in_amt, font=("Helvetica", 20))
        self.in_field.grid(row=4, column=1, sticky=(W, E))


        self.in_select = OptionMenu(self.weigh_frame, self.in_unit, "Kilogram","Hectagram","Decagram", "Gram", "Decigram","Centigram", "Milligram")
        self.in_select.config(width=10, height = 3, bg="Pink", font=("Helvetica", 10, "bold"), fg="white") 
        self.in_select.grid(column=1, row=3, sticky=W)

        self.txtLabel = Label(self.weigh_frame, text = "Convert To:", font= ("Helvetica", 13, "bold"), bg = "Pink", fg="white")
        self.txtLabel.grid(row = 5, column = 1)

        def convert(amt, frm, to):
            if frm != 'g':
                amt = amt * self.factors[frm]
                return amt / self.factors[to]
            else:
                return amt / self.factors[to]

        def callback():
            try:
                amt = float(self.in_field.get())
            except ValueError:
                self.out_amt.set('Invalid input')
                return None
            if self.in_unit.get() == 'Select Unit' or self.out_unit.get() == 'Select Unit':
                self.out_amt.set('Invalid Unit')
                return None
            else:
                frm = self.ids[self.in_unit.get()]
                to = self.ids[self.out_unit.get()]
                self.out_amt.set(convert(amt, frm, to))

        def switch_unit():
            unit1_holder = self.in_unit.get()
            unit2_holder = self.out_unit.get()
            self.in_unit.set(unit2_holder)
            self.out_unit.set(unit1_holder)
        
        def back_btn():
            self.weigh_window.destroy()
            Converter()
      
    
        self.out_field = ttk.Entry(self.weigh_frame, textvariable=self.out_amt, state="readonly", font=("Helvetica", 20))
        self.out_field.grid(column=1, row=7, sticky=(W, E))
        self.in_select = OptionMenu(self.weigh_frame, self.out_unit, "Kilogram","Hectagram","Decagram", "Gram", "Decigram","Centigram", "Milligram")
        self.in_select.config(width=10, height = 3, bg="Pink", font=("Helvetica", 10, "bold"), fg="white")
        self.in_select.grid(column=1, row=6, sticky=W)

        self.conv_button = tk.Button(self.weigh_frame, text="CONVERT", font=("Helvetica", 10, "bold"), activebackground="green", activeforeground="white", command=callback)
        self.conv_button.grid(column=1, row=8, sticky=W, ipadx = 10, ipady = 10)
        
        self.switchunit_button = tk.Button(self.weigh_frame, text="SWITCH UNIT", font=("Helvetica", 10, "bold"), activebackground="green", activeforeground="white", command=switch_unit)
        self.switchunit_button.grid(column=1, row=5, sticky=W)

        for child in self.weigh_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.in_field.focus()
        self.backbtn = Button(self.weigh_frame, text="←", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=back_btn)
        self.backbtn.grid(column=1, row = 1, sticky = W)
        
 # Length conversion setup

  
    def LengthConverter(self):
        
        self.factors = {'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
        self.ids = {"Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "Meters" : 'm', "Centimeters" : 'cm', "Millileters" : 'mm'}

        self.len_window = Tk()
        self.len_window.title("Length Converter")
        self.len_window.geometry("375x667")
        self.len_window.resizable(False, False)

        self.len_frame = tk.Frame(self.len_window, bg="Pink")
        self.len_frame.pack(fill=BOTH, expand=1)
        self.titleLabel = Label (self.len_frame, text = "LENGTH CONVERSION", font = ("Helvetica", 20), justify = CENTER, bg = "Pink", fg ="white")
        self.titleLabel.grid(column=1,row=2)

        self.in_amt = StringVar()
        self.in_amt.set('0')
        self.out_amt = StringVar()

        self.in_unit = StringVar()
        self.out_unit = StringVar()
        self.in_unit.set('Select Unit')
        self.out_unit.set('Select Unit')

        self.in_field = ttk.Entry(self.len_frame, width=20, textvariable=self.in_amt, font=("Helvetica",20))
        self.in_field.grid(row=4, column=1, sticky=(W, E))

        self.in_select = OptionMenu(self.len_frame, self.in_unit, "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millileters")
        self.in_select.config(width=10, height = 3, bg="Pink", font=("Helvetica", 10, "bold"), fg="white") 
        self.in_select.grid(column=1, row=3, sticky=W)

        self.txtLabel = Label(self.len_frame, text = "Convert To:", font= ("Helvetica", 13, "bold"), bg = "Pink", fg="white")
        self.txtLabel.grid(row = 5, column = 1)


        def convert(amt, frm, to):
            if frm != 'm':
                amt = amt * self.factors[frm]
                return amt / self.factors[to]
            else:
                return amt / self.factors[to]

        def callback():
            try:
                amt = float(self.in_field.get())
            except ValueError:
                self.out_amt.set('Invalid input')
                return None
            if self.in_unit.get() == 'Select Unit' or self.out_unit.get() == 'Select Unit':
                self.out_amt.set('Invalid Unit')
                return None
            else:
                frm = self.ids[self.in_unit.get()]
                to = self.ids[self.out_unit.get()]
                self.out_amt.set(convert(amt, frm, to))
                
        def switch_unit():
            unit1_holder = self.in_unit.get()
            unit2_holder = self.out_unit.get()
            self.in_unit.set(unit2_holder)
            self.out_unit.set(unit1_holder)
             
        def back_btn():
            self.len_window.destroy()
            Converter()
       
 
        self.out_field = ttk.Entry(self.len_frame, textvariable=self.out_amt, state="readonly", font=("Helvetica",20))
        self.out_field.grid(column=1, row=7, sticky=(W, E))
        self.in_select = OptionMenu(self.len_frame, self.out_unit, "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millileters")
        self.in_select.config(width=10, height = 3, bg="Pink", font=("Helvetica", 10, "bold"), fg="white")
        self.in_select.grid(column=1, row=6, sticky=W)

        self.conv_button = tk.Button(self.len_frame, text="CONVERT", font=("Helvetica", 10, "bold"), activebackground="green", activeforeground="white", command=callback)
        self.conv_button.grid(column=1, row=8, sticky=W, ipadx = 10, ipady = 10)
        
        self.switchunit_button = tk.Button(self.len_frame, text="SWITCH UNIT", font=("Helvetica", 10, "bold"), activebackground="green", activeforeground="white", command=switch_unit)
        self.switchunit_button.grid(column=1, row=5, sticky=W)

        for child in self.len_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.in_field.focus()
        self.backbtn = Button(self.len_frame, text="←", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=back_btn)
        self.backbtn.grid(column=1, row = 1, sticky = W)
        

# Temperature conversion setup


    def TemperatureConverter(self):
        def convert():
            try:
                celTemp = celTempVar.get()
                fahTemp = fahTempVar.get()
                kelTemp = kelTempVar.get()
            
            except:
                invalid_input()

            else:
                if celTempVar.get() != 0.0 and fahTempVar.get() == 0.0 and kelTempVar.get() == 0.0:
                    celToFah = (celTemp *  9/5 + 32)
                    celToKel = (celTemp + 273.15)
                    fahTempVar.set(celToFah)
                    kelTempVar.set(celToKel)

                elif fahTempVar.get() != 0.0 and celTempVar.get() == 0.0 and kelTempVar.get() == 0.0:
                    fahToCel = ((fahTemp - 32) * (5/9))
                    fahToKel = ((fahTemp - 32) * (5/9) + 273.15)
                    celTempVar.set(fahToCel)
                    kelTempVar.set(fahToKel)

                elif kelTempVar.get() != 0.0 and fahTempVar.get() == 0. and celTempVar.get() == 0.0:
                    kelToCel = (kelTemp - 273.15)
                    kelToFah = ((kelTemp - 273.15) * 9/5 + 32)
                    celTempVar.set(kelToCel)
                    fahTempVar.set(kelToFah)
                
                else:
                    unit_error()
                
        def invalid_input():
            top = Toplevel(padx=50, pady=50)
            top.grid()
            message = Label(top, text = "Invalid Input Please Use Numbers Only")
            button = Button(top, text="OK", command=top.destroy)

            message.grid(row = 0, padx = 5, pady = 5)
            button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

            fahTempVar.set(int(0))
            celTempVar.set(int(0))
            kelTempVar.set(int(0))
                
        def unit_error():
            top = Toplevel(padx=50, pady=50)
            top.grid()
            message = Label(top, text = "Please Use One Unit Only")
            button = Button(top, text="OK", command=top.destroy)

            message.grid(row = 0, padx = 5, pady = 5)
            button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

            fahTempVar.set(int(0))
            celTempVar.set(int(0))
            kelTempVar.set(int(0))
                    
        def reset():
            top = Toplevel(padx=50, pady=50)
            top.grid()
            message = Label(top, text = "Reset Complete")
            button = Button(top, text="OK", command=top.destroy)

            message.grid(row = 0, padx = 5, pady = 5)
            button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

            fahTempVar.set(int(0))
            celTempVar.set(int(0))
            kelTempVar.set(int(0))


  
        def back_btn():
            window.destroy()
            Converter()

        window = Tk()
        window.title("TEMPERATURE CONVERTER")
        window.geometry("375x667")
        window.resizable(False, False)
        window.configure(bg="Pink")

        celTempVar = IntVar()
        celTempVar.set(int(0))
        fahTempVar = IntVar()
        fahTempVar.set(int(0))
        kelTempVar = IntVar()
        kelTempVar.set(int(0))

        titleLabel = Label (window, text = "CONVERT TEMPERATURE", font = ("Helvetica",18 ), justify = CENTER, bg = "Pink", fg = "white")
        titleLabel.grid(column=1,row=2)
        

        celLabel = Label (window, text = "CELCIUS: ", font = ("Helvetica", 16), bg="Pink", fg = "white")
        celLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)
        
        fahLabel = Label (window, text = "FAHRENHEIT: ", font = ("Helvetica", 16), bg="Pink", fg = "white")
        fahLabel.grid(row = 5, column = 1, pady = 10, sticky = NW)

        kelLabel = Label (window, text = "KELVIN: ", font = ("Helvetica", 16), bg="Pink", fg = "white")
        kelLabel.grid(row = 7, column = 1, pady = 10, sticky = NW)

        celEntry = Entry (window, font = ("Helvetica", 15), width = 20, bd = 5, textvariable = celTempVar)
        celEntry.grid(row = 4, column = 1, pady = 10, sticky = NW, padx = 50 )

        fahEntry = Entry (window, font = ("Helvetica", 15), width = 20, bd = 5, textvariable = fahTempVar)
        fahEntry.grid(row = 6, column = 1, pady = 10, sticky = NW, padx = 50 )

        kelEntry = Entry (window, font = ("Helvetica", 15), width = 20, bd = 5, textvariable = kelTempVar)
        kelEntry.grid(row = 8, column = 1, pady = 10, sticky = NW, padx = 50 )

        celSym = Label(window, text ="°C", font = ("Helvetica", 16), bg="Pink", fg="white")
        celSym.grid(row = 4, column = 2, pady = 0, sticky = NW)

        fahSym = Label(window, text ="°F", font = ("Helvetica", 16), bg="Pink", fg="white")
        fahSym.grid(row = 6, column = 2, pady = 0, sticky = NW)

        kelSym = Label(window, text ="°K", font = ("Helvetica", 16), bg="Pink", fg="white")
        kelSym.grid(row = 8, column = 2, pady = 0, sticky = NW)

        convertButton =Button (window, text = "CONVERT", font = ("Helvetica", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="white", command = convert)
        convertButton.grid(row = 9, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx= 20)

        resetButton = Button (window, text = "RESET", font = ("Helvetica", 8, "bold"), relief = RAISED, bd=5, justify = CENTER,  overrelief = GROOVE, activebackground = "red", activeforeground="white", command = reset)
        resetButton.grid(row = 10, column = 1,ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 20)
        
        self.backbtn = Button(window, text="←", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "blue", activeforeground="white", command=back_btn)
        self.backbtn.grid(column=1, row = 1, sticky = W)

    def back_buttoncmd(self):
        from app2 import App
        self.window.destroy()
        App()
 


 # Open temperature conversion

    def open_temp(self):
        self.window.destroy()
        self.TemperatureConverter()
    

 # Open length conversion

    def open_len(self):
        self.window.destroy()
        self.LengthConverter()

# Open weight conversion
    
    def open_weigh(self):
        self.window.destroy()
        self.WeightConverter()
    
           

    

