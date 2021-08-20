import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return "Menü"


@app.route('/tic')
def tictactoe():
    return render_template("tic_tac_toe.html", secret=random.randint(0, 999), pid=1,
                           pchar="x")
    pass


@app.route('/admin')
def admin():
    return "Admin"
