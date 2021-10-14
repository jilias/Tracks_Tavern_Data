#Core pkgs
from numpy.core import numeric
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

st.image("./imgs/logo.jpg", use_column_width=False)
html_style = """
<div style = "background-color:dark">
<h2 style = "color:white;text-align:center;">Welcome to Tracks and Tavern Grille </h3>
</div>
"""
st.write(html_style,unsafe_allow_html=True)
complete_df =  model.load_data()
prediction_df = model.load_model()
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
    model_training = st.container()
    stats = st.container()

    #if about:
    #st.header('About Tavern')
    #if data:
    with dataset:
        st.dataframe(complete_df)
    #if ml:
    with model_training:
        st.subheader('Tracks Tavern Linear Regression Machine Learning Model')

        st.markdown("""
        The purpose of this Machine Learning model is to explore if we can use the **sales data** since february 2019 and the **weather information** to predict sales information. 
        We will analyze the sales of different categories, compare with weather for the period and look for any correlations that can help us in our prediction.
        """)
        st.markdown('Combination of sales dataset and weather dataset')
        st.dataframe(complete_df)

        #Pairplot
        if st.button('Intercorrelation Pairplot'):
            fig_pair = sns.pairplot(complete_df)
            st.pyplot(fig_pair)
            
        if st.button('Intercorrelation Lmplot'):
            st.subheader('Variable correlation')
            st.markdown("""
            From the scatter plots above, we do not see a correlation of any feature with the weather, this might be because our data is affected by covid 19 closures and/or that since our data is for weekly sales, any weather impact on sales can be diluted. 
            Nonetheless, since we spot corralations with the weather, for our model we will drop the temperature columns.
            Below with a table with the corralation values corrabolating the fact that there is no corralation between our sales data and the weather.
            """)
            st.dataframe(complete_df.corr())
            fig_lm = sns.lmplot(x='beer_qty', y='apps_qty', data=complete_df, size=5)
            st.pyplot(fig_lm)
            
        if st.button('Intercorrelation Boxplot'):
            st.markdown('We will create a month column and use it to see if there is any seasonality that can help our model')
            st.subheader('Visualize beer sales by month')
            complete_df['month'] = complete_df['index'].apply(lambda time: time.month)
            f,ax = plt.subplots(figsize=(15,10))
            #ax.figure.savefig('file.png')
            st.write(sns.boxplot(x='month', y='apps_qty', data=complete_df))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            
        if st.button('Intercorrelation Heatmap'):
            st.subheader('Correlation heatmap')
            corr = complete_df.corr()
            cmap = sns.diverging_palette(220,10, as_cmap=True)
            f, ax = plt.subplots(figsize=(11,9))
            ax.figure.savefig('file.png')
            st.write(sns.heatmap(corr, cmap=cmap, center=0, square=True, linewidths=0.5))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    with stats:
        # Creating our feature dateframe as X and our dependant df as y ('scotch_qty')
        def user_input():
            vodka_qty = st.sidebar.number_input('Vodka' )
            scotch_qty = st.sidebar.number_input('Scotch')
            nonalcoholic_qty = st.sidebar.number_input('NonAlcoholic')
            side_qty = st.sidebar.number_input('Side')
            apps_qty = st.sidebar.number_input('Appetizer')
            special_qty = st.sidebar.number_input('Special')
            month = st.sidebar.number_input('Month')


            data = {'vodka_qty': vodka_qty,
                    'scotch_qty': scotch_qty,
                    'nonalcoholic_qty': nonalcoholic_qty,
                    'side_qty': side_qty,
                    'apps_qty': apps_qty,
                    'special_qty': special_qty,
                    'month': month}
            features = pd.DataFrame(data, index=[0])
            return features
        coef  = { 0.19331991,        0.60362646,  1.37073889,  1.73370093,  0.51365566,
        0.5456311 , -5.06256333 }
            
        df = user_input()

        st.subheader('User Input parameters')
        st.write(df)

        beer = {'beer_qty': st.sidebar.slider('Beer', 1,15,7)}
        
        X = df
        y = complete_df['beer_qty']
        
        # Creating a Prediction DF to compare out test y with our predicted y.
        if st.button('Prediction'):
           
           #prediction_df['y_pred'] = model.predict(df)
           predict = 60.23 + df['vodka_qty'] * 0.19 + df['scotch_qty'] * 0.60 + df['nonalcoholic_qty'] * 1.37 + df['side_qty'] * 1.73 + df['apps_qty'] * 0.51 + df['special_qty'] * 0.54 - df['month'] * 5.06
           st.write(predict)
           st.markdown("""
            From the scatter plots above, we do not see a correlation of any feature with the weather, this might be because our data is affected by covid 19 closures and/or that since our data is for weekly sales, any weather impact on sales can be diluted. 
            Nonetheless, since we spot corralations with the weather {predict}, for our model we will drop the temperature columns.
            Below with a table with the corralation values corrabolating the fact that there is no corralation between our sales data and the weather.
            """)
           
           




        #date = st.sidebar.date_input('Date', datetime.date(2019,1,1))

if __name__ == "__main__":
    main()