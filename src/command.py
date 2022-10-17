"""Import tinydb, datetime, database"""
from subprocess import Popen
from datetime import datetime

def get_date_now():
    """Return time with speacial format for logging"""
    return datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

# def cmd_run(command):
#     log = open('log.txt', 'a')
#     log.write('some text, as header of the file\n')
#     log.flush()
#     proc = Popen(command, stdout=log, stderr=log, shell=True)
#     #proc.wait()
#     print(proc.poll())

# cmd_run("sleep 5; ls -la; echo ismail")

def cmd_run(name, command):
    print(name+" basladi")
    date_now = get_date_now()
    log_file = "log/"+date_now+"-"+name+".log"
    
    item = { 'sdate': date_now, 
        'fdate': -1,
        'file': "2022-09-26-15-32-01-komut-adi.log",
        'name': name, 
        'status': -1, 
    }
    log = open(log_file, 'a')
    log.write(date_now+' '+name+'\n')
    log.flush()
    proc = Popen(command, stdout=log, stderr=log, shell=True)
    proc.poll()
    #proc.wait()
    #print(proc.poll())
    #proc.communicate()
