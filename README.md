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

In the first segment of the final project. We used Linear Regression in SKLearn to perform the analysis of the Tracks and Tavern sales and scientifically predict the future sales.

Datasets were loaded in data frame. We have two continuous variables to test the relationship between dates and total sales amount. With the use of regression model, it will help analyze the sales and the purchasing patterns on a particular days or certain times.  It will determine when and if the alcohol products will be in high demand. 

The data was split into a test size of 40%.  Based on the linear regression model, there’s no significant relationship between the date and total sales.  This means the slope of the best fit line will likely be close to zero.

**Scatter Plot for Linear Regression**   
![image](https://user-images.githubusercontent.com/83877498/135734354-71bff064-4f87-4046-81f8-21ae460f00d1.png)

Another machine learning model we used was Pycaret.  The output below shows that the perfect collinearity was removed.  This is because we don’t want to lose precision of our estimated coefficients.

**Pycaret setup results**

![image](https://user-images.githubusercontent.com/83877498/135734389-562ac0a0-1c67-4293-9446-a9cb7177d308.png)

Running the compare models, Bayesian Ridge, Passive Aggressive Regressor gave better results, meaning these regression models will likely be the best Machine Learning Models to apply.

**Compare models methods**

![image](https://user-images.githubusercontent.com/83877498/135734377-a2bbed61-4eed-4c89-b67e-672d864d7b53.png)




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
