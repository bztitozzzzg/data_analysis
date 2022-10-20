import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt

labels = ['サンプル1', 'サンプル2', 'サンプル3']
x = [10, 3, 1]
fig, ax = plt.subplots()
ax.pie(x, labels=labels)
plt.show()
"""
実行結果

"""

print(end='\n')

df = pd.DataFrame([['テレビ、ラジオや新聞等の広告', 5],
                   ['インターネット検索結果', 15],
                   ['インターネット上の広告', 25],
                   ['SNS広告', 50],
                   ['知人からの紹介', 1],
                   ['その他', 4]], columns=["媒体", "集計結果（%）"])
df
print(df)
"""
実行結果
               媒体  集計結果（%）      
0  テレビ、ラジオや新聞等の広告        5
1     インターネット検索結果       15   
2     インターネット上の広告       25   
3           SNS広告       50
4         知人からの紹介        1       
5             その他        4
"""

print(end='\n')

labels = df.loc[:, "媒体"]
rate = df.loc[:, "集計結果（%）"]

fig, ax = plt.subplots()
# ax.pie(rate, labels=labels)
# ax.pie(rate, labels=labels, startangle=90)
# ax.pie(rate, labels=labels, startangle=90, counterclock=False)
# ax.pie(rate, labels=labels, startangle=90, counterclock=False, shadow=True)
"""
ax.pie(rate, labels=labels, startangle=90,
       counterclock=False, autopct='%1.0f%%')
"""
explode=[0.2, 0, 0, 0, 0, 0]
ax.pie(rate, labels=labels, startangle=90, counterclock=False, explode=explode)
ax.axis('equal')
plt.show()
# 実行結果
