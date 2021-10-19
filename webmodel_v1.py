#Core pkgs
import streamlit as st
import model

#EDA pkgs
import pandas as pd
from pathlib import Path

#Data Viz Pkgs
import plotly.express as px

# Streamlit Page Configuration
st.set_page_config(layout="wide") 

# Unpacking pickle files from model.py

complete_df =  model.load_data()
prediction_df = model.load_model()
df = model.load_df()
revenue_df = model.load_revenue()
group_dict = model.load_group()
score = model.score()
model = model.model()

format_score = "{:.4f}".format(score)



# Sales DF
sales_df = complete_df.drop(['temp', 'temp_min', 'temp_max', 'month'], axis=1)

# Creating Group DF to load the treemap plot
groups_df = pd.DataFrame.from_dict(group_dict, orient='index').sort_values([0, 1, 2, 3, 4, 5])

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
topic = ['About', 'Sales', 'Beer Predictor', 'Pairing']
st.sidebar.title("Select topic")
selector = st.sidebar.selectbox('', topic)
st.sidebar.markdown('<br>',unsafe_allow_html=True )
st.sidebar.image("./imgs/web_listing.jpg")
st.sidebar.write("Meet the team:")
st.sidebar.markdown("""
    - Aimerica Mangilit
    - George Calvo
    - Jess Ilias
    - Jose Alcivar
    """)

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
        st.image("./imgs/weekly_sales_chart.jpg", use_column_width=True)
    with sr1_2:
        st.image("./imgs/weekly_licor_sales_chart.jpg", use_column_width=True)
    with sr1_3:
        st.markdown('## Sales Categories')
        st.image("./imgs/pct_sales.jpg", use_column_width=True)
    
    sr2_1, sr2_2 = st.columns((2,8))

    with sr2_1:
        st.markdown('## Top Ten Item Types')
        st.dataframe(df.type.value_counts().head(10))
    
    with sr2_2:
        st.markdown('## Sales Quantities by Features')
        salesbar = st.bar_chart(sales_df.sum(), width=50)


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
            st.image("./imgs/pairgrid.jpg", use_column_width=True)

            

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
            st.image("./imgs/barplot.jpg", use_column_width=True)
        
        elif analysis == 'Correlation Heatmap':
            st.subheader(analysis)
            st.markdown("""
            The heatmap is another way to visualize the corralation between features.
            """)
            st.image("./imgs/heatmap.jpg", use_column_width=True)

        elif analysis == 'Predict Beer Sales Qty':
            st.subheader(analysis)
            st.markdown("""
            Enter weekly sales value for each feature
            """)
            # User Value Inputs
            vodka_qty = st.number_input('Vodka', value=380, min_value=1, max_value=None)
            scotch_qty = st.number_input('Scotch', value=212, min_value=1, max_value=None)
            nonalcoholic_qty = st.number_input('NonAlcoholic', value=88, min_value=1, max_value=None)
            side_qty = st.number_input('Side', value=58, min_value=1, max_value=None) 
            apps_qty = st.number_input('Appetizer', value=137, min_value=1, max_value=None)
            special_qty = st.number_input('Special', value=68, min_value=1, max_value=None)
            month = st.number_input('Month', value=5, min_value=1, max_value=12) 

            # Dataframe with user inputs
            user_input = pd.DataFrame({'vodka_qty':[vodka_qty],'scotch_qty':[scotch_qty],'nonalcoholic_qty':[nonalcoholic_qty],
            'side_qty':[side_qty],'apps_qty':[apps_qty],'special_qty':[special_qty],'month':[month]})

            # Use user inputs to predict beer quantity sales

            predict = model.predict(user_input)
            st.markdown("""
            #  Predicted Weekly Beer Sales Quantity:""")
            st.metric(label="", value=int(predict))
            st.markdown("""
            #  The Model's score used in this prediction is:""")
            st.metric(label="", value=float(format_score))

# Pairing Function

def pairing():
    st.subheader("Pairing")
    st.markdown("""
            Using unsupervised learning and kmeans to create clusters or gropus of drinks and foods items,
            the model can recommend the most sucessful groups or pairing in terms of revenue for a selected food or drink type.
            """)

    

    choice_type = st.selectbox("Enter type of Product:", ["Vodka","Scotch/Whiskey","Appetizers","Sandwich","Rum","Fish","Burger","NonAlcoholic","Side","Tequila","Bourbon","Breakfast","Liqueur","Brandy","Cocktail","Hard Seltzer","Wine","Entree","Gin","Hard Cider","Special","Salad","Happy Hour","Other","Specialty Shots","NO TYPE"])
    def recommend(type_):
        top_groups = revenue_df.sort_values("revenue_per_unit", axis=0, ascending=False)
        groups_with_element = []
        
        #we look for every group that has it
        for key in group_dict:
            #if the elements in the recommended group is true
            if all(x in group_dict[key] for x in type_):
                groups_with_element.append(key)
                
        if len(groups_with_element) == 0:
            return print("We do not have recommendations for you")
            
        win_key = groups_with_element[0]
        win_rev_0 = top_groups['revenue_per_unit'][win_key] #old revenue
        for key in groups_with_element:
            win_rev_1 = top_groups['revenue_per_unit'][key] #new revenue
            #if the new revenue is bigger than the old revenue
            if win_rev_1 > win_rev_0:
                #that key becomes the new win key
                win_key = key
                #and its revenue becomes old revenue
                win_rev_0 = win_rev_1
        recommend_list = group_dict[win_key]
        return recommend_list

    if st.button('Recommendation'):
        group = recommend([choice_type]) 
        st.markdown("We recommend group: ")
        st.markdown(group)
    st.subheader("Plotly Treemap for most revenue generating pairing")
    fig = px.treemap(groups_df, path=[0, 1, 2, 3, 4])
    fig.update_traces(root_color="lightgrey")
    st.plotly_chart(fig, use_container_width=True)

        

# Main functions

def main():
    if selector == 'About':
        about()
    elif selector == 'Sales':
        sales()
    elif selector == 'Beer Predictor':
        beer_predictor()
    elif selector == 'Pairing':
        pairing()



if __name__ == "__main__":
     main()