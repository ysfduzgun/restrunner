"""Import tinydb and datetime"""
from tinydb import TinyDB, Query
from restrunner.conf import settings as Settings
import os

commands_json_file = None
tasks_json_file = None
commands = None
tasks = None
q = None

from restrunner.common import db

def init():
    db.commands_json_file = Settings.DATA_FOLDER+"/commands.json"
    db.tasks_json_file = Settings.DATA_FOLDER+"/tasks.json"

    db.commands = TinyDB(commands_json_file, sort_keys=True, indent=4, separators=(',', ': '))
    fpath = Settings.DATA_FOLDER+"/commands.json"
    if os.stat(fpath).st_size == 0:
        db.commands.insert_multiple(Settings.DEFAULT_COMMANDS)
    
    db.tasks = TinyDB( tasks_json_file, sort_keys=True, indent=4, separators=(',', ': '))
    db.q = Query()

# Command info operations

def get_all_commands():
    """Return all commands in db.json in list type."""
    print("------------"+str(commands.all()))
    return commands.all()

def search_command(value):
    """Search commands in commands table in db.json."""
    res = commands.search(q.name == value)
    if len(res) != 0 :
        return res[0]
    return 0

# Task operations

def search_task(status):
    """Search task in logs table in db.json with status.
    Status parameter can be only 0,1,2.
    0=fail, 1=success, 2=continuing"""
    res = tasks.search(q.status == status)
    print(res)
    if len(res) != 0 :
        return res
    return 0

def new_task(items):
    """Insert new task item like this
    item = {
        "fdate": "2022-10-21-16-58-59",
        "file": "log/2022-10-21-16-58-54-test4.log",
        "name": "test4",
        "sdate": "2022-10-21-16-58-54",
        "status": 1
    }"""
    return tasks.insert(items)

def update_task(id, name, value):
    tasks.update({name: value}, doc_ids=[id] )

def get_all_tasks():
    """Return all commands in db.json in list type."""
    return tasks.all()
