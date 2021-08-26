#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from urllib import request
import pandas as pd
import numpy as np
def requestJson(url):
    json_data = request.urlopen(url).read().decode("utf-8")
    json_data = json.loads(json_data)
    df=pd.DataFrame.from_dict(json_data[0], orient='index').T
    for i in range(len(json_data)-1):
        nextdf=pd.DataFrame.from_dict(json_data[i+1], orient='index').T
        df=pd.concat([nextdf,df],axis=0)
    return df

