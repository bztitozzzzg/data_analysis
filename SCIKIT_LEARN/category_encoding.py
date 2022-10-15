from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder, StandardScaler
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'a', 'b', 'c']
})
print(df)


# カテゴリ変数のエンコーディング
"""
カテゴリ変数のエンコーディングとは、
「a -> 0, b -> 1, c -> 2」のようにカテゴリ変数を数値（整数）に
変換する処理。
カテゴリ変数をエンコーディングするには
preprocessingモジュールのLabelEncoderクラスを使用。
"""

# ラベルエンコーダのインスタンスを生成
le = LabelEncoder()
# ラベルのエンコーディング
le.fit(df['B'])
print(le.transform(df['B']))

# 元の値を確認
print(le.classes_)

# One-hotエンコーディング
"""
カテゴリ変数に対して行う符号化の処理。
テーブル形式のデータのカテゴリ変数の列について、取りうる値の分だけ列を増やして
各行の該当する値の列のみに1が、それ以外の列には0が入力されるように変換する
One-hotエンコーディングは機械学習に入力するデータの作成において
カテゴリ変数の変換等に多用される

One-hotエンコーディングはダミー変数化、生成された列の変数はダミー変数とも呼ばれる
One-hotエンコーディングを行うには、scikit-learnを用いる場合は
preprocessingモジュールのOneHotEncoderクラスを用い、またはpandasを用いる場合は
get_dummies関数を使用する。
"""
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'a', 'b', 'c']
})

# DataFrameをコピー
df_ohe = df.copy()
# ラベルエンコーダのインスタンス化
le = LabelEncoder()
# 英語のa, b, cを1, 2, 3に変換
df_ohe['B'] = le.fit_transform(df_ohe['B'])
# One-hotエンコーダのインスタンス化
ohe = ColumnTransformer(
    [("OneHotEncoder", OneHotEncoder(), [1])], remainder='passthrough')
# One-hotエンコーディング
print(ohe.fit_transform(df_ohe))

# 特徴量の正規化
"""
特徴量の正規化とは、特徴量の大きさをそろえる処理。
特徴量の値が2桁の数値（数十のオーダ）、別の特徴量の値が4桁の数値（数千のオーダ）とした場合
後者の数千のオーダの特徴量に大きな影響を受けて、全社の数十のオーダの特徴量が軽視されやすくなる
こうした状況を防ぐために、2つの特徴量のオーダが同様になるように尺度を揃える必要がある。
分散正規化と、最小最大正規化の2つに着目する
"""

# 分散正規化
"""
分散正規化とは、、、
特徴量の平均が0、標準偏差が1となるように特徴量を変換する処理
標準化やz変換と呼ばれる
数式は、以下
x' = x - μ / δ
x：特徴量
x'：分散正規化された特徴量
μ：この特徴量の平均
δ：標準偏差
"""
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [100, 200, 400, 500, 800]
})

# 列Aの平均は次の式で計算される
# 1 + 2 + 3 + 4 + 5 / 5 = 3

# 標準偏差は次の式で計算される
# √(1/5 * {(1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2}
# = √2 = 1.41421356

# 列Bの平均は次の式で計算される
# # 100 + 200 + 400 + 500 + 800 / 5 = 400

# 標準偏差は次の式で計算される
# √(1/5 * {(100-400)^2 + (200-400)^2 + (400-400)^2 + (500-400)^2 + (800-400)^2}
# = √60000 = 244.94897428

# 列Aの2行目に分散正規化を行うと、分散正規化を行った後の値は
# 次の式で計算される
# 2 - 3 / √2 = -√2/2 = -0.70710678

# また、列Bの4行目に対しては次の式で計算される
# 500 - 400 / √60000 = 0.40824829

# 分散正規化のインスタンスを生成
stdsc = StandardScaler()
# 分散正規化を実行
stdsc.fit(df)
print(stdsc.transform(df))

# 最小最大正規化
"""
最小最大正規化は、特徴量の最小値が0, 最大値が1をとるように
特徴量を正規化する処理
数式は以下
x' = x-xmin / xmax-xmin
x:特徴量
x':最小最大正規化された特徴量
xmin:特徴量の最小値
xmax:特徴量の最大値
"""

# 最小最大正規化のインスタンスを生成
mmsc = MinMaxScaler()
# 最小最大正規化を実行
mmsc.fit(df)
print(mmsc.transform(df))
