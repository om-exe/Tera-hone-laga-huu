from tkinter import *
root=Tk()
root.geometry("350x100")
Label(root,text="Programming Language",font=40).pack()
Button(root,text="Python",fg="blue").pack(side=LEFT)
Button(root,text="Java",fg="red").pack(side=RIGHT)
root.mainloop()
