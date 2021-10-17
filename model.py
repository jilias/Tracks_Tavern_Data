import pandas as pd
import numpy as np
import pickle as p


#access settings
data_path = './ML_Model/'
data_file = 'sales.pkl'
model_file = 'linear.pkl'
df_file = 'df.pkl'
group_file = 'group_dict.pkl'
revenue_file = 'revenue.pkl'
type_file = 'individual_type.pkl'


def load_data():
    global df
    df = p.load(open(data_path+'sales.pkl','rb'))
    return df

def load_model():
    global loaded_model
    loaded_model = p.load(open(data_path+'linear.pkl','rb'))
    return loaded_model

def load_df():
    global sales
    sales = p.load(open(data_path+'df.pkl','rb'))
    return sales
def load_group():
    global loaded_model
    loaded_group = p.load(open(data_path+'group_dict.pkl','rb'))
    return loaded_group

def load_revenue():
    global loaded_revenue
    loaded_revenue = p.load(open(data_path+'revenue.pkl','rb'))
    return loaded_revenue




