import os
from flask import Blueprint, url_for, render_template, redirect, request,session
from werkzeug.utils import secure_filename
import datetime
import pandas as pd


upload = Blueprint('upload', __name__, template_folder='../templates')
# Create an empty dictionary to store file names and directories
file_dict = {}

@upload.route('/', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            file_directory = os.path.join('data/', filename)
            file.save(file_directory)           
            file_dict[filename] = file_directory
        else:
            return "Invalid file. Please upload a CSV file."
    return render_template('upload.html',filenames = file_dict)


@upload.route('/dataset', methods=['GET', 'POST'])
def toDf():
    if request.method == 'POST':
        filename = request.form['filename']
        df_name = filename
        df_name = ("data/" + df_name)
        session['selected_filename'] = df_name 
    return redirect(url_for('home.show'))