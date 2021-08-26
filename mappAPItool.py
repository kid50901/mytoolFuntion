#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time
import base64
import os
import requests
from PIL import Image
from io import BytesIO
import urllib
import datetime as dt

def BinaryfileTObase64URL(Binaryfilepath):
    f=open(Binaryfilepath, 'rb')
    encodestr = base64.b64encode(f.read()) 
    urlbg_file = urllib.parse.quote_plus(encodestr)
    return urlbg_file

def imgurlTObase64URL(imgurl):
    img_re = requests.get(imgurl)
    #image = Image.open(BytesIO(img_re.content)) 
    ls_f=base64.b64encode(BytesIO(img_re.content).read())
    img_base64url = urllib.parse.quote_plus(ls_f)#轉URL
    return img_base64url

def mapppost_content(useraccount,apikey,chatsn,content):
    content_utf8 = content.encode("UTF-8")#轉UTF8
    content_utf8_url = urllib.parse.quote_plus(content_utf8)#轉URL
    url = "http://mapp.local/teamplus_innolux/API/IMService.ashx"
    payload = "ask=sendChatMessage&account={}&api_Key={}&chat_sn={}&content_type=1&msg_content={}&file_show_name=&undefined=".format(useraccount,apikey,chatsn,content_utf8_url)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    
def mapppost_Binaryfile(useraccount,apikey,chatsn,file_base64url,filetype,outputfilename):   
    #上傳檔案
    url = "http://mapp.local/teamplus_innolux/API/IMService.ashx"
    payload = "ask=uploadFile&account={}&api_Key={}&file_type={}&data_binary={}".format(useraccount,apikey,filetype,file_base64url)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    #輸出字串處理
    s=response.text.split(':')
    ss=s[1].split(',')
    x=eval(ss[0])
    
    #mappapi聊天室推送檔案
    url = "http://mapp.local/teamplus_innolux/API/IMService.ashx"
    payload = "ask=sendChatMessage&account={}&api_Key={}&chat_sn={}&content_type=2&msg_content={}&file_show_name={}".format(useraccount,apikey,chatsn,x,outputfilename)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


# In[ ]:




