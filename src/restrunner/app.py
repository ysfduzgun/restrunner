"""Importing standart libs"""
from flask import Flask
from flask_restful import Api
import inspect

from restrunner.resources.query import CommandList
from restrunner.resources.query import SearchTask
from restrunner.resources.restrunner import RunCommand

from restrunner.common.data import create_data_folder
from restrunner.common import db
from restrunner.conf import settings

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
        "host": '127.0.0.1',
        "data_folder": ""
    }
    __setters = ["port", "debug", "host", "data_folder"]

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

        settings.PORT = RestRunner.__conf["port"]
        settings.DEBUG = RestRunner.__conf["debug"]
        settings.HOST = RestRunner.__conf["host"]
        settings.DATA_FOLDER = RestRunner.__conf["data_folder"]

        if(settings.DATA_FOLDER == ""):
            runner_path = inspect.stack()[1][1]
            runner_path = runner_path[0:runner_path.rindex("/")]
            settings.DATA_FOLDER = runner_path+"/data"
            create_data_folder(settings.DATA_FOLDER)
        else:
            print("no")

        db.init()
        app.run(debug=settings.DEBUG,
                port=settings.PORT,
                host=settings.HOST)
