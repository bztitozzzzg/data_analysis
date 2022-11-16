import numpy as np
import pandas as pd
np.random.seed(123)
dates = pd.date_range(start="2020-01-01", periods=31)
df = pd.DataFrame(np.random.randint(1, 10, 31), index=dates, columns=["rand"])
print(df)

df_year = pd.DataFrame(df.groupby(pd.Grouper(freq='W-MON')).sum(), columns=["rand"] )
print(df_year)