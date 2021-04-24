from tkinter import *
a = Tk()

b = Button(a,text="this is button widget",fg='green')

b.pack()
a.title('hello world')
a.geometry("400x400+20+60")
a.mainloop()