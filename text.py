from tkinter import *
a = Tk()

tx = Text(a,height=10,width=20)
tx.pack()

tx.insert(END,'Hello From Tkinter')

a.mainloop()