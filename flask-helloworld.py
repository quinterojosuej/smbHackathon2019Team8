from flask import Flask, render_template 

# create an instance of the Flask class
app = Flask(__name__)

# route() decorator binds a function to a URL
@app.route('/')
def home():
    my_string = "<h1>Welcome to my page</h1><p>Have a nice day!</p>"
    return my_string

@app.route('/hello')
def hello():
    return 'Hello world from Flask' + saymyname()

@app.route('/whoami')
def whoami():
    return saymyname()

def saymyname():
    return "Wes"

