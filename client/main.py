from tkinter import *
from . import database_utils


class RootWindow:
	def __init__(self, win):
		self.diagnose = Button(win, text="Diagnose").pack(side = TOP, pady = 10)




top = Tk()
mainwin = RootWindow(top)

top.title("Dengue Diagnosis Assistant")
top.geometry("800x600+10+10")
top.mainloop()
