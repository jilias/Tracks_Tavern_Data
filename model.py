import pandas as pd
import numpy as np
import pickle as p


#access settings
data_path = './ML_Model/'
data_file = 'sales.pkl'
model_file = 'linear.pkl'

def load_data():
    df = p.load(open(data_path+'sales.pkl','rb'))
    return df

def load_model():
    loaded_model = p.load(open(data_path+'linear.pkl','rb'))
    return loaded_model


