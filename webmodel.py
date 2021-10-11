#Core pkgs
from sqlalchemy import engine
import streamlit as st

#Databse pkgs
import sqlite3
# SQL Connection to Sales
from sqlite3.dbapi2 import Date, connect
import sqlalchemy as sql
from sqlalchemy import create_engine
#from conn import UserInput
from sqlalchemy.orm import sessionmaker



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

quantity = st.sidebar.number_input("Enter a quantity number", min_value=0,max_value=500,step=1)
submit = st.sidebar.button("SUBMIT")

if submit:
    import sqlite3
    conn = sqlite3.connect('Database/sales.db')
    c = conn.cursor()
    st.title("Extracting dataset from Database")
    c.execute('SELECT * FROM sales')
    sales_data = c.fetchall()
    #sales_data = sales_data.columns.astype(str)

else:
    st.title("Extracting dataset from CSV files")
    sales_data = pd.read_excel('Resources/tracks_tavern_sales_data.xlsx')

def main():
    st.title('Welcome to Tavern Data')
    st.text("Using Streamlit")

    #product = ['beer', 'vodka', 'scotch/whiskey', 'nonalcoholic', 'side', 'appetizers', 'fish', 'special']
    map = ['pairplot', 'lmplot', 'barplot', 'heatmap']
    choice = st.sidebar.selectbox('Select Map to explore',map)
    #quantity = st.sidebar.number_input("Enter a number value", min_value=0,max_value=500,step=1)

    dataset = st.container()
    features = st.container()
    model_training = st.container()

    columns = st.columns((1,1))
    with columns[0]:
        #st.markdown(f"Quantity Number: {quantity}")
        st.header('Tavern Dataset')
        st.dataframe(sales_data)
        #st.subheader('Total Count per Product Type')
        #st.dataframe(sales_data.type.value_counts().head(10))
    with columns[1]:
        with dataset:
            #st.write(sales_data.head(20))
            sales_data['date'] = pd.to_datetime(sales_data['date'])
            main_types = ['beer', 'vodka', 'scotch/whiskey', 'nonalcoholic', 'side', 'appetizers', 'fish', 'special']
            
            #Beer DF
            beer_df = sales_data[(sales_data.type == "beer" )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            beer_df = beer_df.groupby(['date']).sum().rename(columns={'quantity': 'beer_qty'})

            #Vodka DF
            vodka_df = sales_data[(sales_data.type == "vodka" )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            vodka_df = vodka_df.groupby(['date']).sum().rename(columns={'quantity': 'vodka_qty'})

            #Scotch Whiskey DF
            scotch_df = sales_data[(sales_data.type == 'scotch/whiskey' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            scotch_df= scotch_df.groupby(['date']).sum().rename(columns={'quantity': 'scotch_qty'})

            # nonalcoholic DF
            nonalcoholic_df = sales_data[(sales_data.type == 'nonalcoholic' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            nonalcoholic_df = nonalcoholic_df.groupby(['date']).sum().rename(columns={'quantity': 'nonalcoholic_qty'})

            # side
            side_df = sales_data[(sales_data.type == 'side' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            side_df = side_df.groupby(['date']).sum().rename(columns={'quantity': 'side_qty'})

            # appetizers
            apps_df = sales_data[(sales_data.type == 'appetizers' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            apps_df = apps_df.groupby(['date']).sum().rename(columns={'quantity': 'apps_qty'})

            # fish
            fish_df = sales_data[(sales_data.type == 'fish' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            fish_df = fish_df.groupby(['date']).sum().rename(columns={'quantity': 'fish_qty'})

            # special
            special_df = sales_data[(sales_data.type == 'special' )].drop(columns=['item', 'item_code', 'unit_price','type', 'total_sales_amount'])
            special_df = special_df.groupby(['date']).sum().rename(columns={'quantity': 'special_qty'})
                    
        #with features:
            # Join features DF
            feature_df = ((((((beer_df.join(vodka_df, how='outer')).join(scotch_df, how='outer'))\
            .join(nonalcoholic_df, how = 'outer')).join(side_df, how='outer')).join(apps_df, how='outer'))\
                .join(fish_df, how='outer')).join(special_df, how = 'outer')
            st.write(feature_df.head(10))
            #st.bar_chart(feature_df.head(500))

            # Read Weather DF
            cols = ['dt','temp', 'temp_min', 'temp_max']
            weather_df = pd.read_csv('Resources/week_weather_summary.csv', index_col=['dt'], usecols=cols)
            weather_df.index = pd.to_datetime(weather_df.index)
            complete_df = feature_df.join(weather_df, how='outer').reset_index()
            complete_df.dropna(inplace=True)

            st.markdown(f"Map Name: {choice}")
            if (choice == 'pairplot'):
                st.subheader('Variable correlation')
                st.dataframe(complete_df.corr())
                fig_pair = sns.pairplot(complete_df)
                st.pyplot(fig_pair)
            elif(choice == 'lmplot'):
                fig_lm = sns.lmplot(x='beer_qty', y='apps_qty', data=complete_df, size=5)
                st.pyplot(fig_lm)
            elif(choice == 'barplot'):
                st.subheader('Visualize beer sales by month')
                complete_df['month'] = complete_df['index'].apply(lambda time: time.month)
                f,ax = plt.subplots(figsize=(15,10))
                ax.figure.savefig('file.png')
                st.write(sns.boxplot(x='month', y='apps_qty', data=complete_df))
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()
            elif(choice == 'heatmap'):
                st.subheader('Correlation heatmap')
                corr = complete_df.corr()
                cmap = sns.diverging_palette(220,10, as_cmap=True)
                f, ax = plt.subplots(figsize=(11,9))
                ax.figure.savefig('file.png')
                st.write(sns.heatmap(corr, cmap=cmap, center=0, square=True, linewidths=0.5))
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()
          

           
        #date = st.sidebar.date_input('Date', datetime.date(2019,1,1))
        
        with model_training:
            def seasonality():
                st.bar_chart(beer_df.groupby(['date']).sum().rename(columns={'quantity': 'beer_qty'}))

if __name__ == "__main__":
    main()