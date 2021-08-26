from datetime import datetime,timedelta,date
from pandas import to_datetime

# 2021/6/7
# rowan.wang
# 取得現在的時間(年_月_日_時_分_秒)(產出文字格式)
def get_time():
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# 2021/6/7
# rowan.wang
# 取得現在的日期(年_月_日)(產出文字格式)
def get_date():
    return datetime.now().strftime("%Y_%m_%d")

# 2021/6/3
# rowan.wang
# 取得n天前的日期(產出日期格式)
def specfic_date(num):
    result = date.today()-timedelta(days=num) 
    # print(result.strftime("%Y_%m_%d"))
    return result

# 2021/6/3
# rowan.wang
# 將文字的日期的欄位YYYY-MM-DD轉成四個欄位，TIME為時間格式的欄位，YEAR MONTH DAY分別取年月日 WEEK則取第幾周
def time_trans(dataframe,column):
    dataframe.loc[:,['TIME']]=to_datetime(dataframe[column], format="%Y-%m-%d")
    dataframe.loc[:,['YEAR']]=dataframe[column].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").strftime("%Y"))
    dataframe.loc[:,['MONTH']]=dataframe[column].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").strftime("%m"))
    dataframe.loc[:,['DAY']]=dataframe[column].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").strftime("%d"))
    dataframe.loc[:,['WEEK']]=dataframe[column].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").strftime("%W"))
    # 當該周為當年第一周 周數是00，將00改為上年最後一周
    # 取得去年最後一日的最後一周
    today = date.today()
    last_year_last_day = today.replace(month=1,day=1)-timedelta(days=1)
    last_week = last_year_last_day.strftime("%W")
    # 將今年第一周取代成去年最後一周周數
    dataframe['WEEK'].replace('00', last_week, inplace=True)
    return dataframe