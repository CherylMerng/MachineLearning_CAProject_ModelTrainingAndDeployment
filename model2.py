import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import sklearn

#df = pd.read_csv('AMZN.csv', index_col= 'Date', parse_dates=True, infer_datetime_format=True)
df = pdr.DataReader('AMZN', data_source='yahoo', start='2009-11-01', end='2022-11-11')

#see graph 
plt.figure(figsize=(18,12))
plt.plot(df.iloc[:,0:4])
# df.iloc[:,0:4].plot()
df.iloc[:,-1].plot(ylabel='Volume')

RECENT_PERIOD = 200
df.Close[-RECENT_PERIOD:]
df.Close[-RECENT_PERIOD:].mean()  
df.Close[-RECENT_PERIOD:].sum()  
moving_avg_200 = df.Close.rolling(window=200).mean().shift(1)
moving_avg_50 = df.Close.rolling(window=50
).mean().shift(1)

print ('moving average 200:\n',moving_avg_200.head())
print ('moving AVG 50:\n', moving_avg_50.head())

# plot the graphs with different moving average
plt.figure(figsize=(16,10))
plt.plot(df.index, df.Close, label='Closing Price')
plt.plot(df.index, moving_avg_200, label='200 MA', color='orange')
plt.plot(df.index, moving_avg_50, label='50 MA', color='magenta')
plt.legend(loc='upper left')
plt.show()

moving_avg_50.to_pickle("50_MA.pkl")
moving_avg_200.to_pickle("200_MA.pkl")

