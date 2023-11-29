#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


data=pd.read_csv(r'/Users/user/Documents/FreeCodeCamp/adult.data.csv')


# In[5]:


data.head()


# In[6]:


race_counts = data['race'].value_counts()
race_counts


# In[7]:


# Calculate the average age of men
average_age_men = data[data['sex'] == 'Male']['age'].mean()
average_age_men


# In[8]:


# Calculate the percentage of people who have a Bachelor's degree
bachelors_degree_percentage = (data['education'] == 'Bachelors').mean() * 100
bachelors_degree_percentage


# In[9]:


# Calculate the percentage of people with advanced education (Bachelors, Masters, or Doctorate) making more than 50K
advanced_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
earning_above_50k = data['salary'] == '>50K'


# In[10]:


# Percentage of people with advanced education making more than 50K
percentage_advanced_education_above_50k = ((advanced_education & earning_above_50k).mean()) * 100
percentage_advanced_education_above_50k


# In[11]:


# Calculate the percentage of people without advanced education making more than 50K
percentage_non_advanced_education_above_50k = ((~advanced_education & earning_above_50k).mean()) * 100
percentage_non_advanced_education_above_50k


# In[12]:


# Find the minimum number of hours a person works per week
min_hours_per_week = data['hours-per-week'].min()
min_hours_per_week


# In[13]:


# Calculate the percentage of people who work the minimum number of hours per week and have a salary of more than 50K
min_hours_workers = data['hours-per-week'] == min_hours_per_week
percentage_min_hours_above_50k = (min_hours_workers & earning_above_50k).mean() * 100
percentage_min_hours_above_50k


# In[14]:


# Calculate the percentage of people earning more than 50K by country
country_salary_counts = data.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
country_above_50k_percentage = country_salary_counts['>50K'].sort_values(ascending=False)
highest_earning_country = country_above_50k_percentage.idxmax()
highest_earning_country_percentage = country_above_50k_percentage.max() * 100

highest_earning_country, highest_earning_country_percentage


# In[15]:


# Find the most popular occupation for those who earn more than 50K in India
india_high_earners = data[(data['native-country'] == 'India') & (earning_above_50k)]
top_occupation_in_india = india_high_earners['occupation'].value_counts().idxmax()
top_occupation_in_india


# In[ ]:




