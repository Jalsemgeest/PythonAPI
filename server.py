'''
Run with `flask --app server run`
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return "Running!"

@app.route("/hello/<name>")
def helloWorld(name=None):
	return render_template("hello.html", name=name)

print("Running")