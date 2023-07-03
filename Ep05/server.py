'''
Run with `flask --app server --debug run`
'''

from flask import Flask, request, render_template
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
	
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

conn = create_connection(
	"postgres", "postgres", "sami", "localhost", "5432")

table_init = """
CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    age INTEGER,
    fun TEXT
)
"""
execute_query(conn, table_init)

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
		print("form data")
		print(request.form)
		print("request data")
		print(request.json.get('name'))
		json=request.json
		create_user = "INSERT INTO users (name, age) VALUES ('"+json.get('name')+"', '"+json.get('age')+"') ON CONFLICT DO NOTHING"
		execute_query(conn, create_user)
		return args

@app.route("/hi/<name>")
def hi(name=None):
	return render_template("hi.html", name=name)

@app.route("/db")
def database():
	q = """
	SELECT 
		*
	FROM
		users;
	"""
	return execute_read_query(conn, q)
	return "database info"

print("Running")