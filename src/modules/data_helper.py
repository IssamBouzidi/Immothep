import numpy as np


def get_room_mean(surface, property_type, df):
    nb_rooms = np.mean(df[(df['Surface reelle bati'] < (surface * 1.1)) & (df['Surface reelle bati'] > (surface * 0.9)) &
(df['Code type local'] ==1)]['Nombre pieces principales'])

    return np.round(nb_rooms)