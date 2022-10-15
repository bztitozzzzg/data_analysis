import numpy as np
import pandas as pd
np.random.seed(123)
dates = pd.date_range(start="2017-04-01", periods=365)
df = pd.DataFrame(np.random.randint(1, 31, 365), index=dates, columns=["rand"])
df_year = pd.DataFrame(df.groupby(
    pd.Grouper(freq='W-SAT')).sum(), columns=["rand"])
