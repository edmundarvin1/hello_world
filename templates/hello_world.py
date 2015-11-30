from flask import Flask,render_template
from os import environ
import datetime
app = Flask(__name__)

@app.route("/")
def say_hiiie():
    return "Hello,World"
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi_person(first_name,last_name):
    
    html = """<h1>Hello Jedi {}!
    </h1>
    """
    return html.format(last_name[:3]+first_name[:2])
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))

    
            
        