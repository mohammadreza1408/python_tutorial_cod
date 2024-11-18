import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')


print(pd.Series([1,2,3,"mohammad",0,np.nan,-1]))

dates = pd.date_range("20210101", periods=6)
print(dates)


print(np.random.randn(6,4))
df =pd.DataFrame(np.random.randn(6,4), index=dates, columns=["A","B","C","D"])
print(df)

print(df.dtypes)
print(df["A"])
print(df.describe())
print(df[df["A"]>0])





