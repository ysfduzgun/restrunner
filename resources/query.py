from flask_restful import Resource
from flask_restful import abort

from common import db
from common.cmd import run

def abort_doesnt_exist(name):
    """Abort request if doesnt exist."""
    abort(404, message=f"{name} doesn't exist")

class CommandList(Resource):
    """Flask Restfull class for getting command list."""
    def get(self):
        """Flask restfull standart get function."""
        command_list = db.get_all_commands()
        return command_list

class SearchTask(Resource):
    """Flask Restfull class for search task."""

    def get(self, status):
        """Flask restfull standart get function."""
        val = db.search_task(status)
        if val != 0 :
            return val
        else:
            abort_doesnt_exist(status)