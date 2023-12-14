import tkinter as tk
from tkinter import font

# Define some font constants

Large_Font =("Helvetica", 40)
Small_Arial = ("Helvetica", 16)
Digit_Font = ("Helvetica", 24)
Default_Font = ("Helvetica", 20)

# Define color constants

glacier = "#CDF0FF"
storm = "#004764"
black = "#000000"
lightblue = "#CCEDFF"
white = "#FFFFFF"
offwhite = "#F8FAFF"
pink = "#FFC0CB"

class Calculator:
    def __init__(self):

# Initialize the calculator window

        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Ridas Calculator")

# Initialize expression variables

        self.total_expression = ""
        self.current_expression = ""
        
# Initialize a list to store the history of calculations
        self.calculation_history = []


# Create the display frame and labels

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

# Define dictionaries for digits and operations

        self.digits ={
            7:(1, 1),8:(1, 2),9:(1, 3),
            4:(2, 1),5:(2, 2),6:(2, 3),
            1:(3, 1),2:(3, 2),3:(3, 3),
            0:(4, 2),'.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

# Create the buttons frame and configure rows and columns

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

# Create digit buttons, operator buttons, and special buttons

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        
    def create_special_buttons(self):

# Create special buttons: clear, equals, square root, square, and back

        self.create_clear_button()
        self.create_equals_button()
        self.create_sqrt_button()
        self.create_square_button()
        self.create_back_btn()
        self.create_history_btn()

    def create_display_labels(self):

# Create and pack total label and current label in the display frame

        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=black, fg=white, padx=24,font=Small_Arial)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=black, fg=white, padx=24,font=Large_Font)
        label.pack(expand=True, fill="both")

        return total_label, label     

    def create_display_frame(self):

# Create the display frame

        frame = tk.Frame(self.window, height=221, bg=pink)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_back_btn(self):

# Create the history button

        back = tk.Button(self.display_frame, text="Back", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = tk.RAISED, bd=5, anchor=tk.E, overrelief = tk.GROOVE, activebackground = "blue", activeforeground="white", command=self.back_btn)
        back.pack()
        
    def create_history_btn(self):

# Create the back button

        history1 = tk.Button(self.display_frame, text="History", bg="gray" , fg="white",font = ("Helvetica", 10, "bold"), relief = tk.RAISED, bd=5, anchor=tk.E, overrelief = tk.GROOVE, activebackground = "blue", activeforeground="white", command=self.show_history)
        history1.pack()

        
        
    def add_to_expression(self, value):

# Add a digit or '.' to the current expression and update the label

        self.current_expression += str(value)
        self.update_label()    

    def create_digit_buttons(self):

# Create digit buttons and grid them in the buttons frame

        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),bg=white,fg=black,font=Digit_Font,borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1],sticky=tk.NSEW)

    def append_operator(self, operator):

# Append an operator to the current expression, update total expression, and update labels

        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()        

    def create_operator_buttons(self):

# Create operator buttons and grid them in the buttons frame

        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=offwhite, fg=black, font=Default_Font, borderwidth=0, command= lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):

# Clear the current and total expressions, update labels

        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):

# Create the clear button

        button = tk.Button(self.buttons_frame, text="C", bg=offwhite, fg=black, font=Default_Font,borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def sqrt(self):

# Calculate the square root of the current expression and update the label

        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()    

    def create_sqrt_button(self):

# Create the square root button

        button = tk.Button(self.buttons_frame, text="\u221a", bg=offwhite, fg=black, font=Default_Font,borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square(self):

# Calculate the square of the current expression and update the label

        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
    
    def create_square_button(self):

# Create the square button

        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=offwhite, fg=black, font=Default_Font,borderwidth=0, command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW)           

    def evaluate(self):

# Evaluate the total expression, update current expression, total expression, and labels

        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.calculation_history.append((self.total_expression, self.current_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:        
            self.update_label()
        

            
    def show_history(self):
        # Display the history of calculations in a new window
        history_window = tk.Toplevel(self.window)
        history_window.title("Calculation History")
        
        # Create a label to display the history
        history_label = tk.Label(history_window, text="Calculation History", font=Default_Font)
        history_label.pack()
        
        # Create a text widget to display the history
        history_text = tk.Text(history_window, height=10, width=30, font=Default_Font)
        history_text.pack()
        
        # Insert each calculation into the text widget
        for index, (expression, result) in enumerate(self.calculation_history, 1):
            history_text.insert(tk.END, f"{index}. {expression} = {result}\n")
        
        # Make the text widget read-only
        history_text.config(state=tk.DISABLED)

    def create_equals_button(self):

# Create the equals button

        button = tk.Button(self.buttons_frame, text="=", bg=pink, fg=black, font=Default_Font,borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)  

    def create_buttons_frame(self):

# Create and return the frame for buttons with a specified background color

        frame = tk.Frame(self.window, bg=storm)
        frame.pack(expand=True, fill="both")
        return frame 

    def update_total_label(self):

# Update the total label with a formatted expression

        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):

# Update the label with the current expression, limiting the display to 11 characters

        self.label.config(text=self.current_expression[:11])
    
    def back_btn(self):

# Go back to the main application when the Back button is pressed

            from utils.app2 import App
            self.window.destroy()
            App()
        


