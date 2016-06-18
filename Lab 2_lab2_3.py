s = "Result:\n"

tuple1 = (oct(64), hex(64), hex(255)) # example 1
s += str(tuple1) + "\n"

tuple2 = (int('0100'), int('0100', 8), int('0x40', 16))
s += str(tuple2) + "\n"

tuple3 = (eval('100'), eval('0o100'), eval('0x40'))
s += str(tuple3) + "\n"

tuple4 = (1j * 1J, 2 + 1j * 3, (2+1j)*3, (3 + 5j) * (2 - 1j)) # example 2
s += str(tuple4) + "\n"
s += str('S1562') + "\n" # example 3

s += str("Classic Rap music") + "\n"

s += str('''Recyle the trash to save the earth''') + "\n"

s += str("""Bangladesh 101""") + "\n"

s += str('''Content-type: text/html
 <h1> Hello World </h1>
 Click <a href="http://www.python.org">here</a>.
 ''') + "\n"

s += str("Python" + " " + "programming") + "\n"

s += str(("Python", "3.5.1", "programming")) + "\n"

# example 4
x = "happy hours"
s += str(len(x)) + "\n"

tuple5 = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10])
s += str(tuple5) + "\n"

s += str(x[4]) + "\n"

s += str(x[len(x)-3]) + "\n"

s += str(x[0:5]) + "\n"

s += str(x[2:5]) + "\n"

s += str(x[:5]) + "\n"

s += str(x[6:]) + "\n"


###### Message Box Code ######
from tkinter import *

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
