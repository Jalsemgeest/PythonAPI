'''
Run with `flask --app server --debug run`
'''

from flask import Flask, request

app = Flask(__name__)

# Get request - it will return just what you tell it to
@app.route("/")
def index():
	return "Running!"

# Get request - it will return based on the input of the name parameter in the URL
@app.route("/hello/<name>")
def helloWorld(name=None):
	return "Hello, " + name + "!"

# Here you can use query parameters. The first must start with ?key=value, then &key=value after that.
# Spaces cannot be used. If you want to add a space you need to do %20 as it's the value for a space!
@app.route("/login")
def query():
	args = request.args
	return args

print("Running")