from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "hey indopak"

@app.route("/cafe")
def home():
    return "this is the cafe page"