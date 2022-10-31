"""Importing standart libs"""
from flask import Flask
from flask_restful import Api

from restrunner.resources.query import CommandList
from restrunner.resources.query import SearchTask
from restrunner.resources.restrunner import RunCommand

# Setup flask rest
app = Flask(__name__)
api = Api(app)


class Help():
    """Flask Restfull class for Help."""
    def get(self):
        """Flask restfull standart get function."""
        routes = []
        for route in app.url_map.iter_rules():
            routes.append(str(route))
        return routes


# Setup the Api resource routing help
#api.add_resource(Help, '/help')



# Flask automatically creates a /static/<path:filename> route
#that will serve any filename under the static folder


# Setup the Api resource routing realated commands
api.add_resource(CommandList, '/commands')
api.add_resource(RunCommand, '/commands/run/<name>')


# Setup the Api resource routing realated tasks
api.add_resource(SearchTask, '/tasks/<int:status>')

class RestRunner:
    __conf = {
    "port": 5000,
    "debug": False,
    "data_folder": "data"
    }
    __setters = ["port", "debug", "data_folder"]

    @staticmethod
    def config(name):
        return RestRunner.__conf[name]

    @staticmethod
    def set(name, value):
        if name in RestRunner.__setters:
            RestRunner.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")

    def run(self):
        app.run()