import inspect
import pkgutil
from FlaskWeb import Api
from Libraries import matrix
from Plugins.Plugin import Plugin


class BaseApplication:

    def __init__(self, matrix):
        self.matrix = matrix
        self.plugins = []
        self.api = Api.Api(self.gameInputCallback(input), self.gameRunningName(), self.gameSetCallback(gameName))

    def run(self):
        self.__reload_plugins()
        self.loadStartpage()
        #TODO: remove when Web Interface is Finnished
        self.__run_plugins()

    def loadStartpage(self):
        pluginNames = []
        for plugin in self.plugins:
            pluginNames.append(plugin.__name__)
        self.api.startpage(pluginNames)

    def gameInputCallback(self, input: str):
        # TODO: check if active plugin is set
        self.activePlugin.inputCallback(input)

    def gameRunningName(self):
        return self.activePlugin.__name__

    def gameSetCallback(self, gameName):
        for plugin in self.plugins:
            if plugin.__name__ == gameName:
                plugin.run()

    def __reload_plugins(self):
        imported_package = __import__('Plugins', fromlist=['blah'])

        for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=['blah'])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Plugin, but NOT Plugin itself
                    if issubclass(c, Plugin) & (c is not Plugin):
                        print(f'    Found plugin class: {c.__module__}.{c.__name__}')
                        self.plugins.append(c(self, self.matrix))

    def __run_plugins(self):
        # TODO: Run boot first
        for plugin in self.plugins:
            self.activePlugin = plugin
            plugin.run()
