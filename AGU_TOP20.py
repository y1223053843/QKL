#encoding=utf-8

import sys
import tushare as ts
import time

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute():
    ts.set_token('a0a3a3ee133d6623bf9072236a5a8423c1c021d00aba3eb0c7bdfa5e')
    pro = ts.pro_api()
    df = pro.hsgt_top10(trade_date='20190508', market_type='3')
    print(df)


execute()