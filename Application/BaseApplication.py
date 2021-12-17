from Plugins.Plugin import Plugin
from Libraries import matrix, Api

import inspect
import pkgutil


class BaseApplication:

    def __init__(self, matrix):
        self.matrix = matrix
        self.plugins = []
        self.api = Api.Api(self.gameInputCallback(), self.gameGetCallback(), self.gameSetCallback())


    def run(self):
        self.__reload_plugins()

        self.__run_plugins()


    def gameInputCallback(self, input: str):
        #TODO: check if active plugin is set
        self.activePlugin.inputCallback(input)


    def gameGetCallback(self):
        pass


    def gameSetCallback(self):
        pass


    def __reload_plugins(self):
        imported_package = __import__('Plugins', fromlist = ['blah'])

        for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist = ['blah'])
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
