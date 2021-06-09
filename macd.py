import pyupbit
import numpy as np

np.set_printoptions()

df = pyupbit.get_ohlcv("KRW-TFUEL", interval = "minute30")

df["MACD_short"] = df["close"].ewm(span=macd_short).mean() 

df["MACD_long"] = df["close"].ewm(span=macd_long).mean() 

df["MACD"] = df.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 

df["MACD_signal"]  = df["MACD"].ewm(span=macd_signal).mean() 

df["MACD_oscillator"] = df.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 

df["MACD_sign"] = df.apply(lambda x: ("buy" if x["MACD"]>x["MACD_signal"] else "sell"), axis=1)


