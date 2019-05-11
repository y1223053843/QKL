#encoding=utf-8
import pandas as pd
import time
import numpy as num
import ccxt
import talib as ta
from email_util import *

def jisuan():
    gateio = ccxt.gateio()
    limit = 500
    current_time = int(time.time()//60*60*1000)

    since_time = current_time - limit * 5 * 60 * 1000
    data = gateio.fetch_ohlcv(symbol='BTC/USDT',timeframe='5m', limit=500,since=since_time)
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

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("LOWER===============" + str(lowArray[-1]))
    print("HIGHER==============" + str(highArray[-1]))
    print("BULL upperband======" + str(upperband[-1]))
    print("BULL middleband=====" + str(middleband[-1]))
    print("BULL lowerband======" + str(lowerband[-1]))

    return upperband, middleband, lowerband,closeArray,highArray,lowArray

upperband, middleband, lowerband,closeArray,highArray,lowArray  = jisuan()

#sendMail("【BTC/USDT】触发5分钟布林线下沿,当前价格：" + str(closeArray[-1]), "【BTC/USDT】触发5分钟布林线下沿,当前价格：" + str(closeArray[-1]))
if (lowArray[-1] <= lowerband[-1]):
    sendMail("BTC/USDT触5分BL下沿：" + str(closeArray[-1]), "BTC/USDT触5分BL下沿：" + str(closeArray[-1]))
if (highArray[-1] >= upperband[-1]):
    sendMail("BTC/USDT触5分BL上沿：" + str(closeArray[-1]), "BTC/USDT触5分BL上沿：" + str(closeArray[-1]))



