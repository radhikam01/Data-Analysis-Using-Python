
# coding: utf-8

# # Percentage of collisions in Manhattan out of 2016's total accidents in New York City

# In[16]:

#Importing all required packages
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import datetime
import calendar
pd.options.mode.chained_assignment = None #'warn'


# In[17]:

#Reading the 'Vehicle Collisions' data
vc = pd.read_csv("vehicle_collisions.csv")
vc_frame = DataFrame(vc)


# In[18]:

#Extracting the date from the DATE column in vc_frame
vc_frame['DATE'] = pd.to_datetime(vc['DATE'])

#Taking out only the dates which are of the year 2016
vc_dataframe_new = vc_frame[(vc_frame['DATE'] > '2015-12-31') & (vc_frame['DATE'] < '2017-01-01')]


# In[19]:

#Extracting the month from the DATE column using dt.month function
vc_dataframe_new['MONTH'] = vc_frame['DATE'].dt.month


# In[20]:

#Creating a new dataframe with the columns 'Manhattan', 'NYC' and 'Percentage'
vc_dataframe_final = DataFrame(columns = ['Manhattan','NYC','Percentage'])
print(vc_dataframe_final)


# In[21]:

#Extracting the count of Manhattan collisions grouping by the month column
vc_dataframe_final['Manhattan'] = vc_dataframe_new[vc_dataframe_new['BOROUGH']=='MANHATTAN'].groupby(['MONTH'],sort = False)['UNIQUE KEY'].count()

#Extracting the count in the whole of New York City collisions grouping by the month column
vc_dataframe_final['NYC'] = vc_dataframe_new.groupby(['MONTH'])['UNIQUE KEY'].count()

#Taking out the percentage of collisions in Manhattan out of total New York City
vc_dataframe_final['Percentage'] = (vc_dataframe_final['Manhattan']/vc_dataframe_final['NYC'])

#Resetting the index of the new dataframe for alignment
vc_indexed = vc_dataframe_final.reset_index()
print(vc_indexed)


# In[22]:

#Changing the month number into the name of the month by using calender.month_abbr and lambda function
vc_indexed['MONTH'] = vc_indexed['MONTH'].apply(lambda x: calendar.month_abbr[x])


# In[23]:

#Final output - showing the 1st five rows using the head function
print(vc_indexed.head())


# In[24]:

#Writing the output into a csv
vc_indexed.to_csv('Q1_Part_One.csv', sep = '\t')

