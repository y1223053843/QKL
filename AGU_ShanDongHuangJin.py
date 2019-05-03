#encoding=utf-8
import pandas as pd
import time
import numpy as num
import tushare as ts
import talib as ta
from email_util import *

data_history = ts.get_k_data("600547", ktype = '60')

# 02、 数据格式处理、并计算布林线值
closeArray = num.array(data_history['close'])
highArray = num.array(data_history['high'])
lowArray = num.array(data_history['low'])

doubleCloseArray = num.asarray(closeArray,dtype='double')
doubleHighArray = num.asarray(highArray,dtype='double')
doubleLowArray = num.asarray(lowArray,dtype='double')

upperband, middleband, lowerband = ta.BBANDS(doubleCloseArray, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("LOWER===============" + str(lowArray[-1]))
print("HIGHER==============" + str(highArray[-1]))
print("CLOSE===============" + str(closeArray[-1]))
print("BULL upperband======" +  str(upperband[-1]))
print("BULL middleband=====" +  str(middleband[-1]))
print("BULL lowerband======" +  str(lowerband[-1]))

#sendMail("【山东黄金】触发60分钟布林线下沿,当前价格：" + str(closeArray[-1]), "【山东黄金】触发60分钟布林线下沿,当前价格：" + str(closeArray[-1]))
if ((lowArray[-1] - lowerband[-1])/lowArray[-1] <= 0.01 ):
     sendMail("【山东黄金】触发60分钟布林线下沿,当前价格：" + str(closeArray[-1]), "【山东黄金】触发60分钟布林线下沿,当前价格：" + str(closeArray[-1]))
if (highArray[-1] >= upperband[-1]):
     sendMail("【山东黄金】触发60分钟布林线上沿,当前价格：" + str(closeArray[-1]), "【山东黄金】触发60分钟布林线下沿,当前价格：" + str(closeArray[-1]))



