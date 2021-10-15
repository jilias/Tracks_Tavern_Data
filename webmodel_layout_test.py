#Core pkgs
from numpy.core import numeric
from scipy.sparse import data
import streamlit as st
import model

#EDA pkgs
import pandas as pd
import numpy as np
import datetime

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

topic = ['About', 'Sales', 'Beer Predictor', 'Grouping']
selector = st.selectbox('', topic)

def about():
    st.markdown("""""
        Overview
Tracks is a small business located in Milwaukee, Wisconsin currently owned by Michael Rebers. 7 days a week, they offer a variety of choice in both food and drinks while providing a place to view many different sports teams and games. In addition, they run volleyball leagues throughout the summer.

Data Source
Because it is a local neighborhood bar serving both drinks and foods Monday thru Wednesday, the data set primarily focus on the sales of food, drinks, and other items sold at the Tavern. We received the dataset directly from the client via a flash drive which includes their weekly data in both .csv and .xlsx format. The data contains sales from 2019 to 2021 on a weekly basis. In addition, we are using weather data from openweather.com to analysis the weather in the Milwaukee area, specifically 53212 zip code. We choose this particular data source and project for the following opportunities

A chance to work with local business and real world data
Providing an unique situation where we work with actual client and allow to gather business requirements and scope the project
Working with a realistic data set that requires primary exploration, cleaning, and standardization before exploration with machine learning and other analysis
A dataset that requirements further contextual knowledge challenging the importance of context in hand with content
    """)

def sales():
    st.image("./imgs/pct_sales.jpg", width=600)
    st.image("./imgs/weekly_sales_chart.jpg", width=600)

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



    complete_df =  model.load_data()
    prediction_df = model.load_model()

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