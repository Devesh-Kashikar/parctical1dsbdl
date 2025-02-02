#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


data_set_name=sns.get_dataset_names()


# In[6]:


print(data_set_name)


# In[7]:


dataset=sns.load_dataset("iris")
dataset


# In[8]:


dataset.head(6)


# In[9]:


dataset.head(5)


# In[10]:


dataset.tail(5)


# In[11]:


dataset.index


# In[12]:


dataset.columns


# In[13]:


dataset.shape


# In[14]:


dataset.dtypes


# In[15]:


dataset.columns.values


# In[16]:


dataset.describe(include='all')


# In[17]:


dataset['sepal_width']


# In[18]:


dataset.sort_index(axis=1,ascending=0)


# In[19]:


dataset.sort_values(by="sepal_length")


# In[20]:


dataset.iloc[5]


# In[21]:


dataset[0:3]


# In[22]:


dataset.loc[:,["sepal_length","sepal_width"]]


# In[23]:


dataset.iloc[:4,:]


# In[24]:


dataset.iloc[:,:2]


# In[25]:


dataset.iloc[:5,:2]


# In[26]:


dataset.iloc[3:5,0:3]


# In[27]:


dataset.iloc[[1,2,4],[0,2]]


# In[28]:


dataset.iloc[[1,9,10],[0,3]]


# In[29]:


dataset.iloc[1:3,:]


# In[30]:


dataset.iloc[:,1:3]


# In[31]:


dataset.iloc[2,1]


# In[32]:


dataset["sepal_length"].iloc[5]


# In[33]:


c=dataset.columns[1:3]
dataset[c]


# In[34]:


dataset[dataset.columns[2:4]].iloc[5:10]


# In[ ]:




