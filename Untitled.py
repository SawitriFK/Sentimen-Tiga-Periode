#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Library

import pandas as pd

import json, requests,tweepy
from requests_oauthlib import OAuth1


# ## Sumber Data

# ### Twitter

# In[ ]:


with open("token.json") as f:
  tokens = json.load(f)

bearer_token = tokens['bearer_token']
api_key = tokens['api_key']
api_key_secret = tokens['api_key_secret']
access_token = tokens['access_token']
access_token_secret = tokens['access_token_secret']

tokens.keys()


# In[ ]:


#buat variabel authentikasi dan api
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api_1 = tweepy.API(auth, wait_on_rate_limit=True)


# In[ ]:


def search_tweets(query):
    response = tweepy.Cursor(api_1.search_tweets,
                             q = query,
                             lang = 'id',
                             tweet_mode = 'extended'
                            ).items()
    for tweet in response:
        print(tweet.full_text)
        print("----------------------------------------")


# In[ ]:


search_tweets('3 periode')


# ## Business Understanding

# ## Data Collection

# ## Data Preparation

# ## Data Processing

# ## Share Insight
