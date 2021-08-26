import os
from pandas import DataFrame,read_excel,concat

# 取得資料夾清單
def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)), reverse=True)
        return dir_list

# 合併資料夾內的所有excel檔
def combine_excel_file(path,destination,filename):
    filelist=get_file_list(path)
    result=DataFrame()
    for i in filelist:
        temp=read_excel('{path}\{filename}'.format(path=path,filename=i))
        result=concat([result,temp], ignore_index=True)

    result.to_excel('{location}\{filename}.xlsx'.format(location=destination,filename=filename), index=False)

# TODO:合併資料夾內的所有csv檔

# TODO:取得資料夾內最新n筆檔案

# TODO:清除資料夾內的所有檔案

# TODO:清除除了最新n筆檔案的所有檔案