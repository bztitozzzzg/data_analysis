from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

"""
問8
以下のコードは、欠損値をカラムごとの平均値で埋めるために書かれたコードである。
以下のコードのXXXの部分に記述されるコードとして正しいものを選べ
※dfは欠損を含むデータが格納されているpandasデータフレームである, versionは0.20以上
"""

df = pd.DataFrame({"Sample": [10, 100, 1000]})

imp = SimpleImputer(strategy="mean")  # meanは平均値を指す
imp.fit(df)
imp.transform(df)

print(end="\n\n")

"""
問10
以下のようなpandasデータフレームdfがある。
日付カラムをこのデータフレームのインデックスにする場合のコードとして正しいものを選べ
"""
df = pd.DataFrame(
    {
        "日付": ["2000/3/27", "2000/3/28", "2000/3/29", "2000/3/30", "2000/3/31"],
        "始値": [19976.14063, 20273.67969, 20406.56055, 20706.44922, 20371.07031],
        "終値": [20281.02930, 20374.33984, 20706.65039, 20441.50000, 20337.32031],
    }
)
df.set_index("日付")
print(df)
"""
実行結果
        日付         始値          終値
0  2000/3/27  19976.14063  20281.02930
1  2000/3/28  20273.67969  20374.33984
2  2000/3/29  20406.56055  20706.65039
3  2000/3/30  20706.44922  20441.50000
4  2000/3/31  20371.07031  20337.32031
pandasデータフレームでは、set_index(カラム名)を使用することにより、データフレームのindexを変更することができます。
"""

print(end="\n\n")

"""
問11
enjoyという出力を返すように、XXXXに当てはまるものとして正しいものを選べ
"""
import re

pattern = r"enjoy"
text = "enjoy data science"
matchOB = re.match(pattern, text)
if matchOB:
    print(matchOB.group())

"""
実行結果
enjoy
groupメソッドはマッチした文字列を取得
"""

print(end="\n\n")

"""
問13
以下のコードを実行した際に出力されるグラフとして正しいものを選べ
"""
import matplotlib.pyplot as plt
import math

x_list = [i for i in range(10)]
y_list = list(map(lambda x: x**2, x_list))
y_list2 = list(map(lambda x: x**3 + x**2, x_list))
y_list3 = list(map(lambda x: (math.e) ** x, x_list))

plt.plot(x_list, y_list, label="x**2")
plt.plot(x_list, y_list2, label="x**3+x**2")
plt.plot(x_list, y_list3, label="exp(x)")
plt.legend()
# plt.show()
"""
着眼点
注目したいのは label パラメータと legend メソッドを使っている所です。
yの値を3つ用意しており、これらを全てplotメソッドのlabelパラメータを使っています。
legend メソッドはこのlabelパラメータで定義したデータを表示させます。
legendでラベルが3つ出ているグラフが正解です。
"""

print(end="\n\n")

"""
問23
以下のような、ユーザーごとのサービス利用状況が格納されたデータフレームdfがある。
性別ごとの人数を棒グラフで表示するためのコードとして正しいものを選べ
"""
df = pd.DataFrame(
    {
        "ユーザーID": [0, 1, 2, 3, 4],
        "利用回数": [79.0, 78.0, 33.0, 55.0, 52.0],
        "利用料金": [4667.0, 5041.0, 8631.0, 8750.0, None],
        "性別": ["男性", "男性", "女性", "女性", "男性"],
        "既婚/独身": ["既婚", "独身", "既婚", "既婚", "既婚"],
    }
)
df["性別"].value_counts().plot.bar()
# plt.show()
"""
解説
value_countsメソッドを使うことで指定したカラムの要素の合計が取得できます。
その結果に対してplot.bar()を実行すると期待するグラフを作成できます。
"""

print(end="\n\n")

"""
問24
以下のコードの出力として正しいものを選べ
"""
A = [x for x in range(10)]
B = {x for x in range(20)}

print(A, len(A))
print(B, len(B))

if len(A) == 10:
    print("A")
elif len(A) == 10 & len(B) == 20:
    print("A,B")
else:
    print("None")
"""
実行結果
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 10
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19} 20
A
"""

print(end="\n\n")

"""
問30
以下のコードを実行した際の出力として正しいものを選べ
"""
a = np.array([[0, 1, 10], [0, 1, 10]])
b = np.array([100, 100, 100])
print(np.vstack([a, b]))
"""
実行結果
vstackは行（垂直）方向で行列結合
[[  0   1  10]
 [  0   1  10]
 [100 100 100]]
"""

print(end="\n\n")
print("******2回目******")

"""
問15
以下のようなグラフを描画するために、コードのXXX の部分に記述されるコードとして正しいものを選べ
"""
df = pd.DataFrame(
    {
        "国名": ["日本", "アメリカ", "イタリア", "フランス", "ロシア", "ブラジル", "イギリス"],
        "人口/万人": [12700, 32800, 6000, 6700, 14500, 20900, 6600],
    }
)

plt.rcParams["font.family"] = "AppleGothic"
# XXX
plt.pie(
    df["人口/万人"],
    labels=df["国名"],
    counterclock=False,
    startangle=90,
    autopct="%1.1f%%",
    pctdistance=0.8,
)
plt.xlabel("人口(万人)")
plt.show()
