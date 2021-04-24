from tkinter import *
a = Tk()
a.geometry("300x300")
sbr = Scrollbar(
    a,
)
sbr.pack(side=RIGHT,fill="y")
a.title("hello world")

s =Listbox(a,font = ("verdana",10))
s.insert(1, 'Demo1')
s.insert(2, 'Demo2')
s.insert(3, 'Demo3')
s.insert(4, 'Demo4')

s.pack(side=LEFT,fill="both",expand=True)
for data in range(40):
    s.insert(data,"Demo "+str(data+1))

sbr.config(command=s.yview)
s.config(yscrollcommand=sbr.set)
a.mainloop()