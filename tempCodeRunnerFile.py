import tkinter as tk
from tkinter import messagebox

def calculate(symbol):
    try:
        int1 = int(int1_entry.get())
        int2 = int(int2_entry.get())
        float1 = float(int1)
        float2 = float(int2)
        
        switcher = {
            "+": f"The sum of the two numbers is: {int1 + int2}",
            "-": f"The difference of the two numbers is: {int1 - int2}",
            "*": f"The product of the two numbers is: {int1 * int2}",
            "/": f"The quotient of the two numbers is: {float1 / float2}" if float2 != 0 else "Division by zero is not allowed",
        }
        
        result = switcher.get(symbol, "Invalid symbol")
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
int1_entry = tk.Entry(root)
int1_entry.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
int2_entry = tk.Entry(root)
int2_entry.grid(row=1, column=1)

tk.Label(root, text="Choose an operation:").grid(row=2, column=0)
tk.Button(root, text="+", command=lambda: calculate("+")).grid(row=3, column=0)
tk.Button(root, text="-", command=lambda: calculate("-")).grid(row=3, column=1)
tk.Button(root, text="*", command=lambda: calculate("*")).grid(row=4, column=0)
tk.Button(root, text="/", command=lambda: calculate("/")).grid(row=4, column=1)

root.mainloop()