from flask_restful import Resource
from flask_restful import abort
from flask import jsonify
from threading import Thread

from restrunner.common import db
from restrunner.common.cmd import run

def abort_doesnt_exist(name):
    """Abort request if doesnt exist."""
    abort(404, message=f"{name} doesn't exist")

class RunCommand(Resource):
    """Flask Restfull class for running command."""

    def get(self, name):
        """Flask restfull standart get function."""
        val = db.search_command(name)
        if val != 0 :
            thread = Thread(target=run, args=(val['name'], val['command']))
            thread.start()
            return jsonify(result=True)
        else:
            abort_doesnt_exist(name)