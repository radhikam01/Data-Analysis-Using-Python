
# coding: utf-8

# # Average salary, benefits, compensation etc of each employee for the calendar year

# In[2]:

#Importing all required packages
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None #'warn'


# In[3]:

#Reading the 'Employee Compensation' data
frame = pd.read_csv("employee_compensation.csv")

#Checking the dataframe using head function
#print(frame.head())


# In[4]:

#Filtering data by calendar year
calendar = frame[frame['Year Type'] == 'Calendar']


# In[9]:

#Finding out the average salary of all the salary related columns by grouping by on Employee Identifier column
calendar_avg = calendar.groupby('Employee Identifier', sort = True).mean()

#Removing all the other columns which are not related to salary and our analysis
salary_avg = calendar.drop(calendar.columns[[0,1,2,3,4,5,6,7,8,10,11]], axis = 1)

#Checking the dataframe using head function
print(salary_avg.head())


# # Finding out the employees whose overtime salary is greater than 5% of salary column

# In[8]:

#Checking if the employee has overtime salary greater than 5% of salaries
salary_avg = salary_avg[salary_avg['Overtime'] > 0.05 * salary_avg['Salaries']]

#Checking the dataframe using head function
print(salary_avg.head())


# # Calculating the percentage of total benefits with respect to total compensation for each job family

# In[10]:

#Calcuating the mean of Total benefits and Total Compensation for each job family by grouping by on Job family
salary_family = salary_avg.groupby('Job Family')['Total Benefits','Total Compensation'].mean()

#Resetting the index of new dataframe and showing using head function
#print(salary_family.reset_index().head())


# In[11]:

#Creating a new percentage column and calcuating the percentage of total benefits wrt total compensation for each job family
salary_family['Percent_Total_Benefit'] = salary_family['Total Benefits']/salary_family['Total Compensation'] * 100

#Sorting the result in descending order so as to show the highest percent value at the top
final_benefits = salary_family.sort_values(['Percent_Total_Benefit'], ascending = False)

#Resetting the index for alignment of columns
final_dataframe = final_benefits.reset_index()

#Showing the top five job families using head function
print(final_dataframe.head())


# In[26]:

#Writing the output into a csv
final_dataframe.to_csv('Q2_Part_Two.csv', sep = '\t')

