import json


def json_reader(filename):
	with open('data/' + filename + '.json', 'r') as f:
		json_file = json.load(f)
		return(json_file)

def json_editor(filename, code, max=5):
		json_data = json_reader(filename)
		for item in json_data:
			if item['id'] == int(code) and item['stars'] < 5:
				item['stars'] += 1
		with open('data/' + filename + '.json', 'w') as g:
			json.dump(json_data, g)