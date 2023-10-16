from tkinter import *
from tkcalendar import Calendar
import datetime

root = Tk()
root.geometry("1000x500")
x = datetime.datetime.now()
print(x)
lich = Calendar(root,font = ("Arial", 18), selectmode = 'day',
			year = x.year, month = x.month,
			day = x.day)
lich.pack(pady = 20)
root.mainloop()