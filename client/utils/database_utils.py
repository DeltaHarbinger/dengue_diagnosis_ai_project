import requests

ROOT_URL = "http://localhost:5000"

def get_all_countries():
	response = requests.get("{}/countries".format(ROOT_URL))
	return response.json()["countries"]

def add_country(country_name, country_code):
	body = {"country_name": country_name, "country_code": country_code}
	response = requests.post("{}/countries".format(ROOT_URL), data=body)
	return response.json()

def update_country(id, country_name=None, country_code=None):
	body = {"id": id}
	if country_name != None:
		body["country_name"] = country_name
	if country_code != None:
		body["country_code"] = country_code
	response = requests.put("{}/countries".format(ROOT_URL), data=body)
	return response.json()["updates"]

def delete_country(id):
	body = {"id": id}
	response = requests.delete("{}/countries".format(ROOT_URL), data=body)
	return response.json()

def get_all_symptoms():
	response = requests.get("{}/symptoms".format(ROOT_URL))
	return response.json()["symptoms"]

def add_symptom(name):
	body = {"name": name}
	response = requests.post("{}/symptoms".format(ROOT_URL), data=body)
	return response.json()

def update_symptom(id, name=None):
	body = {"id": id}
	if name != None:
		body["name"] = name

	response = requests.put("{}/symptoms".format(ROOT_URL), data=body)
	return response.json()["updates"]

def delete_symptom(id):
	body = {"id": id}
	response = requests.delete("{}/symptoms".format(ROOT_URL), data=body)
	return response.json()

if __name__ == '__main__':
	pass
