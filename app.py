"""Witam w pliku app"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')

def index():
    """Funkcja"""
    return '''<h1><center>Witam na mojej stronie</center></h1>\n
            <h2><center>Kamil Napieraj<center></h2>'''

if __name__ == "__main__":
    APP.run(debug=True)
