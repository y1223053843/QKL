#encoding=utf-8
import pandas as pd
import time
import numpy as num
import tushare as ts
import talib as ta
from email_util import *

def strategy(code, name):
     data_history = ts.get_k_data(code, ktype = "15")

     # 02、 数据格式处理、并计算布林线值
     closeArray = num.array(data_history['close'])
     highArray = num.array(data_history['high'])
     lowArray = num.array(data_history['low'])

     doubleCloseArray = num.asarray(closeArray,dtype='double')
     doubleHighArray = num.asarray(highArray,dtype='double')
     doubleLowArray = num.asarray(lowArray,dtype='double')

     SMA30_15_4 = ta.SMA(doubleCloseArray, timeperiod=4)
     SMA30_15_8 = ta.SMA(doubleCloseArray, timeperiod=8)
     SMA30_15_20 = ta.SMA(doubleCloseArray, timeperiod=20)
     SMA30_15_28 = ta.SMA(doubleCloseArray, timeperiod=28)

     if (SMA30_15_4[-1] > SMA30_15_4[-2] and SMA30_15_8[-1] > SMA30_15_8[-2] and SMA30_15_20[-1] > SMA30_15_20[-2] and SMA30_15_28[-1] > SMA30_15_28[-2]):
          str15QuShi = "均线15坚定买入"
     elif (SMA30_15_4[-1] < SMA30_15_4[-2] and SMA30_15_8[-1] < SMA30_15_8[-2] and SMA30_15_20[-1] < SMA30_15_20[-2] and SMA30_15_28[-1] < SMA30_15_28[-2]):
          str15QuShi = "均线15坚定卖出"
     else:
          str15QuShi = "均线15坚定空仓"

     print(name + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

     sendMail(name + + "%.1f" % closeArray[-1]  + "_" + str15QuShi, name + + "%.1f" % closeArray[-1]  + "_" + str15QuShi)

strategy("399006", "创业板指")
