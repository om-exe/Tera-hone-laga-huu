from tkinter import Tk, Label
from datetime import datetime

root = Tk()
root.title('Date and Time')

label = Label(root, text=datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p'), font=('Calibri', 20))
label.pack(pady=20)

root.mainloop()
