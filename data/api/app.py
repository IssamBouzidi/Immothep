import os
import sys
from typing import Optional
import pandas as pd
from fastapi import FastAPI
import uvicorn

src_dir = os.path.join(os.getcwd(), 'src')
sys.path.insert(0,src_dir) 
print()
import modules.prediction_helper as predictor
import modules.file_helper as file_help

property_types = pd.read_csv(os.path.join(file_help.DATA_OUT_FOLDER, 'property_type_referential.csv'), encoding='utf-8', sep=',')

app = FastAPI()

@app.get("/api/estimate/")
async def read_item(insee_code, range_km, property_type, surface, ground_surface, nb_rooms):
    '''
        metre_carre : le nombre de m² habitables loi Carrez
        nb_pieces : nombre de pièces principales
        terrain : le nombre de m² du terrain
        code_postal : le code postal où se trouve le bien
    '''

    property_type_name = property_types[property_types['Code type local'] == int(property_type)]['Type local']

    estimate = predictor.estimate_property(insee_code, int(range_km), property_type_name.values[0], int(surface), int(ground_surface), int(nb_rooms))

    if estimate < 0:
        return 'cannot estimate property. Insee_Code not found'

    return round(float(estimate), 2)


if __name__ == "__main__":
    uvicorn.run(app, port=5003)