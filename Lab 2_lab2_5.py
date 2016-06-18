import InputBox
import MessageBox

# Example 1 - list
r = "Result:"
print(r)

a = [3, 6, 9]
print(a)

b = ['A', 'B', 'C', 'D']
print(b)

c = ['Python', 3.4, True]
print(c)

# example 3 - tuple
t1 = (3, 6, 9)
print(t1)

t2 = ('A', 'B', 'C', 'D')
print(t2)

t3 = ('Python', 3.4, True)
print(t3)

# Example 3 - dict
d = {'OH': "Ohio", 'TX': "Texass"}
print(d)

# Example 4
ans = []  # empty list

InputBox.ShowDialog("What is your full name?")
fullname = InputBox.GetInput()
InputBox.ShowDialog("What is your major?")
major = InputBox.GetInput()
InputBox.ShowDialog('What is the current temp in Fahrenheit?')
f = InputBox.GetInput()

ans.append(fullname)
ans.append(major)
ans.append(f)

# C = (f-32)*(5/9)
x = 'It is', (float(f) - 32) * (5/9), 'degrees in Celsius'
print(x)


MessageBox.Show(str(r) + "\n" + str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(t1) + "\n" + str(t2) +
                "\n" + str(t3) + "\n" + str(d) + "\n" + str(x))
