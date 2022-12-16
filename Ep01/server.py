'''
Run with `flask --app server --debug run`
'''

from flask import Flask

app = Flask(__name__)

# Get request - it will return just what you tell it to
@app.route("/")
def index():
	return "Subscribe to JakeEh!"

# Get request - it will return based on the input of the name parameter in the URL
@app.route("/hello/<name>")
def helloWorld(name=None):
	return "Hello, " + name + "!"

print("Running")