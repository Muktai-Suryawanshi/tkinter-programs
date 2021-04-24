from tkinter import *
a = Tk()
a.geometry("200x200")

a1 = Checkbutton(a,text="C")
a1.pack()

b = Checkbutton(a,text="C++")
b.pack()

c = Checkbutton(a,text="java")
c.pack()

d = Checkbutton(a,text="Python")
d.pack()

e = Checkbutton(a,text="submit")
e.pack()

a.mainloop()
