# Write Python program to create application which use date n time in python
from tkinter import *
from tkinter.ttk import*
from time import strftime
root = Tk()
root.title('Clock')
from tkinter import *
import datetime as dt
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
lbl=Label(root,font=('calibri',40,'bold'),background='orange',foreground='white')
lbl.pack(anchor='center')
time()
mainloop()
def date():
    win=Tk()
    win.title("Display Current Date")
    win.geometry("700x250")
    date=dt.datetime.now()
    label=Label(win,text=f"{date:%A,%B%d,%y}",
                font="Calibri,20")
    label.pack(pady=20)
date()
mainloop()
# import _tkinter as tk
# from _tkinter import ttk
# from time import strftime
# from datetime import datetime

# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Clock and Date")
#         self.geometry("700x250")
#         self.create_widgets()

#     def create_widgets(self):
#         self.clock_label = ttk.Label(self, font=("Calibri", 40, "bold"), background="orange", foreground="white")
#         self.clock_label.pack(pady=20)
#         self.update_clock()

#         self.date_label = ttk.Label(self, text=datetime.now().strftime("%A, %B %d, %Y"), font=("Calibri", 20))
#         self.date_label.pack(pady=20)
#         self.update_date()

#     def update_clock(self):
#         self.clock_label.config(text=strftime("%H:%M:%S %p"))
#         self.after(1000, self.update_clock)

#     def update_date(self):
#         self.date_label.config(text=datetime.now().strftime("%A, %B %d, %Y"))
#         self.after(1000, self.update_date)

# if __name__ == "__main__":
#     app = Application()
#     app.mainloop()