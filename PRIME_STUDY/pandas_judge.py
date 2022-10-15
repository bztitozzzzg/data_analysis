import pandas as pd
df = pd.DataFrame([[40, "a", True], [20, "b", False], [30, "c", False]])
df.index = ["01", "02", "03"]
df.columns = ["A", "B", "C"]


def judge(arg):
    if arg < 50:
        return "low"
    elif arg < 70:
        return "middle"
    else:
        return "high"


df.loc[:, "C"] = df.iloc[:, 0] * 2
print(df)
df.loc[:, "B"] = df.iloc[:, 2].apply(judge)
print(df)
_ = df["C"] > 50
df = df[_]
print(df)
print(df.iloc[0, 0], df.iloc[1, 1])

"""
実行結果
40 middle
"""
