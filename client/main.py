from tkinter import *

from utils.database_utils import *

class RootWindow:
	def __init__(self, win):
		
		self.diagnose_button = Button(win, text="Diagnose", command = self.diagnose_window).pack(side = TOP, pady = (win.winfo_reqheight() / 5, win.winfo_reqheight() / 10))
		self.records_button = Button(win, text="Records").pack(side = TOP, pady = win.winfo_reqheight() / 10)
		self.settings_button = Button(win, text="Diagnose").pack(side = TOP, pady = win.winfo_reqheight() / 10)
	
	def diagnose_window(self):
		diagnosis_header = Tk()
		diagnosis_win = DiagnosticsWindow(diagnosis_header)

		diagnosis_header.title("New Diagnosis")
		diagnosis_header.geometry("800x350+10+10")
		
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

class TemperatureWindow(Toplevel):

	def __init__(self, win):
		Toplevel.__init__(self, win)

		self.temperature = None
		self.title_text = Label(self, text = "Enter Temperature in °C").grid(row = 0, column = 0, columnspan = 2, sticky = N, pady = (self.winfo_reqwidth() / 5, self.winfo_reqwidth() / 10))
		self.temperature_celcius_entry = Entry(self)
		self.temperature_celcius_entry.grid(row = 1, column = 0, sticky = N + W + E, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 5)
		self.temperature_celcius_label = Label(self, text = "°C").grid(row = 1, column = 1, sticky = N + W + E, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 5)
		self.store_temterature_button = Button(self, text = "OK", command = self.on_ok)
		
		self.store_temterature_button.grid(row = 2, column = 0, columnspan = 2, sticky = N + W + E, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 5)
		
		# self.temperature_celcius_entry.bind("<Button-1>", self.on_ok)
		# self.temperature_celcius_entry.bind("<Return>", self.on_ok)
	


	def show(self):
		self.wm_deiconify()
		self.temperature_celcius_entry.focus_force()
		self.wait_window()
		return self.temperature

	def on_ok(self, event=None):
		self.temperature = str(self.temperature_celcius_entry.get())
		self.destroy()
		
class DiagnosticsWindow(Frame):
	name = None
	diagnostics = {"symptoms": None, "temperature": None, "countries_visited": None}

	def __init__(self, win):
		Frame.__init__(self, win)

		self.name_text = Label(win, text = "Name").grid(row = 1, column = 0, columnspan = 2, sticky = N+E+W, padx = win.winfo_reqwidth() / 5)
		self.name_input = Entry(win).grid(row = 1, column = 2, columnspan = 2, sticky = N+E, padx = win.winfo_reqwidth() / 5)
		
		self.build_symptoms_row(win)

		self.build_temperature_row(win)

		self.build_countries_visited_row(win)
		
	def build_symptoms_row(self, win):
		self.symptoms_prefix = Label(win, text = self.generate_prefix("symptoms"))
		self.symptoms_prefix.grid(row = 2, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_text = Label(win, text = "Symptoms")
		self.symptoms_text.grid(row = 2, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_status = Label(win, text = self.generate_status("symptoms"))
		self.symptoms_status.grid(row = 2, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_edit = Button(win, text = "Edit")
		self.symptoms_edit.grid(row = 2, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

	def build_temperature_row(self, win):
		self.temperature_prefix = Label(win, text = self.generate_prefix("temperature"))
		self.temperature_prefix.grid(row = 3, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.temperature_text = Label(win, text = "Temperature")
		self.temperature_text.grid(row = 3, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.temperature_status = Label(win, text = self.generate_status("temperature"))
		self.temperature_status.grid(row = 3, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.temperature_edit = Button(win, text = "Edit", command = self.get_temperature)
		self.temperature_edit.grid(row = 3, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

	def build_countries_visited_row(self, win):
		self.countries_visited_prefix = Label(win, text = self.generate_prefix("countries_visited"))
		self.countries_visited_prefix.grid(row = 4, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.countries_visited_text = Label(win, text = "Cuntries Visited")
		self.countries_visited_text.grid(row = 4, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.countries_visited_status = Label(win, text = self.generate_status("countries_visited"))
		self.countries_visited_status.grid(row = 4, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.countries_visited_edit = Button(win, text = "Edit")
		self.countries_visited_edit.grid(row = 4, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

	def generate_prefix(self, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return ""
		else:
			prefix = self.diagnostics[diagnostic]
			if diagnostic == "temperature":
				farenheit = float(self.diagnostics[diagnostic]) * 1.8 + 32
				return self.diagnostics[diagnostic] + " °C | " + ("%.2f" % farenheit ) + " °F"
			else:
				return str(len(self.diagnostics[diagnostic])) + " Selected"
			
	def generate_status(self, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return "X"
		else:
			return "✓"

	def get_temperature(self):
		self.diagnostics["temperature"] = TemperatureWindow(self).show()

		self.temperature_prefix.config(text = self.generate_prefix("temperature"))
		self.temperature_status.config(text = self.generate_status("temperature"))
	
	


root_header = Tk()
root_win = RootWindow(root_header)

root_header.title("Dengue Diagnosis Assistant")
root_header.geometry("600x400+10+10")
root_header.mainloop()
