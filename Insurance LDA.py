#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# loading the data
dataset=pd.read_csv('C:/Users/Stephen/Downloads/insurance.csv')
dataset.head()


# In[7]:


dataset.tail()


# In[ ]:


# checking if dataset has been duplicated


# In[12]:


dataset.duplicated()


# In[ ]:


# checking number of rows and columns


# In[11]:


dataset.shape


# In[13]:


dataset.describe()


# In[14]:


dataset.nunique


# In[17]:


# cleaning the data


# In[25]:


dataset.isnull().sum()


# In[ ]:





# In[31]:


insurance.head()


# In[3]:


sns.pairplot (raw_data)


# In[80]:


dataset.corr()


# In[81]:


sns.heatmap(dataset.corr())


# In[67]:


sns.pairplot(dataset.corr())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




