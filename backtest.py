  
import pyupbit
import numpy as np

np.set_printoptions()
#OHLCV (open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-XRP", interval = "minutes30")

# 변동성 돌파 기준 범위 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# # range 컬럼을 한칸씩 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# np.where (조건문, 참일때 값, 거짓일떄 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

#누적 곡 계산()
df['hpr'] = df['ror'].cumprod()
df['MDD'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['MDD'].max())


#추가 macd 지표

macd_short, macd_long, macd_signal = 12,26,9 #기본값 
df["MACD_short"] = df["close"].ewm(span=macd_short).mean() 

df["MACD_long"] = df["close"].ewm(span=macd_long).mean() 

df["MACD"] = df.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 

df["MACD_signal"]  = df["MACD"].ewm(span=macd_signal).mean() 

df["MACD_oscillator"] = df.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 

df["MACD_sign"] = df.apply(lambda x: ("buy" if x["MACD"]>x["MACD_signal"] else "sell"), axis=1)

df.to_excel("xrp.xlsx")