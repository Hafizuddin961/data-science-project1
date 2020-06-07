# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:19:02 2020

@author: hafizuddin
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

salary_hour = salary.find('Per Hour')