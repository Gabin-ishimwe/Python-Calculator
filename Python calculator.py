from tkinter import *

root = Tk()
root.title("Calculator")

insert = Entry(root, width=40, borderwidth=5)
insert.grid(column=0, row=0, columnspan=4)

def click(num):
    current = insert.get()
    insert.delete(0, END)
    global first_number
    first_number = insert.insert(0, str(current) + str(num))

def clear():
    insert.delete(0, END)

def add():
    global f_num
    global math
    math = "addition"
    f_num = int(insert.get())
    insert.delete(0, END)

def equal():
    s_num = int(insert.get())
    insert.delete(0, END)
    global math
    if math == "addition":
        insert.insert(0, f_num + s_num)

    elif math == "substraction":
        insert.insert(0, f_num - s_num)

    elif math == "division":
        insert.insert(0, f_num / s_num)

    elif math == "multiplication":
        insert.insert(0, f_num * s_num)

def substract():
    global math
    global f_num
    math = "substraction"
    f_num = int(insert.get())
    insert.delete(0, END)

def multiplication():
    global math
    global f_num
    math = "multiplication"
    f_num = int(insert.get())
    insert.delete(0, END)

def division():
    global math
    global f_num
    math = "division"
    f_num = int(insert.get())
    insert.delete(0, END)


button_1 = Button(root, text="1", command=lambda:click(1), padx=20, pady=20)
button_2 = Button(root, text="2", command=lambda: click(2), padx=20, pady=20)
button_3 = Button(root, text="3", command=lambda : click(3), padx=20, pady=20)
button_4 = Button(root, text="4", command=lambda : click(4), padx=20, pady=20)
button_5 = Button(root, text="5", command=lambda :click(5), padx=20, pady=20)
button_6 = Button(root, text="6", command=lambda : click(6), padx=20, pady=20)
button_7 = Button(root, text="7", command=lambda : click(7), padx=20, pady=20)
button_8 = Button(root, text="8", command=lambda : click(8), padx=20, pady=20)
button_9 = Button(root, text="9", command=lambda: click(9), padx=20, pady=20)
button_0 = Button(root, text="0", command=lambda: click(0), padx=20, pady=20)
button_multiply = Button(root, text="x", command=multiplication, padx=20, pady=20)
button_substract = Button(root, text="-", command=substract, padx=20, pady=20)
button_add = Button(root, text="+", command=add, padx=20, pady=20)
button_equal = Button(root, text="=", command=equal, padx=20, pady=20)
button_clear = Button(root, text="clear", command=clear, padx=42, pady=20)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_substract.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=4, column=3)

root.mainloop()
