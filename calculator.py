import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Professional Calculator")
        root.config(bg='#333333')  # Set background color to dark gray

        # Entry widget for displaying the input and result
        self.entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=5, relief="ridge", justify="right", bg='#666666', fg='white')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configure column and row weights to make the calculator resizable
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), bg='#555555', fg='white',
                      command=lambda b=button: self.button_click(b) if b != '=' else self.calculate()).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 12), bg='#AA0000', fg='white',
                  command=self.clear_entry).grid(row=row_val, column=col_val, sticky="nsew")

        # Configure the clear button to span two columns
        root.grid_columnconfigure(col_val, weight=1)

    def button_click(self, symbol):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + str(symbol))

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
