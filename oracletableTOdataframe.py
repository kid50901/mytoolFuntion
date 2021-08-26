#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import cx_Oracle
def totalTable(UserID,PassWord,Host,ServerPort,ServiceName,tablename):
    #con = cx_Oracle.connect('qis_cowk_tst/tqiscowktst@tvCOMB11gDB.cminl.oa:1521/tcomb11g') #建立連線
    con = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(UserID,PassWord,Host,ServerPort,ServiceName)) #建立連線
    cur = con.cursor() #建立游標
    #execute("SELECT P1, P2, P3,P4,P5  FROM dataoba_myreport" )
    #cur.execute("SELECT * FROM QIS_GLOBALUAT_ADMIN.QA_DATAMART_NG_SYMPTOM")
    cur.execute("SELECT * FROM {}".format(tablename))
    columns_name = [des[0] for des in cur.description]###取欄位值
    mytable = cur.fetchall()
    con.close()
    mytabledf =pd.DataFrame(list(mytable))
    for i in range(len(columns_name)):
        mytabledf=mytabledf.rename(columns={i:columns_name[i]})
    return mytabledf

