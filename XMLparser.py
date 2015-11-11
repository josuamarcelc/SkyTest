import os
import json
from bs4 import BeautifulSoup

def XML_parser(filename):
	soup = BeautifulSoup(open('data/uploads/' + filename + ".xml"))
	data_list = []

	programmes = soup.find_all(attrs={'id': True})
	for n in range(0, len(programmes)):
		name = programmes[n].contents[1].contents[1].contents[0]
		img = programmes[n].contents[1].contents[3].contents[0]
		id = n
		data_list.append({
				'name': name,
				'img': img,
				'id': n,
				'stars':0,
				})
	with open('data/json_data_file.json', 'w') as f:
		json.dump(data_list, f)
	return(data_list)