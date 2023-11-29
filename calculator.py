from tkinter import *

class CalcGUI:

    def _init_(self, window):
        self.window = window
        window.title("Scientific Calculator")

        self.equation_text = Entry(window, width=36, borderwidth=5)
        self.equation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.setup_buttons()

    def setup_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            Button(self.window, text=text, width=9, command=lambda val=text: self.on_click(val)) \
                .grid(row=row, column=col)

    def on_click(self, value):
        current = self.equation_text.get()

        if value == 'C':
            self.equation_text.delete(0, END)
        elif value == '=':
            try:
                result = str(eval(current))
                self.equation_text.delete(0, END)
                self.equation_text.insert(0, result)
            except Exception as e:
                self.equation_text.delete(0, END)
                self.equation_text.insert(0, 'Error')
        else:
            self.equation_text.delete(0, END)
            self.equation_text.insert(0, current + value)

if __name__ == '__main__':
    root = Tk()
    app = CalcGUI(root)
    root.mainloop()