#from Libraries.matrix import NeoMatrix
from Application import BaseApplication

class Plugin:

    pluginName = "Oeffentlicher Name"

    def __init__(self, app:BaseApplication):
        self.app = app

    def run(self):
        raise NotImplementedError

    def get_name(self):
        return self.pluginName
