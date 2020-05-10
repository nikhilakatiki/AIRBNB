#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#create dataframe from csv 
airbnb_listings_dataframe = pd.read_csv('listings.csv')


df = airbnb_listings_dataframe

# del df['host_id','host_name','neighbourhood','latitude','longitude','cancellation_policy']
df.drop(['host_id','host_name','neighbourhood','latitude','longitude','cancellation_policy'], axis=1, inplace=True)

df


# In[54]:


plt.figure(figsize= (10,10), dpi=100)
sns.heatmap(df.corr())


# In[107]:


df1 = df[['city','price']]
df1.loc[:,'city']= df1['city'].str.strip()
df1.loc[:,'city']= df1['city'].str.lower()
df1.loc[:,'price'] = df['price'].groupby(df['city']).transform('mean')
df2=df1.drop_duplicates(keep='first')
df3=df2.loc[df['city'].isin(['astoria','new york','brooklyn','bronx','queens','long island city'])]
df3


# In[109]:


sns.set(style="whitegrid")
ax = sns.barplot(x="city", y="price", data=df3)


# In[ ]:




