# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 03:45:04 2020

@author: hafizuddin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')  

#choose relavant column
df.columns

df_model = df[['avg_salary','Rating', 'Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly',
               'employer_provided', 'job_state','same_state','age','python_yn','spark','aws',
               'excel','job_simp','seniority','desc_len']]

# get dummy variable
df_dummy = pd.get_dummies(df_model) 

# train test.split
from sklearn.model_selection import train_test_split

x = df_dummy.drop('avg_salary', axis=1)
y = df_dummy.avg_salary.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# multiple linear regression
import statsmodels.api as sm

x_sm = x = sm.add_constant(x)
model = sm.OLS(y,x_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))
#lasso regression
# random forest
# tune model GridsearchCV
#test example


















