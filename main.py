from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Home"

@app.route("/cafe")
def home():
    return "Cafe"