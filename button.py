import tkinter
from tkinter import *

m = tkinter.Tk()
c = Canvas(m,bg="red",height="200",width="300")

m.geometry("500x500+50+100")

m.title("home page")

b1 = Button(m, text="This is Button",fg = "red")
b2 = Button(m, text="Button2",fg = "blue")
c1 = Button(m, text="Button3",fg = "green")
c2 = Button(m, text="Button4",fg = "orange")

c.pack()
b1.pack(side = TOP)
b2.pack(side = RIGHT)
c1.pack(side = BOTTOM)
c2.pack(side = LEFT)


m.mainloop()