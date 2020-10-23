
import modules.file_helper as file_help
import modules.data_selector_helper as data_help
import seaborn as sns
import numpy as np
from sklearn import model_selection 
import xgboost


def get_correlation_matrix(code_insee, range, data_type):
    working_data = data_help.get_sells_from_insee_code(code_insee, data_type, range)

    if len(working_data) == 0:
        print('Cannot create correlation matrix')
        return []

    working_data = data_help.apply_isolation_forest(working_data)
    # New correlation matrix
    matrix = working_data[['Surface reelle bati','Nombre pieces principales','Surface terrain','Valeur fonciere']]
    mat_corr = matrix.corr().round(5)
    sns.heatmap(data=mat_corr, annot=True)
    

def estimate_property(code_insee, range, data_type, surface, ground_surface, nb_rooms):
    working_data = data_help.get_sells_from_insee_code(code_insee, data_type, range)
    if len(working_data) == 0:
        print('Cannot estimate property')
        return -1

    working_data = data_help.apply_isolation_forest(working_data)

    xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,                    colsample_bytree=1, max_depth=7)


    X =  working_data[['Surface reelle bati','Nombre pieces principales','Surface terrain']].values
    y = working_data['Valeur fonciere'].values
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y ,test_size=0.3)
    xgb.fit(X_train,y_train)

    score = xgb.score(X_train, y_train)  
    print("Training score for the dataset: %s percents" % round(score*100, 2))

    xNew = np.array([[surface, nb_rooms, ground_surface]]).reshape((1,-1))
    estimate = xgb.predict(xNew)

    return round(estimate[0], 2)



