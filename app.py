"""Witam w pliku app"""

# from flask import Flask

# APP = Flask(__name__)

# @APP.route('/')

# def index():
#     """Funkcja"""
#     return '''<h1><center>Witam na mojej stronie</center></h1>\n
#             <h2><center>Kamil Napieraj<center></h2>'''

def dodawanie(a):
    """Proste dodawanie"""
    return a + 1

def test():
    """Prosty test"""
    assert dodawanie(4) == 5
    assert dodawanie(5) == 6

# if __name__ == "__main__":
    # APP.run(debug=True)
