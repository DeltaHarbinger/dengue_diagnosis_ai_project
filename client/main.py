from tkinter import *
from tkinter import ttk

from utils.database_utils import *

class RootWindow:
	def __init__(self, win):
		
		self.diagnose_button = Button(win, text="Diagnose", command = self.diagnose_window).pack(side = TOP, pady = (win.winfo_reqheight() / 5, win.winfo_reqheight() / 10))
		self.records_button = Button(win, text="Records", command = self.records_window).pack(side = TOP, pady = win.winfo_reqheight() / 10)
		self.settings_button = Button(win, text="Diagnose").pack(side = TOP, pady = win.winfo_reqheight() / 10)
	
	def records_window(self):
		records_header = Tk()
		records_win = RecordsWindow(records_header)
		records_header.title("Diagnosis Records")
		records_header.geometry("800x400+10+10")

		records_header.mainloop()

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

class SymptomsWindow(Toplevel):

	def __init__(self, win):
		self.symptoms = [{"id": s["id"], "name": s["name"]} for s in get_all_symptoms()]
		self.symptoms = sorted(self.symptoms, key = lambda s: (s["name"]))
		self.selected = [BooleanVar() for x in self.symptoms]
		
		Toplevel.__init__(self, win)

		self.build_symptom_rows(self.symptoms)

		self.confirm_button = Button(self, text="Ok", command=self.destroy)
		self.confirm_button.grid(row = len(self.symptoms), column = 0, columnspan = 2, sticky = N + W + E, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 5)


	def build_symptom_rows(self, symptoms):
		for i, symptom in enumerate(self.symptoms):
			self.build_symptom_selection(i, symptom)

	def build_symptom_selection(self, i, symptom):
		Label(self, text = symptom["name"]).grid(row = i, column = 0, pady = self.winfo_reqheight() / 10, padx = (self.winfo_reqwidth() / 10, self.winfo_reqwidth() / 2))
		Checkbutton(self, command=lambda: self.toggle_selected(i)).grid(row = i, column = 1, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 10)

	def toggle_selected(self, i):
		self.selected[i].set(not (self.selected[i].get()))

	def show(self):
		self.wm_deiconify()
		self.wait_window()
		return [symptom for i, symptom in enumerate(self.symptoms) if self.selected[i].get()]

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

	def show(self):
		self.wm_deiconify()
		self.temperature_celcius_entry.focus_force()
		self.wait_window()
		return self.temperature

	def on_ok(self, event=None):
		self.temperature = str(self.temperature_celcius_entry.get())
		self.destroy()

class CountriesVisitedWindow(Toplevel):
	def __init__(self, win):
		self.countries = [{"id": c["id"], "country_name": c["country_name"], "country_code": c["country_code"]} for c in get_all_countries()]
		self.countries = sorted(self.countries, key = lambda c: (c["country_name"]))
		self.selected = [BooleanVar() for x in self.countries]
		
		Toplevel.__init__(self, win)

		self.build_country_rows(self.countries)

		self.confirm_button = Button(self, text="Ok", command=self.destroy)
		self.confirm_button.grid(row = len(self.countries), column = 0, columnspan = 2, sticky = N + W + E, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 5)

	def build_country_rows(self, countries):
		for i, country in enumerate(self.countries):
			self.build_country_selection(i, country)

	def build_country_selection(self, i, country):
		Label(self, text = country["country_name"]).grid(row = i, column = 0, pady = self.winfo_reqheight() / 10, padx = (self.winfo_reqwidth() / 10, self.winfo_reqwidth() / 2))
		Checkbutton(self, command=lambda: self.toggle_selected(i)).grid(row = i, column = 1, pady = self.winfo_reqheight() / 10, padx = self.winfo_reqwidth() / 10)

	def toggle_selected(self, i):
		self.selected[i].set(not (self.selected[i].get()))

	def show(self):
		self.wm_deiconify()
		self.wait_window()
		return [country for i, country in enumerate(self.countries) if self.selected[i].get()]

class DiagnosisResultWindow(Toplevel):
	def __init__(self, win, id):
		Toplevel.__init__(self, win)
		self.diagnosis_info = get_diagnosis(id)
		self.display_result()
	
	def display_result(self):
		name = self.diagnosis_info["name"]
		id = self.diagnosis_info["id"]

		all_symptoms = get_all_symptoms()

		all_countries = get_all_countries()

		self.title = Label(self, text="{}\nDiagnosis ID:{}".format(name, id))
		self.title.grid(row=0, column=0, columnspan=2, pady= self.winfo_reqheight() / 10, padx= self.winfo_reqwidth() / 10)

		self.symptom_ids = [symptom["symptomId"] for symptom in self.diagnosis_info["symptoms"]]
		self.country_ids = [country["countryId"] for country in self.diagnosis_info["countries"]]
		self.countries_info = self.diagnosis_info["countries"]
		
		self.temperature = self.diagnosis_info["temperature"]
		self.result = self.diagnosis_info["result"]

		self.symptoms_names = [symptom["name"] for symptom in all_symptoms if symptom["id"] in self.symptom_ids]
		self.country_names = [country["country_name"] for country in all_countries if country["id"] in self.country_ids]

		self.build_temperature_row()
		self.build_symptoms_row()
		self.build_countries_row()
		self.build_date_row()
		self.build_result_row()

		self.ok = Button(self, text="Okay", command=self.destroy, pady=self.winfo_reqheight() / 20)
		self.ok.grid(row=6, column=0, columnspan=2)

	def build_temperature_row(self):
		self.temperature_text = Label(self, text="Temperature")
		self.temperature_value = Label(self, text="{} °C".format(str(self.diagnosis_info["temperature"])))

		self.temperature_text.grid(row=1, column=0, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)
		self.temperature_value.grid(row=1, column=1, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)

	def build_symptoms_row(self):
		self.symptoms_text = Label(self, text="Symptoms")
		self.symptoms_list = Label(self, text="\n".join(self.symptoms_names))

		self.symptoms_text.grid(row=2, column=0, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)
		self.symptoms_list.grid(row=2, column=1, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)

	def build_countries_row(self):
		self.countries_text = Label(self, text="Countries")
		self.countries_list = Label(self, text="\n".join(self.country_names))

		self.countries_text.grid(row=3, column=0, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)
		self.countries_list.grid(row=3, column=1, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)

	def build_date_row(self):
		self.date_text = Label(self, text="Date")
		self.date_value = Label(self, text="{}".format(self.diagnosis_info["createdAt"]))

		self.date_text.grid(row=4, column=0, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)
		self.date_value.grid(row=4, column=1, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)

	def build_result_row(self):
		self.result_text = Label(self, text="Result")
		self.result_value = Label(self, text="{}%".format(self.diagnosis_info["result"]))

		self.result_text.grid(row=5, column=0, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)
		self.result_value.grid(row=5, column=1, pady= self.winfo_reqheight() / 20, padx= self.winfo_reqwidth() / 2)


	def show(self):
		self.wm_deiconify()
		self.wait_window()

class DiagnosticsWindow(Frame):
	
	def __init__(self, win):
		Frame.__init__(self, win)
		self.name = None
		self.diagnostics = {"symptoms": None, "temperature": None, "countries_visited": None}
		self.final_diagnosis = None

		self.name_text = Label(win, text = "Name").grid(row = 1, column = 0, columnspan = 2, sticky = N+E+W, padx = win.winfo_reqwidth() / 5)
		self.name_input = Entry(win)
		self.name_input.grid(row = 1, column = 2, columnspan = 2, sticky = N+E, padx = win.winfo_reqwidth() / 5)
		
		self.build_symptoms_row(win)

		self.build_temperature_row(win)

		self.build_countries_visited_row(win)

		self.ok_button = Button(win, text="Diagnose", command=self.submit_diagnosis)
		self.ok_button.grid(row = 5, column = 1, columnspan=2, sticky = N + W + E, pady = win.winfo_reqheight() / 10)
		
	def build_symptoms_row(self, win):
		self.symptoms_prefix = Label(win, text = self.generate_prefix("symptoms"))
		self.symptoms_prefix.grid(row = 2, column = 0, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_text = Label(win, text = "Symptoms")
		self.symptoms_text.grid(row = 2, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_status = Label(win, text = self.generate_status("symptoms"))
		self.symptoms_status.grid(row = 2, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.symptoms_edit = Button(win, text = "Edit", command = self.get_symptoms)
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
		
		self.countries_visited_text = Label(win, text = "Countries Visited")
		self.countries_visited_text.grid(row = 4, column = 1, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.countries_visited_status = Label(win, text = self.generate_status("countries_visited"))
		self.countries_visited_status.grid(row = 4, column = 2, sticky = N+W, padx = win.winfo_reqwidth() / 5)
		
		self.countries_visited_edit = Button(win, text = "Edit", command = self.get_countries)
		self.countries_visited_edit.grid(row = 4, column = 3, sticky = N+W, padx = win.winfo_reqwidth() / 5)

	def generate_prefix(self, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return ""
		else:
			prefix = self.diagnostics[diagnostic]
			if diagnostic == "temperature":
				farenheit = float(self.diagnostics[diagnostic]) * 1.8 + 32
				return str(self.diagnostics[diagnostic]) + " °C | " + ("%.2f" % farenheit ) + " °F"
			else:
				return str(len(self.diagnostics[diagnostic])) + " Selected"
			
	def generate_status(self, diagnostic):
		if self.diagnostics[diagnostic] == None:
			return "X"
		else:
			return "✓"

	def get_symptoms(self):
		self.diagnostics["symptoms"] = SymptomsWindow(self).show()
		
		self.symptoms_prefix.config(text = self.generate_prefix("symptoms"))
		self.symptoms_status.config(text = self.generate_status("symptoms"))

	def get_temperature(self):
		self.diagnostics["temperature"] = int(TemperatureWindow(self).show())

		self.temperature_prefix.config(text = self.generate_prefix("temperature"))
		self.temperature_status.config(text = self.generate_status("temperature"))


	def get_countries(self):
		self.diagnostics["countries_visited"] = CountriesVisitedWindow(self).show()

		self.countries_visited_prefix.config(text = self.generate_prefix("countries_visited"))
		self.countries_visited_status.config(text = self.generate_status("countries_visited"))

	def diagnose_patient(self):
		country_ids = None
		symptom_ids = None
		
		country_probability = 0
		symptom_probability = 0
		temperature_probability = 0

		success = True
		
		try:

			if self.diagnostics["countries_visited"] != None and self.diagnostics["countries_visited"] != []:
				country_ids = [country["id"] for country in self.diagnostics["countries_visited"]]
				country_probability = get_country_probability(country_ids)
			
			if self.diagnostics["symptoms"] != None and self.diagnostics["symptoms"] != []:
				symptom_ids = [symptom["id"] for symptom in self.diagnostics["symptoms"]]
				symptom_probability = get_symptom_probability(symptom_ids)
			
			if(self.diagnostics["temperature"] != None):
				if self.diagnostics["temperature"] > 37:
					temperature_probability = 0.5
				elif self.diagnostics["temperature"] > 40:
					temperature_probability = 1

		except Exception as e:
			success = False
			print(e)
		
		if success:
			self.final_diagnosis = int((country_probability + symptom_probability + temperature_probability) / 3 * 100)
			result = add_diagnosis(self.name, self.diagnostics["temperature"], self.final_diagnosis, country_ids, symptom_ids)
			DiagnosisResultWindow(self, result["id"])

	def submit_diagnosis(self):
		self.name = self.name_input.get()
		self.diagnose_patient()

class RecordsWindow(Frame):

	def __init__(self, win):
		Frame.__init__(self, win)
		self.diagnoses = get_all_diagnoses()

		self.record_view = Canvas(win)
		self.scroll_bar = Scrollbar(win, command=self.record_view.yview)
		self.record_list = Frame(self.record_view)

		self.delete_buttons = []
		self.view_buttons = []

		self.build_records(win)
		
		self.record_view.create_window(0, 0, anchor='nw', window=self.record_list)		
		self.record_view.update_idletasks()
		self.record_view.configure(yscrollcommand=self.scroll_bar.set, scrollregion=self.record_view.bbox('all'))
		self.record_view.pack(side=LEFT, fill=BOTH, expand=True)

		self.scroll_bar.pack(side=RIGHT, fill=Y)

	def build_records(self, win):
		for i, diagnosis in enumerate(self.diagnoses):
			self.build_row(win, i, diagnosis)
	
	def delete_record(self, id, num):
		delete_diagnosis(id)
		self.delete_buttons[num].config(state='disabled')
		self.view_buttons[num].config(state='disabled')

	def build_row(self, win, num, diagnosis):
		Label(self.record_list, text=diagnosis["name"]).grid(row=num * 2, column=0, padx=win.winfo_reqwidth() / 3)
		Label(self.record_list, text=diagnosis["createdAt"]).grid(row=num * 2, column=1)
		self.view_buttons.append(Button(self.record_list, text="View", command=lambda: DiagnosisResultWindow(win, diagnosis["id"])))
		self.view_buttons[-1].grid(row=num * 2, column=2, sticky=E, padx = (50, 25))
		self.delete_buttons.append(Button(self.record_list, text="Delete", command=lambda: self.delete_record(diagnosis["id"], num)))
		self.delete_buttons[-1].grid(row=num * 2, column=3, sticky=E, padx = (25, 0))
		ttk.Separator(self.record_list, orient=HORIZONTAL).grid(row=num * 2 + 1, column = 0, columnspan=4, sticky = E + W)

root_header = Tk()
root_win = RootWindow(root_header)

root_header.title("Dengue Diagnosis Assistant")
root_header.geometry("600x400+10+10")
root_header.mainloop()
