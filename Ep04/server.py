'''
Run with `flask --app server --debug run`
'''

from flask import Flask, request, render_template

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
@app.route("/login", methods=["GET", "POST"])
def query():
	args = request.args
	print(request.method)
	if request.method == "GET":
		return "Get: " + args.get("name", default="Sami") + " is " + args.get("age", default="4") + " years old."
	else:
		print(request.form)
		print(request.data)
		return args

@app.route("/hi/<name>")
def hi(name=None):
	return render_template("hi.html", name=name)

print("Running")