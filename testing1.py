import pandas as pd
import numpy as np
import pyupbit

np.set_printoptions()
df = pyupbit.get_ohlcv("KRW-TFUEL", interval="minute15")
print(df)
df.to_excel("ddd.xlsx")