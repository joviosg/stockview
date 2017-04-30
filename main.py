from googlefinance import getQuotes
from flask import *

app = Flask(__name__)

@app.route('/')

def stock():
    y = getQuotes('FB')
    return render_template('index', y=y)

