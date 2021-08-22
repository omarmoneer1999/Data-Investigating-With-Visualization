#importing the used libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Loading the dataset and understand it
df = pd.read_csv('movies.csv')
df.head()
df.info()
df.overview
df.desccribe()
df.shape

##Data Cleaning

#Dropping the unneeded columns
df.drop(['id','imdb_id','original_title','cast','homepage','overview'],axis=1,inplace=True)
df.drop(['tagline'],axis=1,inplace=True)

#Removing the zeroth values in budget
z= df[df['budget']==0].index
df.drop(z,inplace=True)

df[df['budget']==0]

#Removing the zeroth values in revenue
v = df[df['revenue']==0].index
df.drop(v,inplace=True)

df[df['revenue']==0]

#Removing the rows with nan values
df.dropna(inplace=True)
df.info()


#Finding relationships 
df['director'].value_counts().idxmax()
df.nlargest(10, ['vote_average'])
df['genres'].value_counts().idxmax()

#Premiere Visualizations
df.hist(figsize=(10,8))

#Exploratory Data Analysis with Visualizations
x= df['release_year']
y=df['revenue']
plt.scatter(x, y)
plt.xlabel('Release_Year')
plt.ylabel('Revenue')
plt.title('The relation between the revenue and the time')


x= df['release_year']
y=df['budget']
plt.scatter(x, y, color='green')
plt.xlabel('Release_Year')
plt.ylabel('Budget')
plt.title('the relation between the budget and the time')


