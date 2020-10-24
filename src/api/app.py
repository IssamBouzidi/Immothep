import os
import sys
import pandas as pd
from fastapi import FastAPI
import uvicorn

#find root directory
src_dir = os.path.join(os.getcwd(), 'src')
sys.path.insert(0,src_dir) 

import modules.prediction_helper as predictor
import modules.file_helper as file_help
import modules.data_selector_helper as data_help

property_types = pd.read_csv(os.path.join(file_help.DATA_OUT_FOLDER, 'property_type_referential.csv'), encoding='utf-8', sep=';')

app = FastAPI()

@app.get("/api/estimate/")
async def read_item(insee_code, range_km, property_type, surface, ground_surface, nb_rooms):
    """Estimate a property based on similar properties sold in the same geographical perimeter

    Args:
        insee_code (int): give the insee code then estimate will be based on this city and a defined perimeter
        range_km (int): permiter of the search in km
        property_type (int): type of property : 1- Home; 2- Appartement
        surface (int): surface of the property
        ground_surface (int): surface of the ground property
        nb_rooms (int): number of rooms

    Returns:
        [int]: estimate in €
    """

    property_type_name = property_types[property_types['Code type local'] == int(property_type)]['Type local']

    #check input data
    if not str.isnumeric(range_km):
        return 'bad input numeric value for range_km'

    if not str.isnumeric(surface):
        return 'bad input numeric value for surface'

    if not str.isnumeric(ground_surface):
        return 'bad input numeric value for ground_surface'

    if not str.isnumeric(nb_rooms):
        return 'bad input numeric value for nb_rooms'

    if not data_help.is_insee_code_exists(insee_code):
        return 'code insee not found'

    #only apply estimation for 1 or 2
    if int(property_type) < 1 or int(property_type) > 2:
        return 'bad property type - use 1 for houses or 2 for appartments'

    #estimate propoerty
    estimate = predictor.estimate_property(insee_code, int(range_km), property_type_name.values[0], int(surface), int(ground_surface), int(nb_rooms))

    #bad estimate due to non existing code INSEE
    if estimate < 0:
        return 'cannot estimate property. Insee_Code not found'

    return {'estimation': round(float(estimate), 2)} 


if __name__ == "__main__":
    uvicorn.run(app, port=5003)