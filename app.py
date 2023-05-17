from distutils.command.upload import upload
from flask import Flask, send_from_directory,redirect, url_for, session
from logic.home import home
from logic.upload import upload

app = Flask(__name__, static_folder='templates/static')

app.config['SECRET_KEY'] = 'secret_key'


app.register_blueprint(upload)
app.register_blueprint(home)


@app.route('/')
def index():
    return redirect(url_for('process.show'))

if __name__ == '__main__':
    app.run(debug=True)
