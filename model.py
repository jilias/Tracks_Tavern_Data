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

def score():
    linear_regresion_df =  load_data()

    X = linear_regresion_df.drop(['index','beer_qty', 'fish_qty', 'temp', 'temp_min', 'temp_max'], axis=1)
    y = linear_regresion_df['beer_qty']

    # Split the data into train and test 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # Create the linear regression model

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    score = model.score(X_train, y_train)
    return score

def model():
    linear_regresion_df =  load_data()

    X = linear_regresion_df.drop(['index','beer_qty', 'fish_qty', 'temp', 'temp_min', 'temp_max'], axis=1)
    y = linear_regresion_df['beer_qty']

    # Split the data into train and test 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # Create the linear regression model

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model