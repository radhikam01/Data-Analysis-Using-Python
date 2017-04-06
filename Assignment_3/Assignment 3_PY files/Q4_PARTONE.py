
# coding: utf-8

# # Extract data from the Awards column and split it into its specific columns

# In[1]:

#Importing all required packages
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar
pd.options.mode.chained_assignment = None #'warn'


# In[2]:

#Reading the 'Movies Awards' data
movies_awards = pd.read_csv('movies_awards.csv')


# In[3]:

#Extracting the wins and nominations according to the awards in their respective columns

#Extracting won awards from Awards column and putting it into 'Awards_Won' column
movies_awards['Awards_Won'] = movies_awards['Awards'].str.extract('(\d+) win', expand=True)

#Extracting nominated awards from the Awards column and putting it into 'Awards_Nominated' column
movies_awards['Awards_Nominated'] = movies_awards['Awards'].str.extract('(\d+) nomination', expand=True)

#Extracting won Primetime awards from Awards column and putting it into 'PrimeAwards_Won' column
movies_awards['PrimeAwards_Won']= movies_awards['Awards'].str.extract('Won (\d+) Primetime', expand=True)

#Extracting nominated Primetime awards from Awards column and putting it into 'PrimeAwards_Nominated' column
movies_awards['PrimeAwards_Nominations']= movies_awards['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)

#Extracting won BAFTA awards from Awards column and putting it into 'BaftaAwards_Won' column
movies_awards['BaftaAwards_Won']= movies_awards['Awards'].str.extract('Won (\d+) BAFTA', expand=True)

#Extracting nominated BAFTA awards from Awards column and putting it into 'BaftaAwards_Nominations' column
movies_awards['BaftaAwards_Nominations']= movies_awards['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)

#Extracting won Oscar awards from Awards column and putting it into 'BaftaAwards_Won' column
movies_awards['OscarAwards_Won']= movies_awards['Awards'].str.extract('Won (\d+) Oscar', expand=True)

#Extracting nominated Oscar awards from Awards column and putting it into 'BaftaAwards_Nominations' column
movies_awards['OscarAwards_Nominations']= movies_awards['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)

#Extracting won GoldenGlobe awards from Awards column and putting it into 'GoldenGlobeAwards_Won' column
movies_awards['GoldenGlobeAwards_Won']= movies_awards['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)

#Extracting nominated GoldenGlobe awards from Awards column and putting it into 'GoldenGlobeAwards_Nominations' column
movies_awards['GoldenGlobeAwards_Nominations']= movies_awards['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)


# In[4]:

#Selecting only those columns which are needed for the result and analysis and creating a new dataframe with the same
movies_awards_new = movies_awards[[15,21,22,23,24,25,26,27,28,29,30]]


# In[6]:

#Filling the non numeric/NA values with 0
movies_awards_result = movies_awards_new.fillna(0)

#Viewing the result using head function
#print(movies_awards_result.head())


# In[7]:

#Converting all the pandas objects into int
movies_awards_result['Awards_Won'] = movies_awards_result['Awards_Won'].astype(str).astype(int)
movies_awards_result['PrimeAwards_Won'] = movies_awards_result['PrimeAwards_Won'].astype(str).astype(int)
movies_awards_result['BaftaAwards_Won'] = movies_awards_result['BaftaAwards_Won'].astype(str).astype(int) 
movies_awards_result['OscarAwards_Won'] = movies_awards_result['OscarAwards_Won'].astype(str).astype(int) 
movies_awards_result['GoldenGlobeAwards_Won'] = movies_awards_result['GoldenGlobeAwards_Won'].astype(str).astype(int)
movies_awards_result['Awards_Nominated'] = movies_awards_result['Awards_Nominated'].astype(str).astype(int) 
movies_awards_result['PrimeAwards_Nominations'] = movies_awards_result['PrimeAwards_Nominations'].astype(str).astype(int)
movies_awards_result['BaftaAwards_Nominations'] = movies_awards_result['BaftaAwards_Nominations'].astype(str).astype(int)
movies_awards_result['OscarAwards_Nominations'] = movies_awards_result['OscarAwards_Nominations'].astype(str).astype(int)  
movies_awards_result['GoldenGlobeAwards_Nominations'] = movies_awards_result['GoldenGlobeAwards_Nominations'].astype(str).astype(int)


# In[8]:

#Calculating and totalling up the awards won by each movie
movies_awards_result['Awards_Won'] = movies_awards_result['Awards_Won']+movies_awards_result['PrimeAwards_Won']+movies_awards_result['BaftaAwards_Won']+movies_awards_result['OscarAwards_Won']+movies_awards_result['GoldenGlobeAwards_Won']


# In[9]:

#Calculating the no of times the movie has been nominated for awards
movies_awards_result['Awards_Nominated'] = movies_awards_result['Awards_Nominated']+movies_awards_result['PrimeAwards_Nominations']+movies_awards_result['BaftaAwards_Nominations']+movies_awards_result['OscarAwards_Nominations']+movies_awards_result['GoldenGlobeAwards_Nominations']


# In[10]:

#Final output - showing the 1st five rows using the head function
print(movies_awards_result.head())


# In[11]:

#Writing the output into a csv
movies_awards_result.to_csv('Q4_PARTONE.csv')

