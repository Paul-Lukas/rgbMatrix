from Plugins.Plugin import Plugin

import inspect
import pkgutil


class BaseApplication:

	def __init__(self):
		self.plugins = []


	def run(self):
		self.__reload_plugins()
		self.__run_plugins()


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
						self.plugins.append(c())


	def __run_plugins(self):
		for plugin in self.plugins:
			plugin.run()
