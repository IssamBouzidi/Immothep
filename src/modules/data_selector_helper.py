import os
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import modules.file_helper as file_help

cwd = file_help.get_root()

DATA_IN_FOLDER = os.path.join(cwd, 'data', 'out')

def compute_distance(lat1, lon1, lat2, lon2):
    R = 6372800  # Earth radius in meters

    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    total_distance = 6372800 * c
    return np.rint(total_distance/1000)


def get_sells_from_insee_code(insee_code, property_type, range_km):
    coord_gps = pd.read_csv(os.path.join(DATA_IN_FOLDER, 'coord_gps_referential.csv'), encoding='utf-8', sep=';')
    curated_data = pd.read_csv(os.path.join(DATA_IN_FOLDER, property_type + '_valeursfoncieres.csv'), encoding='utf-8', sep=';')

    coord_gps['Code INSEE'] = coord_gps['Code INSEE'].astype(str)
    from_city = coord_gps[coord_gps['Code INSEE'] == str(insee_code)]
    if len(from_city) == 0:
        print('INSEE code not found')
        return []

    lat1, lon1 = [from_city['Latitude'].values[0], from_city['Longitude'].values[0]]

    curated_data['distance'] = compute_distance(lat1, lon1, curated_data['Latitude'].values, curated_data['Longitude'].values)

    working_data = curated_data[curated_data['distance'] < int(range_km)]
    if len(working_data) == 0:
        print('No data found for this INSEE code')
        return []

    return working_data

def apply_isolation_forest(working_data):
    #Use Isolation forest model to finalize cleanup of dataset
    df = working_data[['Surface reelle bati','Nombre pieces principales','Surface terrain', 'Valeur fonciere', 'distance']]

    iForest = IsolationForest(n_estimators=100,  contamination=0.1 , random_state=42, max_samples=200)
    iForest.fit(df)

    df['anomaly'] = iForest.predict(df)
    print('number of anomalies found : %s' % len(df[df['anomaly'] == -1]))

    working_data.drop(df.loc[df['anomaly'] == -1].index, inplace=True)

    return working_data

def is_insee_code_exists(insee_code):
    coord_gps = pd.read_csv(os.path.join(DATA_IN_FOLDER, 'coord_gps_referential.csv'), encoding='utf-8', sep=';')
    coord_gps['Code INSEE'] = coord_gps['Code INSEE'].astype(str)
    from_city = coord_gps[coord_gps['Code INSEE'] == str(insee_code)]
    if len(from_city) == 0:
        return False
    else:
        return True