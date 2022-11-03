import os

from restrunner.conf import settings as Settings

def get_data_folder():
    return Settings.DATA_FOLDER

def create_data_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            os.makedirs(path+"/log")
            open(path+"/commands.json", 'a').close()
            open(path+"/tasks.json", 'a').close()
        elif not os.path.exists(path+"/log"):
            path = path+"/log"
            os.makedirs(path)
            open(path+"/commands.json", 'a').close()
            open(path+"/tasks.json", 'a').close()
        else:
            if not os.path.exists(path+"/commands.json"):
                open(path+"/commands.json", 'a').close()
            if not os.path.exists(path+"/tasks.json"):
                open(path+"/tasks.json", 'a').close()
                
    except OSError as e:
        print(e)

def create_commands_template():
    pass
