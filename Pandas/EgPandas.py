'SERIES'
# Importing Pandas
import pandas as pd
import numpy as np

# Creating a one dimensional array
arr = [1,2,3,'Hemanth']

# Creating series
series = pd.Series(data=arr)

# Displaying the series
print(series)

# CREATING A SERIES FROM NUMPY ARRAY

data = np.array([1,2,3,4,5])
serie = pd.Series(data)
print(serie)

# CREATING A SERIES FROM A DICTIONARY

dict = {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5}
series = pd.Series(dict)
print(series)

# CREATING A SERIES FROM A LIST OF LISTS

list = [['Hemanth' , 'Arreyan' , 'Surya' , 'Muskan' , 'Subah'],
		[7.1 , 8.2 , 6.8 , 9.2 , 7.5]]

series = pd.Series(list)
print(series) 

'DATAFRAMES'

# CREATING A DATAFRAME FROM A LIST

list = ['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah']
df = pd.DataFrame(list)
print(df)

# CREATING DATAFRAMES FROM ndarrays/dictionary

data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
		'Age' : [19 , 19 , 18 , 20 , 18],
		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh']}

df = pd.DataFrame(data)
print(df)

# DEALINGS WITH ROWS AND COLUMNS

# Column Selection
# -- We can access the columns by calling their columns name.

data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
		'Age' : [19 , 19 , 18 , 20 , 18],
		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

df = pd.DataFrame(data) # Converting dict to df

cols = df[['Name' , 'Work']]
print(cols)

# Rows Selection

data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
		'Age' : [19 , 19 , 18 , 20 , 18],
		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

df = pd.DataFrame(data) # Converting the dict to dataframe

first = df[df['Name'] == 'Hemanth']
second = df[df['Name'] == 'Surya']

print(first ,"\n\n\n" ,second)

# Indexing Dataframe

data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
		'Age' : [19 , 19 , 18 , 20 , 18],
		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

df = pd.DataFrame(data)
print(df.iloc[3]) # Gives us all the details at index 3 (Name , Age , Place , Work).

# Working with missing data

dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
df = pd.DataFrame(dict) # converting dict to dataframe
print(df.isnull()) # To check we have have any nan values present in our dataframe.


'DATA MANIPULATION'

data = {'Name':['Hemanth' , 'Arryean' , 'Surya' , 'Muskan' , 'Subah'],
		'Age' : [19 , 19 , 18 , 20 , 18],
		'Place': ['Kerela' , 'Dehli' , 'Hyderabad' , 'Amritsar' , 'Himachal Pradesh'],
		'Work':['Data Scintist' , 'AI ML Developer' , 'Canva Designer' , 'ML Specialist' , 'UX Designer']}

df = pd.DataFrame(data=data)
print(df)

# Shape
print(df.shape) # (5,4) returns no of rows and columns

# Info()
print(df.info())

# Describe()
print(df.describe()) # describes only numerical data
print(df.describe(include='all')) # describes numerical and categorical data.

'GROUPING AND AGGREGATION'

df = pd.DataFrame([[10,27,30,22,26],
				   [16,19,10,23,28],
				   [28,23,30,30,11],
				   [11,7,24,30,30]],
				   columns=['Maths' , 'Hindi' , 'SST' , 'PE' , 'English'])

# AGGREGATION

# 1. Sum()
print(df.sum()) # returns the sum of each column.

# 2. Min()
print(df.min()) # return the min of the column values.

# 3. Max()
print(df.max()) # return the max of the column values.

# 4. Mean()
print(df.mean()) # compute the mean of column value.

# USing agg() method

print(df.agg(['min' , 'max' , 'mean' , 'std']))

# GROUP_BY
group_pe=df.groupby(by=['Maths'])
print(group_pe)

# to view the result of formed groups we will use first() method.
print(group_pe.first())

'COMBINING THE DATA IN PANDAS USING MERGE() , JOIN() , CONCAT()'

# Concat
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("This is dataframe1:  " , "\n" , df1 , "\n")
print("This is dataframe2:  " , "\n" , df2 , "\n")

concat = pd.concat([df1,df2])
print("This is concated frame: " , "\n" , concat)

# JOIN
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kerala'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Shimla', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 1. Inner join
ineer_join = pd.merge(df1 , df2 , on='Address' , suffixes=("_df1" , "_df2"))
print(ineer_join) # returns only the matching rows.

# 2. Left Join
left_join = pd.merge(df1,df1 , on="Address" , how='left' , suffixes=("_df1" , "_df2"))
print(left_join)

# 3. Right Join
right_join = pd.merge(df1 , df2 , on='Address' , how='right' , suffixes=('_df1' , '_df2'))
print(right_join)

# 4. OUTER JOIN
outer_join = pd.merge(df1 , df2 , on='Address' , how='outer' , suffixes=('_df1' , '_df2'))
print(outer_join)

'METHODS TO HANDLE MISSING DATA'

# isnull() and notnull()
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 

df = pd.DataFrame(dict)

print(df.isnull()) # Rteurn True for NaN values
print(df.notnull()) # Return False for NaN values.

# Fillna()
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 

df = pd.DataFrame(dict)
print(df.fillna(0))

print(df.fillna(method = 'pad')) # fill the NaN using privious value.

print(df.bfill()) # fill the NaN using next value.

# Replace
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 

df = pd.DataFrame(dict)

rep = df.replace(to_replace=np.nan , value=0) # replacing the NaN values with 0.
print(rep)

# Interpolate using Linear method
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 

df = pd.DataFrame(dict)

inter = df.interpolate(method='linear' , limit_direction='both')
print(inter)