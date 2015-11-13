import os
from flask import Flask, render_template, request, flash
from werkzeug import secure_filename
from XMLparser import XML_parser
from json_kit import json_editor, json_reader
from operator import itemgetter

app = Flask(__name__, static_folder=os.path.dirname(os.path.realpath('images')) + "\images")
app.config.from_object('config')
app.secret_key = 'some_secret'


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
	try:
		programme_list = json_reader('json_data_file')
		return render_template('index.html', programme_list=programme_list)
	except FileNotFoundError:
		return render_template('index.html', message="Please upload a file.")
	


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			XML_parser(filename)
			flash('You successfully uploaded a file!')
		else:
			flash('You need a .xml file!')
	return render_template('upload.html')


@app.route('/vote/<code>')
def vote(code):
	json_editor('json_data_file', code)
	programme_list = json_reader('json_data_file')
	return render_template('index.html', programme_list=programme_list)


@app.route('/leaders')
def leaders():
	programme_list = json_reader('json_data_file')
	newlist = sorted(programme_list, key=itemgetter('stars'), reverse=True) 
	return render_template('leaders.html', programme_list=newlist)