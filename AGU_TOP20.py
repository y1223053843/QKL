#encoding=utf-8

import sys
import tushare as ts
import time
import numpy as num
from datetime import datetime, date
from datetime import timedelta

'''
#################################
执行函数 execute
说明：
#################################
'''
def execute_shenzhen_1(days):
    ts.set_token('a0a3a3ee133d6623bf9072236a5a8423c1c021d00aba3eb0c7bdfa5e')
    pro = ts.pro_api()

    jsonDic = {}
    for i in range(days) :
        date_n = (date.today() - timedelta(days=i)).strftime("%Y%m%d")
        df = pro.hsgt_top10(trade_date=date_n, market_type='3')
        ts_code = num.array(df['ts_code'])
        name = num.array(df['name'])
        net_amount = num.array(df['net_amount'])
        net_amount = net_amount.astype(num.float)
        if (len(ts_code) > 0):
            for i in range(ts_code.size):
                if (jsonDic.get(name[i]) == None):
                    jsonDic[name[i]] = 0
                jsonDic[name[i]] = jsonDic.get(name[i]) + net_amount[i]

    jsonDic1 = sorted(jsonDic.items(),key=lambda x:x[1])
    print(jsonDic1)

print("===========================05天：")
execute_shenzhen_1(5)
print("===========================10天：")
execute_shenzhen_1(10)
print("===========================30天：")
execute_shenzhen_1(30)
print("===========================60天：")
time.sleep(60)
execute_shenzhen_1(60)
