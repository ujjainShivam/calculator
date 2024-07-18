import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

entry = ttk.Entry(root, width=20, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: button_click(x)
    ttk.Button(root, text=button, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define delete function
def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])        

ttk.Button(root, text='C', command=clear).grid(row=5, column=0)
ttk.Button(root, text='Del', command=delete).grid(row=5, column=1)
ttk.Button(root, text='=', command=evaluate).grid(row=5, column=2, columnspan=2)

root.mainloop()

import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget
entry = ttk.Entry(root, width=20, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button click function
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Define clear function
def clear():
    entry.delete(0, tk.END)

# Define evaluate function
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: button_click(x)
    ttk.Button(root, text=button, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add clear and equal buttons
ttk.Button(root, text='C', command=clear).grid(row=5, column=0)
ttk.Button(root, text='=', command=evaluate).grid(row=5, column=1, columnspan=3)

# Run the main loop
root.mainloop()