import pyupbit
import numpy as np
import pandas as pd

np.set_printoptions()

df = pyupbit.get_ohlcv("KRW-XRP", interval = "minutes30")

df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
df['hpr'] = df['ror'].cumprod()
df['MDD'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

macd_short, macd_long, macd_signal = 12,26,9 
df["MACD_short"] = df["close"].ewm(span=macd_short).mean() 
df["MACD_long"] = df["close"].ewm(span=macd_long).mean() 
df["MACD"] = df.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 
df["MACD_signal"]  = df["MACD"].ewm(span=macd_signal).mean() 
df["MACD_oscillator"] = df.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 
df["MACD_sign"] = df.apply(lambda x: ("buy" if x["MACD"]>x["MACD_signal"] else "sell"), axis=1)

df.to_excel("xrp.xlsx")

print("MDD(%): ", df['MDD'].max())


dataf = pd.read_excel('xrp.xlsx')
for index, row in dataf.iterrows():
    if row['MACD_sign'] == 'buy':
        print("BUY RIGHT NOW")
    elif row['MACD_sign'] == 'sell':
        print("SELL NOW")
    else:
        exit
        