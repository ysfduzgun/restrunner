import os

def get_data_folder():
    path = os.getcwd()
    return os.path.abspath(os.path.abspath(path))

def create_data_folder(path):
    path = path+"/data"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            path = path+"/log"
            if not os.path.exists(path):
                os.makedirs(path)
    except OSError as e:
        print(e)
