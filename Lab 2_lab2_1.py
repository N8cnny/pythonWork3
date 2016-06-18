s = "Result:\n"

tuple1 = ("16.9", '37', "python", 'programming')
s += str(tuple1) + "\n"

tuple2 = (17, 44.5, 6.25e-23)
s += str(tuple2) + "\n"

# example 3
tuple3 = (type(2.1), id(2.1), type(47), type('apple'), type(True), type(None))
s += str(tuple3) + "\n"

# example 4
x = 2.1
s += str(type(x)) + "\n"
s += str(id(x)) + "\n"
y = "orange"
s += str(type(y)) + "\n"


###### Message Box Code ######
from tkinter import *

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()