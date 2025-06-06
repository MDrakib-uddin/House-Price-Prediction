# util.py

import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

MODEL_PATH = './artifacts/banglore_home_prices_model.pickle'
COLUMNS_PATH = './artifacts/columns.json'

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    if __model:
        return round(__model.predict([x])[0], 2)
    else:
        raise Exception("Model not loaded.")

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    with open(COLUMNS_PATH, "r") as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __locations = __data_columns[3:]

    with open(MODEL_PATH, 'rb') as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully.")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
