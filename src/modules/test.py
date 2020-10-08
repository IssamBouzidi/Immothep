import os
import numpy as np
import pandas as pd

DATA_IN_FOLDER = 'C:/prairie/projet8/data/in/'

data = pd.read_csv(os.path.join(DATA_IN_FOLDER, 'valeursfoncieres-2019.txt'), encoding='utf-8', sep='|')

# Check the number of data points in the data set
print(len(data))
# Check the number of features in the data set
print(len(data.columns))
# Check the data types
print(data.dtypes.unique())


#drop empty columns
data.dropna(axis = 1, how ='all', inplace = True) 
print(len(data.columns))

data.dropna(subset = ['Nature mutation','Valeur fonciere','Code postal','Type local','Surface reelle bati','Nombre pieces principales', 'Surface terrain'], inplace = True) 
print(len(data))


data.reset_index(drop=True)

new_data = data.filter(['Date mutation', 'Nature mutation','Valeur fonciere','Code postal','Type local','Surface reelle bati','Nombre pieces principales', 'Surface terrain'])
new_data.head()


""" 
data.select_dtypes(include=['O']).columns.tolist()

# Check any number of columns with NaN
print(data.isnull().any().sum(), ' / ', len(data.columns))
# Check any number of data points with NaN
print(data.isnull().any(axis=1).sum(), ' / ', len(data))

#drop empty columns
empty_columns = []
for column in data.columns:
    if(data[column].isnull().all()):
        print(f'column {column} is empty')
    elif(data[column].isnull().any()):
        print(f'column {column} as empty field')

data.drop(columns=empty_columns, inplace=True) """

