
# coding: utf-8

# # For each borough, finding out distribution of each collision

# In[1]:

#Importing all required packages
from pandas import Series, DataFrame 
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None #'warn'


# In[2]:

#Reading the 'Vehicle Collisions' data
vc = pd.read_csv('vehicle_collisions.csv')
vc_frame = DataFrame(vc)


# In[4]:

#Taking out the count of all the vehicle1,2,3,4 type columns based on borough by using group by function
vc_frame_new = vc_frame.groupby(['BOROUGH'],sort = False)['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE'].count().reset_index()

#Creating an empty dataframe
vc_dataframe = DataFrame() 

#Copying the borough column to new dataframe
vc_dataframe['BOROUGH'] = vc_frame_new['BOROUGH']  

#Calculating count of one vehicle involved
vc_dataframe['One_Vehicle_Involved'] = vc_frame_new['VEHICLE 1 TYPE'] - vc_frame_new['VEHICLE 2 TYPE'] 

#Calculating count of two vehicles involved
vc_dataframe['Two_Vehicles_Involved'] = vc_frame_new['VEHICLE 2 TYPE'] - vc_frame_new['VEHICLE 3 TYPE'] 

#Calculating count of three vehicles involved
vc_dataframe['Three_Vehicles_Involved'] = vc_frame_new['VEHICLE 3 TYPE'] - vc_frame_new['VEHICLE 4 TYPE'] 

#Calculating count of more than three Vehicles involved
vc_dataframe['More_Vehicle_Involved'] = vc_frame_new['VEHICLE 4 TYPE'] 

vc_dataframe.set_index('BOROUGH', inplace = True)

#print(vc_dataframe.head())


# In[5]:

#Resetting the index for alignment of columns
vc_final_frame = vc_dataframe.reset_index()
print(vc_final_frame)


# In[ ]:

#Writing the output into a csv
vc_final_frame.to_csv('Q1_Part_Two.csv', sep = '\t')

