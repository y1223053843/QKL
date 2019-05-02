#encoding=utf-8
import pandas as pd
import time
import numpy as num
import ccxt
import talib as ta
from email_util import *

huobi = ccxt.huobipro()

limit = 500
current_time = int(time.time()//60*60*1000)
print(current_time)

since_time = current_time - limit * 60 * 60 * 1000

data = huobi.fetch_ohlcv(symbol='TRX/USDT',timeframe='1h', limit=500,since=since_time)
df = pd.DataFrame(data)
df = df.rename(columns={0: 'open_time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms') + pd.Timedelta(hours=8)

# 02、 数据格式处理、并计算布林线值
closeArray = num.array(df['close'])
highArray = num.array(df['high'])
lowArray = num.array(df['low'])

doubleCloseArray = num.asarray(closeArray, dtype='double')
doubleHighArray = num.asarray(highArray, dtype='double')
doubleLowArray = num.asarray(lowArray, dtype='double')

upperband, middleband, lowerband = ta.BBANDS(doubleCloseArray, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

sendMail("111111111111111","11111111111")
