#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


data = pd.read_csv("C:\\Users\\91630\\Downloads\\EDA_dataset (1).csv")


# In[6]:


missing_percentage = data.isnull().mean().mean() *100


# In[7]:


column_with_most_missing = data.isnull().sum().idxmax()


# In[12]:


print(f"percentage of missing values: {missing_percentage: .2f}%")
print(f"column with the highest number of missing value: {column_with_most_missing}")


# In[9]:


unique_value_counts = data.nunique()


# In[10]:


column_with_one_value = unique_value_counts[unique_value_counts <=1]


# In[11]:


num_columns_with_one_value = len(columns_with_one_value)


# In[13]:


data = pd.read_csv("C:\\Users\\91630\\Downloads\\EDA_dataset (1).csv")


# In[14]:


unique_value_counts = data.nunique()


# In[35]:


column_with_one_value = unique_value_counts[unique_value_counts <= 1]


# In[36]:


num_column_with_one_value = len(column_with_one_value)


# In[37]:


print(f"Number of column with not more than just one value: {num_column_with_one_value}")
print("Column with not more than just one value")
print(column_with_one_value)


# In[46]:


numeric_columns = data.select_dtypes(include = ['float64','int64'])
filtered_columns = numeric_columns.columns[numeric_columns.nunique() >= 5]


# In[40]:


import numpy as np


# In[41]:


import pandas as pd


# In[42]:


data = pd.read_csv("C:\\Users\\91630\\Downloads\\EDA_dataset (1).csv")


# In[45]:


numeric_columns = data.select_dtypes(include = ['float64','int64'])
filtered_columns = numeric_columns.columns[numeric_columns.nunique() >= 5]


# In[47]:


statistical_properties = data[filtered_columns].describe()


# In[48]:


print("Statistical properties of columns with numerical values and at least 5 unique column values:")
print(statistical_properties)


# In[49]:


import matplotlib.pyplot as plt


# In[50]:


selected_columns = ['MntWines','MntFruits','MntMeatProducts']


# In[51]:


for column in selected_columns:
    data[column].plot(kind = 'hist', bins = 10)
    plt.title(f'Histogram plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# In[52]:


import seaborn as sns
import pandas as ps


# In[53]:


data


# In[54]:


sns.pairplot(data)


# In[55]:


x = data["Recency"]
y = data["MntWines"]
z = data["Z_CostContact"]


# In[56]:


plt.scatter(x,y,z)


# In[57]:


data.tail()


# In[58]:


newdata = data[['Recency','MntWines','Z_CostContact']].dropna()
newdata.tail()


# In[59]:


newdata.corr()


# In[60]:


plt.scatter(x,y,z)


# In[61]:


x = data["Income"]
y = data["Year_Birth"]
z = data["Z_Revenue"]


# In[62]:


plt.scatter(x,y,z)


# In[63]:


newdata = data[['Year_Birth','Income','Z_Revenue']].dropna()


# In[64]:


newdata.head()


# In[65]:


newdata.corr()


# In[66]:


data.head()


# In[67]:


newdata.head()


# In[ ]:




