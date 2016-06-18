s = "Results:\n"

y = 63.5 # example 1
s += str(type(y)) + "\n"

s += str(type(str(y))) + "\n"

s += str(type(str(3.14))) + "\n"

s += str(type(str(7.12))) + "\n"

s += str('Python Programming ' + str(3) + " units") + "\n"

s += str('Python Programming ' + repr(3) + " units") + "\n"

str1 = "Welcome To Python"  # example 2
s += str(str1.upper()) + "\n"

s += str(str1.lower()) + "\n"

str1 = "Welcome To python" # Example 3
s += str(str1.upper()) + "\n"
s += str(str1.lower()) + "\n"

s += str(type(True)) + "\n" # Example 4
s += str(type(False)) + "\n"
s += str(3 >2) + "\n"

x = 5
s += str(x < 4) + "\n"
s += str(type(x)) + "\n"

x = 5
y = (x < 4)
s += str(type(y)) + "\n"

w = "D901"
s += str(w.isalpha()) + "\n"

###### Message Box Code ######
from tkinter import *

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
