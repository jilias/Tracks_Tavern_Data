#Core pkgs
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

st.image("./imgs/logo.jpg", use_column_width=False)
html_style = """
<div style = "background-color:dark">
<h2 style = "color:white;text-align:center;">Welcome to Tracks and Tavern Grille </h3>
</div>
"""
st.markdown(html_style,unsafe_allow_html=True)
def main():
   

    st.title('Welcome to Tavern Data')
    columns = st.columns((2,2,2))
    with columns[0]:
        about = st.button("About")
    with columns[1]:
        data = st.button("Data")
    with columns[2]:
        ml = st.button("Model")

    dataset = st.container()
    features = st.container()
    model_training = st.container()

    if about:
        st.header('About Tavern')
    if data:
        with dataset:
            st.subheader("loading data from pickle")
            sales_data = model.load_data()
            st.dataframe(sales_data)
    if ml:
        complete_df =  model.load_model()
        map = ['pairplot', 'lmplot', 'barplot', 'heatmap']
        choice = st.sidebar.radio('Navigation',map)
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

if __name__ == "__main__":
    main()