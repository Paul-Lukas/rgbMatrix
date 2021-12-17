class Plugin:

    def __init__(self, app, matrix):
        self.matrix = matrix
        self.app = app
        self.pluginName = "Put Plugin Name Here"
        self.pluginDescription = "Put Descripiton here"

    def run(self):
        raise NotImplementedError

    def inputCallback(self):
        raise NotImplementedError