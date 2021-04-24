from tkinter import *
a = Tk()
a.geometry("200x200")

msg ='Hello From Tkinter'
i = Message(a,text = msg,bg='gray')

i.pack()
a.mainloop()