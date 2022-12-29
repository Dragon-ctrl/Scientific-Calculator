import tkinter as tk
calcuWindow = tk.Tk()
calcuWindow.title("Calculator")

calcuWindow.geometry('400x600')
calcuWindow.maxsize(400, 600)
calcuWindow.minsize(400, 600)

calcuEntry = tk.Entry(calcuWindow, width=35, borderwidth=5, bg='#bfb2b2')
calcuEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

navigationDrawer = tk.Frame(calcuWindow, width=200, height=600, relief='groove', bg='#4c4d4f')
navigationDrawer.grid(row=0, column=4, rowspan=8)

tabBar = tk.Frame(calcuWindow, width=400, height=60, relief='solid', bg='#4c4d4f')
tabBar.grid(row=8, column=0, columnspan=4)

def button_click(number):
    current = calcuEntry.get()
    calcuEntry.delete(0, tk.END)
    calcuEntry.insert(0, str(current) + str(number))

def button_clear():
    calcuEntry.delete(0, tk.END)

def button_add():
    first_number = calcuEntry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    calcuEntry.delete(0, tk.END)

def button_subtract():
    first_number = calcuEntry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    calcuEntry.delete(0, tk.END)

def button_multiply():
    first_number = calcuEntry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    calcuEntry.delete(0, tk.END)

def button_divide():
    first_number = calcuEntry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    calcuEntry.delete(0, tk.END)

def button_sqrt():
    first_number = calcuEntry.get()
    global math
    math = "sqrt"
    f_num = int(first_number)
    calcuEntry.delete(0, tk.END)

def button_equal():
    second_number = calcuEntry.get()
    calcuEntry.delete(0, tk.END)

    if math == "addition":
        calcuEntry.insert(0, f_num + int(second_number))
    elif math == "subtraction": 
        calcuEntry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        calcuEntry.insert(0, f_num * int(second_number))
    elif math == "division":
        calcuEntry.insert(0, f_num / int(second_number))
    elif math == "sqrt":
        calcuEntry.insert(0, f_num ** (1/2))

button_1 = tk.Button(calcuWindow, text="1", padx=40, pady=20, command=lambda: button_click(1), bg='#bfb2b2')
button_2 = tk.Button(calcuWindow, text="2", padx=40, pady=20, command=lambda: button_click(2), bg='#bfb2b2')
button_3 = tk.Button(calcuWindow, text="3", padx=40, pady=20, command=lambda: button_click(3), bg='#bfb2b2')
button_4 = tk.Button(calcuWindow, text="4", padx=40, pady=20, command=lambda: button_click(4), bg='#bfb2b2')
button_5 = tk.Button(calcuWindow, text="5", padx=40, pady=20, command=lambda: button_click(5), bg='#bfb2b2')
button_6 = tk.Button(calcuWindow, text="6", padx=40, pady=20, command=lambda: button_click(6), bg='#bfb2b2')
button_7 = tk.Button(calcuWindow, text="7", padx=40, pady=20, command=lambda: button_click(7), bg='#bfb2b2')
button_8 = tk.Button(calcuWindow, text="8", padx=40, pady=20, command=lambda: button_click(8), bg='#bfb2b2')
button_9 = tk.Button(calcuWindow, text="9", padx=40, pady=20, command=lambda: button_click(9), bg='#bfb2b2')
button_0 = tk.Button(calcuWindow, text="0", padx=40, pady=20, command=lambda: button_click(0), bg='#bfb2b2')
button_add = tk.Button(calcuWindow, text="+", padx=39, pady=20, command=button_add, bg='#4c4d4f', fg='#bfb2b2')
button_subtract = tk.Button(calcuWindow, text="-", padx=40, pady=20, command=button_subtract, bg='#4c4d4f', fg='#bfb2b2')
button_multiply = tk.Button(calcuWindow, text="*", padx=40, pady=20, command=button_multiply, bg='#4c4d4f', fg='#bfb2b2')
button_divide = tk.Button(calcuWindow, text="/", padx=40, pady=20, command=button_divide, bg='#4c4d4f', fg='#bfb2b2')
button_sqrt = tk.Button(calcuWindow, text="√", padx=40, pady=20, command=button_sqrt, bg='#4c4d4f', fg='#bfb2b2')
button_equal = tk.Button(calcuWindow, text="=", padx=91, pady=20, command=button_equal, bg='#4c4d4f', fg='#bfb2b2')
button_clear = tk.Button(calcuWindow, text="Clear", padx=79, pady=20, command=button_clear, bg='#4c4d4f', fg='#bfb2b2')

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_sqrt.grid(row=7, column=0)

calcuWindow.mainloop()
