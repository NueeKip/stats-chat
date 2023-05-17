import datetime
from flask import render_template, request, session, Blueprint
import pandas as pd

home = Blueprint('home', __name__, template_folder='../templates')

"""Other functions"""
def get_greeting():
    greeting_msg = ""
    time = datetime.datetime.now()
    if time.hour < 12:
        greeting_msg = "Good morning, welcome to our data analysis, let's explore our dataset"
    elif time.hour >= 12 and time.hour <= 16:
        greeting_msg = "Good afternoon, welcome to our data analysis, let's explore our dataset"
    else:
        greeting_msg = "Good evening, welcome to our data analysis, let's explore our dataset"
    return greeting_msg


def get_filename():
    selected_filename = session.get('selected_filename')
    return selected_filename

def get_df():
    filename = get_filename()
    df = pd.read_csv(filename)
    return df
    

"""Stat functions"""

def get_attributes():
    df = get_df()
    attributes = df.columns
    return str(attributes)


"""Route functions"""

def display_filename():
    filename = get_filename()
    truncated_filename = filename.replace('data/', '').replace('-', ' ').replace('.csv', '')
    display = truncated_filename.title()
    return display

@home.route('/home', methods=['GET', 'POST'])
def show():
    get_filename()
    filename = display_filename()
    print(filename)

    if 'session_data' not in session:
        session['session_data'] = {'filename': filename}

    session_data = session['session_data']

    if 'attributes' not in session_data:
        attributes = get_attributes()
        session_data['attributes'] = attributes
    
    
    greeting_msg = get_greeting()
    session_data['greetings'] = greeting_msg
        
    template_data = {
                'greetings': session_data['greetings'],
                'cols': session_data['attributes'],
                'filename': session_data['filename']
            }
    return render_template('index.html' ,**template_data)







    # if request.method == 'POST':
    #     if request.form['submit'] == 'Start':
    #         greeting_msg = get_greeting()
    #         session_data['greetings'] = greeting_msg
    #         template_data = {
    #             'greetings': session_data['greetings'],
    #             'filename': session_data['filename']
    #         }
    #         return render_template('index.html', **template_data)
    #     elif request.form['submit'] == 'Attributes':
    #         greeting_msg = get_greeting()
    #         session_data['greetings'] = greeting_msg
    #         template_data = {
    #             'greetings': session_data['greetings'],
    #             'cols': session_data['attributes'],
    #             'filename': session_data['filename']
    #         }
    #         return render_template('index.html', **template_data)
    # else:
    #     return render_template('index.html', **template_data)