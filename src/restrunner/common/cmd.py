"""Import tinydb, datetime, database"""
from subprocess import Popen
from datetime import datetime

# import database
from restrunner.common import db
from restrunner.conf import settings as Settings

def get_date_now():
    """Return time with speacial format for logging"""
    return datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

def run(name, command):
    print(name+" basladi")
    date_now = get_date_now()
    log_file = Settings.DATA_FOLDER+"/log/"+date_now+"-"+name+".log"
    print(log_file)

    item = { 'sdate': date_now,
        'fdate': -1,
        'file': log_file,
        'name': name,
        'status': 2
    }
    log = open(log_file, 'a')
    log.write(date_now+' '+name+'\n')
    log.flush()
    proc = Popen(command, stdout=log, stderr=log, shell=True)
    proc_id = db.new_task(item)
    proc.wait()
    if proc.poll() == 0 :
        db.update_task(proc_id, "status", 1)
        db.update_task(proc_id, "fdate", get_date_now())
    else:
        db.update_task(proc_id, "status", 0)
        db.update_task(proc_id, "fdate", get_date_now())
