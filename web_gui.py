from flask import Flask
from Applications.Animator.animator import ListAnimations

app = Flask(__name__)

@app.route('/')
def menu():
    return "Menü"

app.add_url_rule('/animations/', view_func=ListAnimations.as_view('list_animations'))
