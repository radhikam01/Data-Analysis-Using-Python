
# coding: utf-8

# # Calculate the average score for each team which host the game and win the game

# In[1]:

#Importing all required packages
import pandas as pd
import numpy as np
from pandas import DataFrame
pd.options.mode.chained_assignment = None #'warn'


# In[2]:

#Reading the 'Cricket Matches' file
cricket_matches = pd.read_csv("cricket_matches.csv")


# In[3]:

#Removing all the other columns which are not related to host, winning and innings columns and our analysis
cm_new = cricket_matches.drop(cricket_matches.columns[[0,1,2,3,4,5,7,9,10,11,14,15,16,19,20,21,22,23]], axis = 1)

#Creating a new dataframe for the average scores
cm_dataframe =  DataFrame(columns = ['Average Score'])


# In[7]:

#Comparing the home and winner column to find out if the host team is the winner team
cm_new = cm_new[cm_new['home'] == cm_new['winner']]

#Checking the new dataframe using head function
print(cm_new.head())


# In[8]:

#Checking if the host team played in innings1, if it did then put innings1_runs into score column, if not then innings2_runs should go into score column
cm_new['Score'] = cm_new['innings1_runs'].where(cm_new['home'] == cm_new['innings1'], cm_new['innings2_runs'])

#Checking the new dataframe using head function
print(cm_new.head())


# In[9]:

#Calculating the mean of the score column based on the host team using groupby
cm_dataframe['Average Score'] = cm_new.groupby('home')['Score'].mean()

#Sorting the result in descending order so as to show the highest score value at the top
cm_dataframe_final = cm_dataframe.sort_values(['Average Score'], ascending = False)

#Resetting the index for alignment of columns
cm_final_dataframe = cm_dataframe_final.reset_index()

#Showing the top five scores using head function
print(cm_final_dataframe.head())


# In[21]:

#Writing the output into a csv
cm_final_dataframe.to_csv('Q3_Part_One.csv', sep = '\t')

