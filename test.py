#!/usr/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/outside')
def outside():
    return render_template('outside.html')

@app.route('/forecast')
def forecast():
    return render_template('forecast.html')

@app.route('/system')
def system():
    return render_template('system.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





