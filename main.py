import os
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
from bs4 import BeautifulSoup

UPLOAD_FOLDER = 'data/uploads/'
ALLOWED_EXTENSIONS = set(['xml'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def XML_parser():
	soup = BeautifulSoup(open('data/uploads/test_data.xml'))
	data_list = []

	programmes = soup.find_all(attrs={'id': True})
	# print(programmes[0].contents[1].contents[3].contents)
	for n in range(0, len(programmes)):
		name = programmes[n].contents[1].contents[1].contents[0]
		img = programmes[n].contents[1].contents[3].contents[0]
		id = n
		data_list.append({
				'name': name,
				'img': img,
				'code' : n
				})
	
	return(data_list)

@app.route('/')
def index():

	return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			print(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template('upload_complete.html')
	return render_template('upload.html')

