from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/psy')
def psy():
    return render_template('index.html')
@app.route('/kot')
def kot(name):
    return render_template('index.html')
@app.route('/user/name')
def kot(name):
    return render_tamplate('user.html', imie=name)
