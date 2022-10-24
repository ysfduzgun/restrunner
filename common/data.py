import os

def get_data_folder():
    path = os.getcwd()
    _ROOT = os.path.abspath(os.path.abspath(path))
    return os.path.join(_ROOT, 'data/')