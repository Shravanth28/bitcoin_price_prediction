import pandas as pd
from merlion.utils import TimeSeries

df=pd.read_csv("Bitcoin_price.csv")
df.head()

df.set_index('DATE', inplace=True)
df.index = pd.to_datetime(df.index)
df.index.freq = 'MS'

# Bring into Merlion's data structure
df_ts = TimeSeries.from_pd(df, freq='MS')

print(df_ts.is_aligned)

df_ts_train, df_ts_test = df_ts.bisect('2015-07-01')