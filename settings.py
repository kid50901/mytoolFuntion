import configparser
import logging

# config必須使用絕對路徑
def load_config(inipath):
    config = configparser.ConfigParser()
    config.read(inipath)
    return config


# TODO:log優化目前不能引用
def load_log():
    # log file
    logger = logging.getLogger(__name__)
    # DEBUG程度的寫入log file
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler('{location}/{filename}.log'.format(location=load_config()['location']['output'],filename = 'bu'))
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
