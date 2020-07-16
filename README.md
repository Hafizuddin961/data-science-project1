# data-science-project1
This my first full project on data science that in include data collection using web scrapper, cleaning the data, make Exploratory Data 
Analysis (EDA) and applying machine learning model to estimate data scientist salary

# Data Science Salary Estimator: Project Overview
* Created a model that estimates data science salaries with result of Mean Absolute Error (MAE) ~$11K 
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Using Linear, Lasso, and Random Forest Regressors model and optimized them using GridsearchCV

# Data Collection
Getting data from Glassdoor website and extract them using web scraper. The attribute that collected are:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

# Data Cleaning
Cleaned up the data and extract the important features such as:
* skill requirement e.g. python, R, AWS
* Standardized and specified the job title e.g. Junior Data Scientist, Senior Data Scientist, Manager, etc.
* Standardized the job location name based on its state e.g. CA for California, FL for Florida, Germany, ID for India, etc.
* Convert some number from string format to integer format for easy in process EDA

# Exploratory Data Analysis (EDA)
Make data visulization to get easier understanding of the data and make descriptive analysis after that<br/>
Here the example of result:<br/>
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/avg-salary.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/hist%20rating.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/heatmap.png)<br/>
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/graf-ownership.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/graph-revenue.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/bot-plot-rating.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/bot-plot-salary.png)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/pivot-seniority.JPG)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/pivot-sector.JPG)
![alt text](https://github.com/Hafizuddin961/data-science-project1/blob/master/example%20result/revenue-pivot.JPG)

# Model Building & performance
Transformed the categorical variables into dummy variables. then, split the data into train and tests sets with a test size of 20%.
Tried three different models and evaluated them using Mean Absolute Error. 

*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67


## Reference and more info
https://github.com/PlayingNumbers/ds_salary_proj
## Resources 
Glassdoor scrapper: https://github.com/arapfaik/scraping-glassdoor-selenium
