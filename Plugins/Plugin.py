from Application import BaseApplication
from Libraries.matrix import NeoMatrix


class Plugin:

    def __init__(self, app: BaseApplication, matrix: NeoMatrix):
        self.matrix = matrix
        self.app = app
        self.pluginName = "Put Plugin Name Here"
        self.pluginDescription = "Put Descripiton here"

    def run(self):
        raise NotImplementedError
