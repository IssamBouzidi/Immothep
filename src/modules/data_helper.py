import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.colors as colors
import matplotlib.pyplot as plt

def get_room_mean(surface, property_type, df):
    nb_rooms = np.mean(df[(df['Surface reelle bati'] < (surface * 1.1)) & (df['Surface reelle bati'] > (surface * 0.9)) &
(df['Code type local'] ==1)]['Nombre pieces principales'])

    return np.round(nb_rooms)


def print_sells_to_map(df):
    working_data = df[["Latitude","Longitude"]].value_counts(subset=['Latitude', 'Longitude'], sort=False).rename_axis(["Latitude","Longitude"]).reset_index(name='counts')
    working_data.sort_values(by=['counts'], ascending=False, inplace=True)

    # Extract the data we're interested in
    lat = working_data['Latitude'].values
    lon = working_data['Longitude'].values
    sells = working_data['counts'].values


    # 1. Draw the map background
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='merc',
                    llcrnrlat=42,
                    llcrnrlon=-5,
                    urcrnrlat=52,
                    urcrnrlon=9,
                    resolution='l')
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')
    m.drawrivers(color='lightblue')

    # define color for the layer
    cmap = plt.get_cmap('plasma')
    new_cmap = colors.LinearSegmentedColormap.from_list(
            'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=0.4, b=0.9),
            cmap(np.linspace(0.4, 0.9, 100)))


    # 2. scatter city data, with color reflecting population
    # and size reflecting area
    m.scatter(lon, lat, latlon=True,
            c=sells, s=sells/5,
            alpha=1, cmap=new_cmap)

    # 3. create colorbar and legend
    plt.colorbar(label=r'sells')
    plt.clim(3, 7)
