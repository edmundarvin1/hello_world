from flask import Flask,render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello_home():
    return render_template("hello1.html")

@app.route('/hello/<name>')
def hello_personal(name):
    return render_template('personal_hello.html',
    my_name= name)
    
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port= 8080)

