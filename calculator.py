#Scientific-Calculator
# Importing all classes and functions from the tkinter module
from tkinter import *

# Define the CalcGUI class which will create the calculator interface
class CalcGUI:

    # Constructor to initialize the CalcGUI object
    def __init__(self, window):
        self.window = window  # Reference to the main window
        window.title("Scientific Calculator")  # Set the title of the window

        # Create an entry widget for displaying the equation
        self.equation_text = Entry(window, width=36, borderwidth=5)
        self.equation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.setup_buttons()  # Call method to setup buttons on the calculator

        

    # Method to setup the layout of buttons on the calculator
    def setup_buttons(self):
        # Define a list of tuples for button configurations (button text, row, column)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        # Loop to create and position buttons on the grid
        for (text, row, col) in buttons:
            Button(self.window, text=text, width=9, command=lambda val=text: self.on_click(val)) \
                .grid(row=row, column=col)

    # Method called when a button is clicked
    def on_click(self, value):
        current = self.equation_text.get()  # Get the current text in the entry widget

        if value == 'C':  # Clear the entry widget if 'C' is clicked
            self.equation_text.delete(0, END)
        elif value == '=':  # If '=' is clicked, evaluate the equation
            try:
                result = str(eval(current))  # Evaluate the expression and convert result to string
                self.equation_text.delete(0, END)  # Clear the entry widget
                self.equation_text.insert(0, result)  # Display the result
            except Exception as e:
                self.equation_text.delete(0, END)  # Clear the entry widget on error
                self.equation_text.insert(0, 'Error')  # Display error message
        else:
            # For other buttons, append their value to the entry widget
            self.equation_text.delete(0, END)
            self.equation_text.insert(0, current + value)

# This block runs if the script is the main program and not an imported module
if __name__ == '__main__':
    root = Tk()  # Create the main window
    app = CalcGUI(root)  # Instantiate CalcGUI with the main window
    root.mainloop()  # Start the event loop to run the application
