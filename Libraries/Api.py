from fastapi import FastAPI


class Api:
    app = FastAPI()


    def __init__(self, inputCallback, getCallback, setGameCallback):
        self.inputCallback = inputCallback
        self.getCallback = getCallback
        self.setGameCallback = setGameCallback


    @app.get("/")
    def status(self):
        pass


    @app.get("/game/set")
    def setGame(self, gameId: int):
        self.setGameCallback()


    @app.get("/game/input")
    def input(self, input: str):
        self.inputCallback(input)


    @app.get("/game/get")
    def output(self):
        self.getCallback()
