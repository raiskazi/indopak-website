from flask import Flask, render_template, url_for 
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/cafe")
def home():
    return "<h1>Cafe<h1>"

