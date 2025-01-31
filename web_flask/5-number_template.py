#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_root():
    """Prints 'Hello HBNB!' to display"""
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Prints 'HBNB' to display"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    """Print route param to display"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def display_n(n):
    """Print n if n is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_n_template(n):
    """Return an html page with value of n"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
