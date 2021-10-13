# Tracks Tavern Data
## Overview
Tracks is a small business located in Milwaukee, Wisconsin currently owned by Michael Rebers. 7 days a week, they offer a variety of choice in both food and drinks while providing a place to view many different sports teams and games. In addition, they run volleyball leagues throughout the summer.

## Data Source
Because it is a local neighborhood bar serving both drinks and foods Monday thru Wednesday, the data set primarily focus on the sales of food, drinks, and other items sold at the Tavern. We received the dataset directly from the client via a flash drive which includes their weekly data in both .csv and .xlsx format. The data contains sales from 2019 to 2021 on a weekly basis. In addition, we are using weather data from openweather.com to analysis the weather in the Milwaukee area, specifically 53212 zip code. We choose this particular data source and project for the following opportunities
- A chance to work with local business and real world data
- Providing an unique situation where we work with actual client and allow to gather business requirements and scope the project
- Working with a realistic data set that requires primary exploration, cleaning, and standardization before exploration with machine learning and other analysis
- A dataset that requirements further contextual knowledge challenging the importance of context in hand with content

## Questions/Scope
As a team we decided to incorporate the weather data to see what liquors and food sold best in which season. We will further analyze the data to see how the liquors and food sales correlate with one another. As our data model, we are looking to use linear regression, unsupervised machine learning, and Facebook Prophet.
- Does the weather influence the sales?
- What items can be best grouped together?
- What does an average week look like at Tracks?
- What items are sold best together?

![Tracks_Tavern_Diagram_Planning](https://user-images.githubusercontent.com/82242081/135001252-b133bcc2-9ec4-41a1-9e37-b50111f4eab9.jpeg)

## Meet the Team
While our team has particular set of deliverables and skills, we have found ourselves overlapping in responsiblities and bringing in fresh ideas and outlooks. As we met over Zoom calls multiple times a week and continued further communications on Slack, we constantly gave one another deliverables to meet and helped hone each other, the data, and analysis. Together we have explored, managed, and analyzed the dataset.
#### Aimerica Mangilit
While Aimerica lent her skills in exploring the dataset through supervised machine learning, she has shined as the lead in our dashboard creation and helping our analysis and ideas come to life. Through her work, we are able to have an interactive space for the data.
#### George Calvo
George ventured in various ways with the data. His initial expeditions of the data provided a high level overview and grew into a specified expeditions through Facebook Prophet which led to using seaborn as our best option for machine learning and further analyzations. In gathering our other machine learning models, George helped narrow down the data and helped guide us in answering some of our questions.
#### Jess Ilias
#### Jose Alcivar
As a detailed individual, Jose took charge in creating a database that was suitable and manageable for the project. By using SQLite, Jose provided us a way to use sqlalchemy and pandas to feed into our coding and create an ease of access to the data. Not only ease of access but he has taken two different sets of data and joined them for our continued use. In addition to the database support, Jose as well took part in our machine learning explorations and helped provided a ranking grouping of the Tracks Tavern products types to see what top products grouped best together.

## Pre-Exploration
Before diving immediately into the project, we each explored the data in multiple different ways including but not limited to linear regression, unsupervised/supervised models, and Facebook Prophet. We used linear regression in sklearn to perform the analysis of the Tracks Tavern sales and attempted scientifically predict the future sales.
Datasets were loaded into a pandas dataframe in order to create and test two continuous variables and observe the relationship between dates and total sales amount. With the use of regression model, we hoped to analyze the sales and the purchasing patterns on a particular weeks or certain times in order to determine what products are in demand. 
The data was split into a test size of 40%.  Based on the linear regression model, it was concluded there’s no significant relationship between the date and total sales. This means the slope of the best fit line will likely be close to zero.

**Scatter Plot for Linear Regression**   
![image](https://user-images.githubusercontent.com/83877498/135734354-71bff064-4f87-4046-81f8-21ae460f00d1.png)

Another machine learning model we used was Pycaret.  The output below shows that the perfect collinearity was removed.  This is because we don’t want to lose precision of our estimated coefficients.

**Pycaret setup results**

![image](https://user-images.githubusercontent.com/83877498/135734389-562ac0a0-1c67-4293-9446-a9cb7177d308.png)

Running the compare models, Bayesian Ridge, Passive Aggressive Regressor gave better results, meaning these regression models will likely be the best Machine Learning Models to apply.

**Compare models methods**

![image](https://user-images.githubusercontent.com/83877498/135734377-a2bbed61-4eed-4c89-b67e-672d864d7b53.png)

For the initial stages of the final project, we gather the data from the taverns as single week csv files for period starting February 2019 up to September 2021, which we concatenated into a single csv file containing all the weekly sales data.  
With the data into a single file, we performed an initial exploration into the data to have wide view of the sales patterns. Create charts for weekly sales, pie chart of sales by liquor and food categories, plus word cloud to visualize most common items. These charts are shown below:  

**Chart 1: Weekly sales**   
![image](https://user-images.githubusercontent.com/82473940/135688380-21c8e85f-fa8a-41e0-97b7-9df3a85e8b46.png)

**Chart 2: Percentage of liquor and food sales**  
![image](https://user-images.githubusercontent.com/82473940/135688451-25839fa1-ef21-453d-a4eb-05a2eb426514.png)

**Chart 3: Cloud Word Chart**  
![image](https://user-images.githubusercontent.com/82473940/135688526-2f8bd792-a501-42fb-8482-905d10f25f46.png)

## Machine Learning - Supervised and Unsupervised

### Tracks Tavern Linear Regression Machine Learning Model
The purpose of this Machine Learning model is to explore if we can use the sales data since february 2019 and the weather information to predict sales information. We will analyze the sales of different categories, compare with weather for the period and look for any correlations that can help us in our prediction.
In using the value counts we determined the following main categories as the feature of our machine learning model:

- Beer
- Scotch/Whiskey
- Side
- Fish
- Vodka
- NonAlcoholic
- Appetizers
- Specials

We will create a column for each type grouping by date summarizing the quantity per date.
Within in our model, we gathered historical weather data for the area where Tracks Tavern resides from openweather.com and cleaned and transform to reflect a weekly average weather.
For our model we will be focusing on the average temp, minimum temp, and maximum temp.
From the scatter plots, we do not see a correlation of any feature with the weather possibly due to Covid-19 closures or the weekly sales may impact the scaling for the weather data and dilute it.
![download (2)](https://user-images.githubusercontent.com/82242081/136715093-e7addc6c-4563-41d6-9202-4054d715a846.png)
The correlation graph in additions supports that there is no clear correlation between weather and sales data![download (1)](https://user-images.githubusercontent.com/82242081/136715103-127e0289-c0b2-4c68-bd89-063dbc16f7ab.png)
From the bar graph we spot seasonally with sales declining in November, December and January. In addition, we clearly see a large spike in May just before summer begins.
![download](https://user-images.githubusercontent.com/82242081/136715112-9903b968-c29f-404d-988b-59b5b42fc82c.png)

### Grouping Products by Sales ML model
This model is will be seeking what combination of products group best together.
We are seeking to use the different types of food through Kmeans Clustering to see how best they work together.
Types of food and drink may belong to multiple groups, however, individual products can only belong to one type.
Items are scaled so that they will be weighed equally in the model.
By using Kmeans, we can help understand how many clusterings there could possibly be.
The Kmeans in addition will be quicker in predicting the amount of clusters rather than the use of hierarchical clustering.
Once the cluseters are found and the types are grouped, the model can use revenue data to determine the most successful of the groups.
After running our model and finding 2,499 groupings , we discover that the most successful group is that one composed by the types Fish, Burger, Beer, Hard Cider and Other. These are the most revenue-generating type of items, at an average of $13.57 per unit of product sold. These are our following top ten groupings:
1. Fish, Burger, Beer, Hard Cider, Other
6. Burger, Beer, Breakfast, Fish, Appetizers, Other
2. Breakfast, Fish, Beer, Brandy, Hard Cider
7. Breakfast, Fish, Beer, Brandy, Other
3. Beer, Fish, Hard Cider, Breakfast, Brandy, Appetizers
8. Fish, Other, Burger, Beer, Brandy
4. Beer, Fish, Hard Cider, Scotch/Whiskey, Brandy
9. Beer, Tequila, Fish, Hard Cider, Breakfast, Sandwich
5. Burger, Fish, Scotch/Whiskey, Beer, Brandy
10. Fish, Appetizers, Beer,  Burger, Brandy

## Database
As a group, we decided the best system for us to use would be **SQLite**. This is because it has a great advantage in being both local and portable. It helps us to keep a copy of the database in our local repo so we may reference it as needed, and thanks to libraries like **SQLAlchemy** and **Pandas** we can simply make a connection to our database and make queries SQL-style if we need to pull specific data from it.

In order to import our files from our current format (csv) to our database, we ran a code as described in the [csvToSQLite](processing/csvToSQLite.ipynb) file. We used the **sqlalchemy** library for python and the **to_sql()** method from Pandas. We saved our data on a [db file](Database/sales.db), which for the time being contains two tables: 

- A concatenated sales data which holds the sales information of both food and drinks 
- Our weather data, which holds the (weekly) historical weather information. 

The file can be viewed in a SQLite browser such as DB Browser. An advantage of using our code is that it helps set up the database with new csv files that may be coming. As we proceeded to clean our data and add columns necessary for our analysis, we can easily add them using SQL code and integrate it into a dataframe.

A challenge we encountered when setting up the database was the addition of relationships between tables via PRIMARY and FOREIGN KEYS, as per our [schema](Database/Schema.txt). This issue stems from limitations of both SQLite and the to_sql() method. Though doable through a workaround, it is a process that we deem not necessary for the time being, but we may come back to it if we feel we can gain an advantage from it.

###### ERD

![ERD](imgs/ERD.png)

## Analysis

## Dashboard

https://github.com/jilias/Tracks_Tavern_Data/blob/main/webmodel.py

## Presentation
https://docs.google.com/presentation/d/1VRICFz63dp378-NGYYzXR_Gvo7oOsKVnM7d9bCKS_gs/edit?usp=sharing

## Final Conclusion
