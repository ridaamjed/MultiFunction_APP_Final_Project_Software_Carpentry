import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from utils.calcu import Calculator
import re

class Notepad:
    def __init__(self):

# Initialize the main window

        self.window = tk.Tk()
        self.window.title("Notes")
        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(1,  weight = 1)
        self.window.geometry("375x667")

# Create the layout and buttons

        self.create_layout()
        self.create_buttons()
        self.result = []
        self.result1 = ""
        

    def create_layout(self):

# Create the text editor and button frame

        self.txt_editor = tk.Text(self.window, font = "Verdana", bg="Pink", fg="Black", insertbackground="Black")
        self.button_frame = tk.Frame(self.window, relief = tk.RAISED, bd = 2, bg="Pink")

# Grid layout for the text editor and button frame

        self.txt_editor.grid(row = 0, column = 1, sticky = "NSEW")
        self.button_frame.grid(row = 0, column = 0, sticky = "NS")

    def create_buttons(self):

# Create buttons for opening, saving, and going back

        self.openfile_button = tk.Button(self.button_frame, text = "Open", command = self.open_file, bg="Pink", fg="White")
        self.savefile_button = tk.Button(self.button_frame, text = "Save As", command = self.save_file, bg="Pink", fg="White")
        self.backbtn = tk.Button(self.button_frame, text="←", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = tk.RAISED, bd=5, justify = tk.CENTER, overrelief = tk.GROOVE, activebackground = "blue", activeforeground="white", command=self.back_btn)
        self.Evaluatebtn = tk.Button(self.button_frame, text="Eval", bg="Pink" , fg="white",font = ("Helvetica", 10, "bold"), relief = tk.RAISED, bd=5, justify = tk.CENTER, overrelief = tk.GROOVE, activebackground = "blue", activeforeground="white", command=self.evaluate_exp)
        self.Convertbtn = tk.Button(self.button_frame, text="Conv", bg="Pink" , fg="white",font = ("Helvetica", 10, "bold"), relief = tk.RAISED, bd=5, justify = tk.CENTER, overrelief = tk.GROOVE, activebackground = "blue", activeforeground="white", command=self.convert_exp)

# Grid layout for the buttons

        self.openfile_button.grid(row = 1, column = 0, sticky = "EW", padx = 5, pady = 5)
        self.savefile_button.grid(row = 2, column = 0, sticky = "EW", padx = 5)
        self.backbtn.grid(row = 0, column = 0, sticky = "EW", padx = 5, pady = 5)
        self.Evaluatebtn.grid(row = 3, column = 0, sticky = "EW", padx = 5, pady = 5)
        self.Convertbtn.grid(row = 4, column = 0, sticky = "EW", padx = 5, pady = 5)

        
        

    def open_file(self):

# Open a file dialog to select a file for opening
        
        self.filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
     )
        if not self.filepath:
            return

# Clear the text editor and insert the content of the selected file

        self.txt_editor.delete("1.0", tk.END)
        with open(self.filepath, mode="r", encoding="utf-8") as input_file:
            self.text = input_file.read()
            self.txt_editor.insert(tk.END, self.text)

# Update the window title with the file path

        self.window.title(f"My Notes - {self.filepath}")
    
    
# Evaluate all the mathematical expressions in the notepad

    def evaluate_exp(self):


        
        # self.text1 = self.txt_editor.get("1.0", tk.END).splitlines()
        # self.txt_editor.delete("1.0", tk.END)

        # for text1 in self.text1:
            # self.result1 = str(eval(text1))
            # self.result.append(self.result1)
            # self.txt_editor.insert(tk.END, self.text1)
        expressions = self.txt_editor.get("1.0", tk.END).splitlines()
    
    # Clear the notepad
        self.txt_editor.delete("1.0", tk.END)

    # Initialize an empty list to store results
        results = []

    # Evaluate each expression and store the result
        for expression in expressions:
            try:
                result = str(eval(expression))
                results.append(result)
            except Exception as e:
                results.append(f"Error: {str(e)}")

    # Display the results on the notepad
        for result in results:
            self.txt_editor.insert(tk.END, f"{result}\n")

    # Converts an expression from one unit to another.
    
    def convert_exp(self):

        flag_l = False
        flag_n = False
        self.factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
        self.factors2 = {'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
        results = []


        expression = self.txt_editor.get("1.0", tk.END)
        self.txt_editor.delete("1.0", tk.END)

        match = re.search(r'(\d*\.?\d+)([a-zA-Z]+)', expression)

        if match:
            amount, unit = match.groups()
            amt = float(amount)
            if self.factors.get(unit) != None:
                amt = amt * self.factors[unit]
                
                results = []
                for target_unit, factor in self.factors.items():
                    converted_amt = amt / factor
                    results.append(f"{converted_amt} {target_unit}")

                    
                
            else:
                amt = amt * self.factors2[unit]
                

                results = []
                for target_unit, factor in self.factors2.items():
                    converted_amt = amt / factor
                    results.append(f"{converted_amt} {target_unit}")

            for result in results:
                self.txt_editor.insert(tk.END, f"{result}\n")
                
                
        # expression = self.txt_editor.get("1.0", tk.END)
        # val=re.search('[a-zA-Z]', expression)
        # numberstring=expression[0:val[0]]
        
        # amt = amt * self.factors[val[0]]
        # for i in self.factors:
            # try:
                # results.append(amt / self.factors[i])
            # except Exception as e:
                # results.append(f"Error: {str(e)}")
                        
        # for result in results:
            # self.txt_editor.insert(tk.END, f"{result}\n")
               
        

        


                        
            




        
    def save_file(self):

# Open a file dialog to select a file for saving

        self.filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not self.filepath:
            return

# Write the content of the text editor to the selected file

        with open(self.filepath, mode="w", encoding="utf-8") as output_file:
            self.text = self.txt_editor.get("1.0", tk.END)
            output_file.write(self.text)

# Update the window title with the file path

        self.window.title(f"My Notes - {self.filepath}")
        
    def back_btn(self):

# Close the current window and go back to the main application window

        from utils.app2 import App
        self.window.destroy()
        App()
        
        

    


