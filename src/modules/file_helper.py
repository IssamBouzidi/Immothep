from genericpath import exists
import os
import requests

def get_root():
    path = os.getcwd()    
    root = False
    i = 0

    while not root:
        if not os.path.exists(os.path.join(path, 'requirements.txt')):
            path = os.path.abspath(os.path.join(path, os.pardir))
        else:
            root = True
        i = i+1

    return path
    
cwd = get_root()
DATASOURCE_PATH = r'https://www.data.gouv.fr/fr/datasets/r/3004168d-bec4-44d9-a781-ef16f41856a2'
DATA_IN_FOLDER = os.path.join(cwd, 'data', 'in')
DATA_CURATED_FOLDER = os.path.join(cwd, 'data', 'curated')
DATA_OUT_FOLDER = os.path.join(cwd, 'data', 'out')
DATA_REPORTS_FOLDER = os.path.join(cwd, 'data', 'reports')
FILE_NAME_IN = 'valeursfoncieres-2019.txt'
FILE_NAME_OUT_EXT = '_valeursfoncieres.csv'

def initialize_sells_referential():
    global_datasource_dest = os.path.join(DATA_IN_FOLDER, FILE_NAME_IN)

    if os.path.exists(global_datasource_dest):
        print('Data already downloaded')
    else :
        print('Download %s to %s' % (DATASOURCE_PATH, DATA_IN_FOLDER))
        with open(global_datasource_dest, "wb") as f:
            response = requests.get(DATASOURCE_PATH, stream=True)
            f.write(response.content)
            print('Data downloaded')
