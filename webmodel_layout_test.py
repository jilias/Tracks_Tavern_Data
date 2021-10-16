#Core pkgs
from numpy.core import numeric
from scipy.sparse import data
import streamlit as st
import model

#EDA pkgs
import pandas as pd
import numpy as np
import datetime
from pathlib import Path

#Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

#ML pkgs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.metrics import confusion_matrix, accuracy_score

# importing stat functions
import statsmodels.api as sm
import statsmodels.formula.api as smf




st.set_page_config(layout="wide") 

# Dataframes and data transformation

complete_df =  model.load_data()
prediction_df = model.load_model()
df = model.load_df()

sales_df = complete_df.drop(['temp', 'temp_min', 'temp_max', 'month'], axis=1)



# Header
r1_1, r1_2 = st.columns((1,4))


with r1_1:
    st.image("./imgs/logo.jpg", width=200)

with r1_2:
    st.title("Track Tavern and Grille Dashboard") 
    st.markdown(
        "http://www.trackstavernmilwaukee.org  |"
        "   1020 E Locust St - Milwaukee, WI 53212"
    )
    st.markdown(
        "Tracks is a small business located in Milwaukee, Wisconsin currently owned by Michael Rebers."
        "7 days a week, they offer a variety of choice in both food and drinks while providing a place"
        "to view many different sports teams and games. In addition, they run volleyball leagues throughout the summer."
)

# Sidebar Selectors
topic = ['About', 'Sales', 'Beer Predictor', 'Grouping']
st.sidebar.title("Select topic")
selector = st.sidebar.selectbox('', topic)
st.sidebar.markdown('<br>',unsafe_allow_html=True )
st.sidebar.image("./imgs/web_listing.jpg")

# Functions for different options

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# ABOUT

def about():
    about_md = read_markdown_file("README.md")
    st.markdown(about_md, unsafe_allow_html=True)

# SALES

def sales():
    sr1_1, sr1_2, sr1_3 = st.columns(3)
    
    with sr1_1:
        st.image("./imgs/weekly_sales_chart.jpg", width=600)
    with sr1_2:
        st.image("./imgs/weekly_licor_sales_chart.jpg", width=600)
    with sr1_3:
        st.markdown('## Sales Categories')
        st.image("./imgs/pct_sales.jpg", width=600)
    
    sr2_1, sr2_2 = st.columns((2,8))

    with sr2_1:
        st.markdown('## Top Ten Item Types')
        st.dataframe(df.type.value_counts().head(10))
    
    with sr2_2:
        st.markdown('## Sales Quantities by Features')
        salesbar = st.bar_chart(sales_df.sum(), width=5)

    



# BEER

def beer_predictor():
    html_style = """
    <h2>Beer Prediction Model</h2>
    <p> Predicting Beer quantity sold on a week based on Linear Regression
    Machine Learning Model. To determine which features where the best to build out model, we first determine if there was
    any correlation between out features. Using seaborn pair plot and box plot we are able to visualize the corralations
    </p>
    """

    r2_1, r2_2 = st.columns(2)

    with r2_1:
        st.write(html_style,unsafe_allow_html=True)



    r3_1, r3_2 = st.columns((1,5))

    with r3_1:
        analysis = st.radio(
            'Menu', ('Correlation Pairplot', 'Correlation Table', 'Beer Sales By Month', 'Correlation Heatmap', 'Predict Beer Sales Qty' )
        )

    with r3_2:
        if analysis == 'Correlation Pairplot':
            st.subheader(analysis)
            st.markdown("""
            Using the scatter plots below, we determine which feature presents correlation with each other.
            The Features that present correlation will be use for our Machine Learning Model.
            """)
            st.image("./imgs/pairgrid.jpg", width=600)

            

        elif analysis == 'Correlation Table':
            st.subheader(analysis)
            st.markdown("""
            The correlation table below further confirm the observation from the pairplots. We will drop from our
            model the feature that present no correlation.
            """)
            st.dataframe(complete_df.corr())

        elif analysis == 'Beer Sales By Month':
            st.subheader(analysis)
            st.markdown('The sales by month column is used to see if there is any seasonality that can help our model')
            st.image("./imgs/barplot.jpg", width=600)
        
        elif analysis == 'Correlation Heatmap':
            st.subheader(analysis)
            st.markdown("""
            The heatmap is another way to visualize the corralation between features.
            """)
            st.image("./imgs/heatmap.jpg", width=600)

        elif analysis == 'Predict Beer Sales Qty':
            st.subheader(analysis)
            st.markdown("""
            Enter weekly sales value for each feature
            """)
            vodka_qty = st.number_input('Vodka', value=380, min_value=1, max_value=None)
            scotch_qty = st.number_input('Scotch', value=212, min_value=1, max_value=None)
            nonalcoholic_qty = st.number_input('NonAlcoholic', value=88, min_value=1, max_value=None)
            side_qty = st.number_input('Side', value=58, min_value=1, max_value=None) 
            apps_qty = st.number_input('Appetizer', value=137, min_value=1, max_value=None)
            special_qty = st.number_input('Special', value=68, min_value=1, max_value=None)
            month = st.number_input('Month', value=5, min_value=1, max_value=12) 
            predict = 60.23 + vodka_qty * 0.19331991 + scotch_qty * 0.60362646 + nonalcoholic_qty * 1.37073889 + side_qty * 1.73370093 + apps_qty * 0.51365566 + special_qty * 0.5456311 - month * 5.06256333
            st.markdown("""
            #  Predicted Weekly Beer Sales Quantity:""")
            st.metric(label="", value=int(predict))

   
# Main functions

def main():
    if selector == 'About':
        about()
    elif selector == 'Sales':
        sales()
    elif selector == 'Beer Predictor':
        beer_predictor()
    elif selector == 'Grouping':
        st.write('TEST')



if __name__ == "__main__":
     main()