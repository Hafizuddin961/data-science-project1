# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:55:34 2020

@author: hafizuddin
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing
#company text only
#state field
#age of company
#parsing of job description (python,etc.)

#salary parsing
df["hourly"] = df['Salary Estimate'].apply(lambda x: 1 
                                              if 'per hour' in x.lower() else 0)
df["provided"] = df['Salary Estimate'].apply(lambda x: 1 
                                              if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').
                        replace('employer provided salary', ''))


df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0].replace(':', '')))
df['max_salary']= min_hr.apply(lambda x: int(x.split('-')[-1]))

df['average'] = (df['min_salary'] + df['max_salary']) // 2

#company text only
df['Company_text'] = df.apply(lambda x: x['Company Name'] 
                                if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#job state
df['job_state'] = df['Location'].apply(lambda x: x.split(', ')[-1])

df['HQ'] = df['Headquarters'].apply(lambda x: x.split(', ')[-1])
df['same_location'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#age of company
df['age'] = df.apply(lambda x: 2020 - x['Founded'] 
                        if x['Founded'] != -1
                        else -1, axis = 1)

#parsing of job description (python,etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0) 
print('Python')
print(df.python_yn.value_counts())

#R
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'R' in x else 0) 

print('R')
print(df.R_yn.value_counts())

#spark
df['Spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0) 
print('Spark')
print(df.Spark_yn.value_counts())

#aws
df['AWS_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0) 
print('AWS')
print(df.AWS_yn.value_counts())

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0) 
print('excel')
print(df.excel_yn.value_counts())

df.columns

df_out = df.drop(df.columns[0], axis=1)

df_out.to_csv('salary_cleaned.csv', index=False)










