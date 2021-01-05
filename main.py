from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cafe")
def cafe():
    return render_template('cafe.html')


@app.route("/butcher")
def butcher():
    return render_template('butcher.html')

@app.route("/banquet")
def banquet():
    return render_template('banquet.html')

@app.route("/about")
def about():
    return render_template('about.html')
