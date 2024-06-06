from tkinter import *

root = Tk()

# Entry widget
e = Entry(root, width=35, bd=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(no):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + no)

def clear():
    e.delete(0, END)

def add():
    fno = e.get()
    global fnum
    global math
    math = "add"
    fnum = int(fno)
    e.delete(0, END)

def sub():
    fno = e.get()
    global fnum
    global math
    math = "sub"
    fnum = int(fno)
    e.delete(0, END)

def mul():
    fno = e.get()
    global fnum
    global math
    math = "mul"
    fnum = int(fno)
    e.delete(0, END)

def div():
    fno = e.get()
    global fnum
    global math
    math = "div"
    fnum = int(fno)
    e.delete(0, END)

def equal():
    sno = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fnum + int(sno))
    elif math == "sub":
        e.insert(0, fnum - int(sno))
    elif math == "mul":
        e.insert(0, fnum * int(sno))
    elif math == "div":
        if int(sno) != 0:
            e.insert(0, fnum / int(sno))
        else:
            e.insert(0, "Error")

# Button widgets
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: click("7"))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: click("8"))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: click("9"))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: click("4"))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: click("5"))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: click("6"))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: click("3"))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: click("2"))
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: click("1"))

button0 = Button(root, text='0', padx=40, pady=20, command=lambda: click("0"))
buttonplus = Button(root, text='+', padx=40, pady=20, command=add)
buttonsub = Button(root, text='-', padx=40, pady=20, command=sub)
buttonmul = Button(root, text='*', padx=40, pady=20, command=mul)
buttondiv = Button(root, text='/', padx=40, pady=20, command=div)
buttonclear = Button(root, text='clear', padx=40, pady=20, command=clear)
buttonequal = Button(root, text='=', padx=138, pady=20, command=equal)

# Place the buttons on the grid
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonplus.grid(row=4, column=1)
buttonsub.grid(row=4, column=2)

buttonmul.grid(row=5, column=0)
buttondiv.grid(row=5, column=1)
buttonclear.grid(row=5, column=2)

buttonequal.grid(row=6, column=0, columnspan=3)

# Start the main event loop
root.mainloop()
