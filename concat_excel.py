#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
def concat_excelF(path):
    VLRROBA_list=pd.DataFrame(columns=['A'])
    for i in os.listdir(r"{}".format(path)):#組合所有excel
        df=pd.read_excel(r"{}\{}".format(path,i))
        VLRROBA_list=pd.concat([df,VLRROBA_list],axis=0)
    VLRROBA_list=VLRROBA_list.drop(['A'], axis=1)
    return VLRROBA_list

