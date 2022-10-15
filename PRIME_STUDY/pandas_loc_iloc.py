"""
次のスクリプトを実行して10を出力させたい。[ア]に入るものの説明として正しいものはどれか。
"""
import pandas as pd
df = pd.DataFrame([[15, "a", True], [20, "b", False], [10, "c", False]])
df.index = ["01", "02", "03"]
df.columns = ["A", "B", "C"]
a = df.loc["03", "A"]
print(a)
a = df.iloc[2, 0]
print(a)
