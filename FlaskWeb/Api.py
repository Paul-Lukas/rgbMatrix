from flask import Flask, request, render_template


class Api:
    app = Flask("RGB Matrix")

    def __init__(self, inputCallback, gameRunningName, gameSetCallback):
        self.baseGameSetCallback = gameSetCallback

    @app.route('/game/input', methods=['GET', 'POST'])
    def inputCallback(self):
        if request.method == 'POST':
            pass
        else:
            pass

    def gameGetCallback(self):
        pass

    def gameSetCallback(self, gameName):
        self.baseGameSetCallback(gameName)

    def loadGame(self):
        pass

    @app.route('/')
    def startpage(self, gameNameList):
        return render_template('/FlaskWeb/templates/index.html', gameNameList = gameNameList)
