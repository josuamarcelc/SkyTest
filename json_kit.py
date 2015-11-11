import json
def json_reader(filename):
	with open('data/' + filename + '.json', 'r') as f:
		json_file = json.load(f)
		return(json_file)

def json_editor(filename, code):
		json_data = json_reader(filename)
		# print(json_data)
		for item in json_data:
			if item['id'] == int(code):
				item['stars'] += 1
				print(item['stars'])
		with open('data/' + filename + '.json', 'w') as g:
			json.dump(json_data, g)