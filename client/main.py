from tkinter import *

from utils.database_utils import *

class RootWindow:
	def __init__(self, win):
		# self.title_text = Label(win, text = "Dengue Diagnosis Assistant").pack(side = TOP, pady = 10)
		self.diagnose_button = Button(win, text="Diagnose", command = self.diagnose_window).pack(side = TOP, pady = 10)
		self.records_button = Button(win, text="Records").pack(side = TOP, pady = 10)
		self.settings_button = Button(win, text="Diagnose").pack(side = TOP, pady = 10)
	
	def diagnose_window(self):
		diagnosis_header = Tk()
		diagnosis_win = DiagnosticsWindow(diagnosis_header)

		diagnosis_header.title("New Diagnosis")
		diagnosis_header.geometry("600x350+10+10")
		
		Grid.columnconfigure(diagnosis_header, 0, weight=1)
		Grid.columnconfigure(diagnosis_header, 1, weight=2)
		Grid.columnconfigure(diagnosis_header, 2, weight=2)
		Grid.columnconfigure(diagnosis_header, 3, weight=2)
		Grid.rowconfigure(diagnosis_header, 0, weight=1)
		Grid.rowconfigure(diagnosis_header, 1, weight=3)
		Grid.rowconfigure(diagnosis_header, 2, weight=3)
		Grid.rowconfigure(diagnosis_header, 3, weight=3)
		Grid.rowconfigure(diagnosis_header, 4, weight=3)
		
		diagnosis_header.mainloop()

class TemperatureWindow:
	temperature = None

	def __init__(self):
		pass

class DiagnosticsWindow:
	name = None
	diagnostics = {"symptoms": None, "temperature": None, "countries_visited": None}

	def __init__(self, win):
		# self.title_text = Label(win, text = "New Diagnosis").grid(row = 0, column = 0, columnspan = 4, sticky = N, pady = 15)

		self.name_text = Label(win, text = "Name").grid(row = 1, column = 0, columnspan = 2, sticky = N+E+W, padx = win.winfo_reqwidth() / 5)
		self.name_input = Entry(win).grid(row = 1, column = 2, columnspan = 2, sticky = N+E, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_prefix = Label(win, text = self.generate_prefix(win, "symptoms")).grid(row = 2, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.symptoms_text = Label(win, text = "Symptoms").grid(row = 2, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.symptoms_status = Label(win, text = self.generate_status(win, "symptoms")).grid(row = 2, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.symptoms_edit = Button(win, text = "Edit").grid(row = 2, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

		self.temperature_prefix = Label(win, text = self.generate_prefix(win, "temperature")).grid(row = 3, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.temperature_text = Label(win, text = "Temperature").grid(row = 3, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.temperature_status = Label(win, text = self.generate_status(win, "temperature")).grid(row = 3, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.temperature_edit = Button(win, text = "Edit").grid(row = 3, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

		self.countries_visited_prefix = Label(win, text = self.generate_prefix(win, "countries_visited")).grid(row = 4, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.countries_visited_text = Label(win, text = "Cuntries Visited").grid(row = 4, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.countries_visited_status = Label(win, text = self.generate_status(win, "countries_visited")).grid(row = 4, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		self.countries_visited_edit = Button(win, text = "Edit").grid(row = 4, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

	def generate_prefix(self, win, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return ""
		else:
			prefix = self.diagnostics[diagnostic]
			if diagnostic == "temperature":
				farenheit = int(self.diagnostics[diagnostic]) * 1.8 + 32
				return self.diagnostics[diagnostic] + " °C | " + str(farenheit) + " °F"
			else:
				return str(len(self.diagnostics[diagnostic])) + " Selected"
			
	def generate_status(self, win, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return "X"
		else:
			return "✓"

root_header = Tk()
root_win = RootWindow(root_header)

root_header.title("Dengue Diagnosis Assistant")
root_header.geometry("800x600+10+10")
root_header.mainloop()

