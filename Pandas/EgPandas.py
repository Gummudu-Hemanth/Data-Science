'SERIES'
# Importing Pandas
import pandas as pd
import numpy as np

# # Creating a one dimensional array
# arr = [1,2,3,'Hemanth']

# # Creating series
# series = pd.Series(data=arr)

# # Displaying the series
# print(series)

# CREATING A SERIES FROM NUMPY ARRAY

# data = np.array([1,2,3,4,5])
# serie = pd.Series(data)
# print(serie)

# CREATING A SERIES FROM A DICTIONARY

# dict = {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5}
# series = pd.Series(dict)
# print(series)

# CREATING A SERIES FROM A LIST OF LISTS

# list = [['Hemanth' , 'Arreyan' , 'Surya' , 'Muskan' , 'Subah'],
# 		[7.1 , 8.2 , 6.8 , 9.2 , 7.5]]

# series = pd.Series(list)
# print(series) 

'DATAFRAMES'

# CREATING A DATAFRAME FROM A LIST

# list = ['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah']
# df = pd.DataFrame(list)
# print(df)

# CREATING DATAFRAMES FROM ndarrays/dictionary

# data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
# 		'Age' : [19 , 19 , 18 , 20 , 18],
# 		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh']}

# df = pd.DataFrame(data)
# print(df)

# DEALINGS WITH ROWS AND COLUMNS

# Column Selection
# -- We can access the columns by calling their columns name.

# data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
# 		'Age' : [19 , 19 , 18 , 20 , 18],
# 		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
# 		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

# df = pd.DataFrame(data) # Converting dict to df

# cols = df[['Name' , 'Work']]
# print(cols)

# Rows Selection

# data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
# 		'Age' : [19 , 19 , 18 , 20 , 18],
# 		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
# 		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

# df = pd.DataFrame(data) # Converting the dict to dataframe

# first = df[df['Name'] == 'Hemanth']
# second = df[df['Name'] == 'Surya']

# print(first ,"\n\n\n" ,second)

# Indexing Dataframe

# data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
# 		'Age' : [19 , 19 , 18 , 20 , 18],
# 		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
# 		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

# df = pd.DataFrame(data)
# print(df.iloc[3])

# Working with missing data

# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
 
# df = pd.DataFrame(dict) # converting dict to dataframe
# print(df.isnull()) # To check we have have any nan values present in our dataframe.

