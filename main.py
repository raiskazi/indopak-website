from flask import Flask, render_template, url_for, request
from markupsafe import escape 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/butcher")
def butcher():
    return render_template('butcher.html')

@app.route("/banquet")
def banquet():
    return render_template('banquet.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/cafe/')
@app.route('/cafe/<location>')
def cafe(location=None):
    if location is None or (location != "plano" and location !="richardson" and location !="arlington" and location !="lewisville" and location !="carrollton"):
        return render_template("cafe/cafe.html")
    return render_template("cafe/" + location + ".html")