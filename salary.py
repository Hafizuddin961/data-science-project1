# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:01:06 2020

@author: hafizuddin
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/hafizuddin/Documents/Data-Science-Project1/chromedriver"

df = gs.get_jobs(False, 150, False, path, 15)

df.to_csv(r'C:/Users/hafizuddin/Documents/Data-Science-Project1/salary_150.csv', index = False)