from flask import Flask, render_template, url_for, request
from datetime import datetime
import json
app = Flask(__name__)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'$'):
        if amount is None:
            return '(N/A)'
        return u'{1}{0:.2f}'.format(amount, currency)
    return dict(format_price=format_price)


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
    if location is None or (location != "plano" and location != "richardson" and location != "arlington" and location != "lewisville" and location != "carrollton" and location != "irving" and location != "murphy"):
        return render_template("cafe/cafe.html")
    with open('cafe.json') as f:
        data = json.load(f)
    return render_template("cafe/" + location + ".html", data=data[location])
