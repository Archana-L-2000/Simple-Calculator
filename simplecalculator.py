from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=50, bg="#fff", fg="black", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
# define button


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global math
    global f_num
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num+int(second_number))
    if math == "subtraction":
        e.insert(0, f_num-int(second_number))
    if math == "multiplication":
        e.insert(0, f_num*int(second_number))
    try:
        if math == "division":
            e.insert(0, f_num/int(second_number))
    except: 
         e.insert(0,"Syntax Error")
        
    if (math == "multiplication" and (f_num and second_number == 0)):
        e.delete(0, END)
        e.insert(0, "0")
    if math == "division" and (f_num==0):
      
        e.delete(0, END)
        e.insert(0, "0")
def button_sub():
    first_number = e.get()

    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()

    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()

    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


Button_1 = Button(root, text="1", padx=45, pady=15, command=lambda: button_click(
    1), bg='lightblue', fg="black", activebackground='lightblue')
Button_2 = Button(root, text="2", padx=45, pady=15, command=lambda: button_click(
    2), bg='lightblue', fg="black", activebackground='lightblue')
Button_3 = Button(root, text="3", padx=45, pady=15, command=lambda: button_click(
    3), bg='lightblue', fg="black", activebackground='lightblue')
Button_4 = Button(root, text="4", padx=45, pady=15, command=lambda: button_click(
    4), bg='lightblue', fg="black", activebackground='lightblue')
Button_5 = Button(root, text="5", padx=45, pady=15, command=lambda: button_click(
    5), bg='lightblue', fg="black", activebackground='lightblue')
Button_6 = Button(root, text="6", padx=45, pady=15, command=lambda: button_click(
    6), bg='lightblue', fg="black", activebackground='lightblue')
Button_7 = Button(root, text="7", padx=45, pady=15, command=lambda: button_click(
    7), bg='lightblue', fg="black", activebackground='lightblue')
Button_8 = Button(root, text="8", padx=45, pady=15, command=lambda: button_click(
    8), bg='lightblue', fg="black", activebackground='lightblue')
Button_9 = Button(root, text="9", padx=45, pady=15, command=lambda: button_click(
    9), bg='lightblue', fg="black", activebackground='lightblue')
Button_0 = Button(root, text="0", padx=45, pady=15, command=lambda: button_click(
    0), bg='lightblue', fg="black", activebackground='lightblue')
Button_add = Button(root, text="+", padx=45, pady=15, command=button_add ,bg="indigo", fg="white")
Button_sub = Button(root, text="-", padx=45, pady=15, command=button_sub, bg="indigo", fg="white")
Button_mul = Button(root, text="*", padx=45, pady=15, command=button_mul, bg="indigo", fg="white")
Button_div = Button(root, text="/", padx=45, pady=15, command=button_div, bg="indigo", fg="white")
Button_equal = Button(root, text="=", padx=45, pady=15, command=button_equal, bg="indigo", fg="white")
Button_clear = Button(root, text="CLEAR", padx=85,
                      pady=15, command=button_clear , bg="red", fg="lightblue")
# put button on the screen

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=1)

Button_add.grid(row=4, column=2)

Button_sub.grid(row=4, column=0)
Button_mul.grid(row=5, column=0)
Button_div.grid(row=5, column=1)
Button_equal.grid(row=5, column=2)
Button_clear.grid(row=6, column=0, columnspan=3)
root.mainloop()
