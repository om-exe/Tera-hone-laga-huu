# write a GUI program to design a app
# Different Fonts & colors
from tkinter import*
root=Tk()
root.geometry("350x100")
w=Label(root,text="Programming Language",font=40)
w.pack()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
b1_button=Button(frame,text="Python",fg="blue")
b1_button.pack(side=LEFT)

b2_button=Button(frame,text="Java",fg="blue")
b2_button.pack(side=LEFT)

b3_button=Button(frame,text="C++",fg="blue")
b3_button.pack(side=LEFT)

b4_button=Button(frame,text="HTML",fg="blue")
b4_button.pack(side=BOTTOM)

b5_button=Button(frame,text="CSS",fg="blue")
b5_button.pack(side=BOTTOM)
