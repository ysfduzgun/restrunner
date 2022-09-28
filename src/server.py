"""Importing flask"""
from flask import Flask
from flask_restful import abort, Api, Resource

# Import database and command
import database
# import command

COMMAND_LIST = database.get_all_commands()

# Setup flask rest
app = Flask(__name__)
api = Api(app)


def abort_doesnt_exist(name):
    """Abort request if doesnt exist."""
    abort(404, message=f"{name} doesn't exist")


class CommandList(Resource):
    """Flask Restfull class for getting command list."""
    def get(self):
        """Flask restfull standart get function."""
        return COMMAND_LIST


class RunCommand(Resource):
    """Flask Restfull class for running command."""

    def get(self, name):
        """Flask restfull standart get function."""
        val = database.search_command(name)
        if val != 0 :
            #command.run(val['command'])
            return val
        else:
            abort_doesnt_exist(name)


class SearchTask(Resource):
    """Flask Restfull class for search task."""

    def get(self, status):
        """Flask restfull standart get function."""
        val = database.search_task(status)
        if val != 0 :
            return val
        else:
            abort_doesnt_exist(status)


class Help(Resource):
    """Flask Restfull class for Help."""
    def get(self):
        """Flask restfull standart get function."""
        routes = []
        for route in app.url_map.iter_rules():
            routes.append(str(route))
        return routes


# Setup the Api resource routing help
api.add_resource(Help, '/help')
# Flask automatically creates a /static/<path:filename> route
#that will serve any filename under the static folder


# Setup the Api resource routing realated commands
api.add_resource(CommandList, '/commands')
api.add_resource(RunCommand, '/commands/run/<name>')


# Setup the Api resource routing realated tasks
api.add_resource(SearchTask, '/tasks/<int:status>')


if __name__ == '__main__':
    app.run(debug=True)
