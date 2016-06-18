s = "Result:\n"

x = 2 # example 1
s += str(type(2)) + "\n"

x = "Python"
s += str(type(x)) + "\n"

x = (9, 8, 7, 6)
s += str(type(x)) + "\n"
x = 0 # example 2
s += str(x) + "\n"

x = "Hello"
s += str(x) + "\n"

x = [1, 2, 3]
s += str(x) + "\n"

tuple1 = (3.14e-10, 5.07E210, 5.07e+210)
s += str(tuple1) + "\n" # example 3

tuple2 = (0b1111100, 0o174, 0x7c)
s += str(tuple2) + "\n"

tuple3 = (1, 10, 100)
s += str(tuple3) + "\n"

tuple4 = (0b1 , 0b10, 0b100)
s += str(tuple4) + "\n"

tuple5 = (0o1, 0o10, 0o100)
s += str(tuple4) + "\n"

tuple6 = (0x01, 0x10, 0xFF)
s += str(tuple6) + "\n"
s += str(0XFF == 0Xff == 0XFf == 0XfF) + "\n" # example 4

tuple7 = (0b1011, 0B1011)
s += str(tuple7) + "\n"

tuple8 = (0o177, 0O177)
s += str(tuple8) + "\n"

tuple9 = (0x9ff, 0X9ff)
s += str(tuple9) + "\n"
s += str(5.07e+210 == 5.07e210) + "\n"
s += str(5.07e+210 == 5.07E210) + "\n"


###### Message Box Code ######
from tkinter import *

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()