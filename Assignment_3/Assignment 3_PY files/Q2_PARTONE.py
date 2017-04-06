
# coding: utf-8

# # Finding out the highest paid departments in each organization group by calculating mean of total compensation for every department

# In[1]:

#Importing all required packages
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None #'warn'


# In[2]:

#Reading the 'Employee Compensation' data
ec = pd.read_csv("employee_compensation.csv")

#Viewing the dataframe using head function
#print(ec.head())


# In[3]:

#Calculating the mean of the Total Compensation based on department in each organization using group by
ec_frame = ec.groupby([ec['Organization Group'], ec['Department']])['Total Compensation'].mean()

#Viewing the dataframe using head function
#print(ec_frame.head())


# In[5]:

#Converting the series dataset into dataframe
ec_dataframe = pd.DataFrame(ec_frame)

#Resetting the index for alignment of columns
ec_indexed = ec_dataframe.reset_index()

#Viewing the dataframe using head function
print(ec_indexed.head())


# In[6]:

#Sorting the result in descending order so as to show the highest total compensation based on each organization
ec_final_data = ec_indexed.sort_values(['Organization Group','Total Compensation'], ascending = [True,False])
print(ec_final_data.head())


# In[7]:

#Writing the output into a csv
ec_final_data.to_csv('Q2_Part_One.csv', sep = '\t')

