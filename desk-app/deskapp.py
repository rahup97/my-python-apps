from tkinter import *

window = Tk()

def convert():
    kg = float(e1_value.get())
    t1.delete(0.0,END)
    t2.delete(0.0,END)
    t3.delete(0.0,END)
    grams = 1000*kg
    lb = 2.20462*kg
    on = 35.274*kg
    t1.insert(END, grams)
    t2.insert(END, lb)
    t3.insert(END, on)

l1 = Label(window, text = "Kg ->")
l1.grid(row = 1, column = 0)

b1 = Button(window, text = "Convert", command = convert)
b1.grid(row = 2, column = 1)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 1, column = 1)

t1 = Text(window, height = 1, width = 10)
t1.grid(row = 3, column = 0)
t2 = Text(window, height = 1, width = 10)
t2.grid(row = 3, column = 1)
t3 = Text(window, height = 1, width = 10)
t3.grid(row = 3, column = 2)


window = mainloop()
