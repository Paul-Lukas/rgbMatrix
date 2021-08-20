import random

from Libraries.matrix import NeoMatrix
from Applications.template import Application

class TicTacToe (Application):

    def __init__(self, matrix: NeoMatrix):
        super().__init__(matrix)

    def start(self):
        super().start()
        self.__reset()
        self.play()

    def play(self):
        #TODO: Get input Player 1
        pass

    def __reset(self):
        self.game_field = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tic')
def tictactoe():
    return render_template("tic_tac_toe.html", secret=random.randint(0, 999), pid=1,
                           pchar="x")