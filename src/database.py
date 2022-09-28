"""Import tinydb and datetime"""
from datetime import datetime
from tinydb import TinyDB, Query

def date_now():
    """Return time with speacial format for logging"""
    return datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

db_json = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
table_commands = db_json.table('Commands')
table_tasks = db_json.table('Tasks')
q = Query()

# Command operations

def get_all_commands():
    """Return all commands in db.json in list type."""
    return table_commands.all()

def search_command(value):
    """Search commands in commands table in db.json."""
    res = table_commands.search(q.name == value)
    if len(res) != 0 :
        return res[0]
    return 0

# Task operations

def search_task(status):
    """Search task in logs table in db.json with status.
    Status parameter can be only 0,1,2.
    0=fail, 1=success, 2=continuing"""
    res = table_tasks.search(q.status == status)
    print(res)
    if len(res) != 0 :
        return res
    return 0

def get_all_tasks():
    """Return all commands in db.json in list type."""
    return table_tasks.all()
