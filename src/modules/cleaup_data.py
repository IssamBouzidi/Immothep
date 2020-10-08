import os
import pandas as pd

DATA_IN_FOLDER = 'C:/prairie/projet8/data/in/'


data = pd.read_csv(os.path.join(DATA_IN_FOLDER, 'valeursfoncieres-2019.txt'), encoding='utf-8', sep='|')

#data.subset=['Valeur fonciere', 'born']

data.dropna(column)
new_data = data.filter(['Date mutation', 'Nature mutation','Valeur fonciere','Code postal','Type local','Surface reelle bati','Nombre pieces principales', 'Surface terrain'])
new_data.head()
