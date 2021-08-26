#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
def boomtable(suourstable,wantlist,wantboom,choosesplit):
    initboom=((pd.concat([pd.Series( row[wantlist[0]], row[wantboom].split(choosesplit)) for _, row in suourstable.iterrows()]).reset_index()).rename(columns={"index":wantboom,0:wantlist[0]}))
    for i in range(len(wantlist)-1):
        addboom=((pd.concat([pd.Series( row[wantlist[i+1]], row[wantboom].split(choosesplit)) for _, row in suourstable.iterrows()]).reset_index()).rename(columns={0:wantlist[i+1]}))
        initboom=pd.concat([initboom,addboom[wantlist[i+1]]],axis=1)
    return initboom

