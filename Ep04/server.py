
from flask import Flask, render_template
import random

app = Flask(__name__)

messages = [ "Subscribe", "Like", "Comment", "Eat a cookie" ]

@app.route('/')
def index():
    message = messages[random.randint(0, 3)]
    
    return render_template('index.html', message=message)

@app.route('/about')
def about():
  
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)