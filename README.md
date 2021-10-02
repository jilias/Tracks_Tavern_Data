# Tracks_Tavern_Data

## Segment 1
#### Overview
We have chosen to review the Tracks Tavern sales data on both food and drinks and see how they correlate with the local weather. This provides an opportunity to work with a client and scope out a project for a local business.

#### Team
Our team communicates via email and Slack to keep up to date. As well, we meet through Zoom to discuss in real time. We have each been assigned our branch to work with Jess Ilias as the individual approving merge request.
- Aimerica Mangilit
- George Calvo
- Jess Ilias
- Jose Alcivar

#### Description of Data Source
We received csv files provided directly from the client which were converted to sqlite. We sourced the weather data from openweather.org. Together we will union the data to create one massive data frame.
#### Questions/Scope
Initially the client wanted to see the sales and inventory analysis. As a team we decided to incorporate the weather data to see what liquors and food sold best in which season. We will further analyze the data to see how the liquors and food sales correlate with one another. As our data model, we are looking to use linear regression, unsupervised machine learning, and Facebook Prophet. 
![Tracks_Tavern_Diagram_Planning](https://user-images.githubusercontent.com/82242081/135001252-b133bcc2-9ec4-41a1-9e37-b50111f4eab9.jpeg)
### Update
##### Aimerica Mangilit
##### George Calvo  

For the initial stages of the final project, we gather the data from Tracks taverns as single week csv files for period starting February 2019 up to September 2021, which we concatenated into a single csv file containing all the weekly sales data.  
With the data into a single file, we performed an initial exploration into the data to have wide view of track taverns sales patterns. Create charts for weekly sales, pie chart of sales by liquor and food categories, plus word cloud to visualize most common items. These charts are shown below:  

**Chart 1: Weekly sales**   
![image](https://user-images.githubusercontent.com/82473940/135688380-21c8e85f-fa8a-41e0-97b7-9df3a85e8b46.png)

**Chart 2: Percentage of liquor and food sales**  
![image](https://user-images.githubusercontent.com/82473940/135688451-25839fa1-ef21-453d-a4eb-05a2eb426514.png)

**Chart 3: Cloud Word Chart**  
![image](https://user-images.githubusercontent.com/82473940/135688526-2f8bd792-a501-42fb-8482-905d10f25f46.png)

##### Jess Ilias
##### Jose Alcivar

###### Database Set Up

As a group, we decided the best system for us to use would be **SQLite**. This is because it has a great advantage in being both local and portable. It helps us to keep a copy of the database in our local repo so we may reference it as needed, and thanks to libraries like **SQLAlchemy** and **Pandas** we can simply make a connection to our database and make queries SQL-style if we need to pull specific data from it.

In order to import our files from our current format (csv) to our database, we ran code as described in the [csvToSQLite](csvToSQLite.ipynb) file. We used the **sqlalchemy** library for python and the **to_sql()** method from Pandas. We saved our data on a [db file](data/sales.db), which for the time being contains two tables: a concatenated sales data which holds the sales information of both food and drinks and our weather data, which holds the (weekly) historical weather information. The file can be viewed in a SQLite browser such as DB Browser.

An advantage of using our code is that it helps set up the database with new csv files that may be coming. In the following weeks, as we proceed to clean our data and add columns necessary for our analysis, we can easily add them using SQL code and integrate it into a dataframe.

A challenge we encounter when setting up the database was the addition of relationships between tables via PRIMARY and FOREIGN KEYS, as per our [schema](Schema.txt). This issue stems from limitations of both SQLite and the to_sql() method. Though doable through a workaround, it is a process that we deem not necessary for the time being, but we may come back to it if we feel we can gain an advantage from it.
