#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd 
import matplotlib.pyplot as plt 
from pprint import pprint # pretty print
from tqdm import tqdm # google this
from wordcloud import WordCloud
import itertools
from collections import Counter
import collections
import csv
import numpy as np
from scipy import stats


# In[4]:


listings_df = pd.read_csv('listings (1).csv')
listings_df


# In[5]:


names = listings_df['name']
description = listings_df['description']
nbhood_oview = listings_df['neighborhood_overview']
instant_book = listings_df['instant_bookable']
lstgs_per_host = listings_df['host_total_listings_count']
host_name = listings_df['host_name']
resp_time = listings_df['host_response_time']
accep_rate = listings_df['host_acceptance_rate']
resp_rate = listings_df['host_response_rate']
superhost = listings_df['host_is_superhost']
pro_pic = listings_df['host_has_profile_pic']
nbhood = listings_df['neighbourhood_group_cleansed']
prop_type = listings_df['property_type']
room_type = listings_df['room_type']
num_accom = listings_df['accommodates']
baths = listings_df['bathrooms_text']
bedrooms = listings_df['bedrooms']
beds = listings_df['beds']
amenities = listings_df['amenities']
price = listings_df['price']
min_nights = listings_df['minimum_nights']
num_reviews = listings_df['number_of_reviews']
rev_scores = listings_df['review_scores_rating']
rev_clean = listings_df['review_scores_cleanliness'] 
#rev_per_month = pd.concat(listings_df['reviews_per_month'], listings_df['id'], axis = 0)


# In[6]:


rev_clean.dropna(inplace = True)
rev_clean


# In[7]:


price = price.replace('[\$,]', '', regex=True).astype(float)
entire_homes = room_type[room_type == 'Entire home/apt']
entire_home_clean_rev = rev_clean.loc[listings_df['room_type'] == 'Entire home/apt']
entire_home_price = price.loc[listings_df['room_type'] == 'Entire home/apt']
entire_home_clean_rev.mean()
entire_homes.count()
entire_home_clean_rev.count()
entire_homes.count()


# In[8]:


private_rooms = room_type[room_type == 'Private room']
private_room_clean_rev = rev_clean.loc[listings_df['room_type'] == 'Private room']
private_room_price = price.loc[listings_df['room_type'] == 'Private room']
private_room_clean_rev.mean()  
private_rooms.count()
private_rooms.count() 


# In[11]:


homes = entire_homes.count()
clean_a = entire_home_clean_rev.sum()
failures_a = entire_homes.count() - entire_home_clean_rev.count()

rooms = private_rooms.count()
clean_b = private_room_clean_rev.sum() 
failures_b = private_rooms.count() - private_room_clean_rev.count() 

beta_a = stats.beta(1+clean_a, 1+failures_a)
beta_b = stats.beta(1+clean_b, 1+failures_b)

samp_a = beta_a.rvs(size=100000)
samp_b = beta_b.rvs(size=100000)

(samp_b > samp_a).mean()


# In[ ]:




