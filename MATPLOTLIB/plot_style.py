"""
グラフに個別のスタイルを指定するための
方法について説明
"""
import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np
import pandas as pd

# 色の設定
"""
グラフに表示する線、背景色、枠線などさまざまな要素に色が指定できます。
以下のコードはplotメソッドのcolor引数を使用して、線色を指定
"""
fig, ax = plt.subplots()

# 線の色を名前で指定
ax.plot([1, 3], [3, 1], label='aqua', color='aqua')
# 16進数のRGBで指定
ax.plot([1, 3], [3, 1], label='#0000FF', color='#0000FF')
# RGBAをfloatで指定
ax.plot([1, 3], [2, 2], label='(0.1,0.2,0.5,0.3)', color=(0.1, 0.2, 0.5, 0.3))

ax.legend()  # 凡例を表示

plt.show()

# edgecolor引数：枠線の色を指定
fig, ax = plt.subplots()
ax.bar([1], [3], color='aqua')  # 塗りつぶしの色を指定
# 塗りつぶしの色と枠線の色を指定
ax.bar([2], [4], color='aqua', edgecolor='black')
plt.show()

# 線のスタイル
"""
折れ線グラフやグラフの枠線、区切り線など、さまざまな線に対してスタイルを適用できる
linewidth引数を指定すると線の幅を変更できる
単位はポイント
"""
fig, ax = plt.subplots()
# 5.5ポイントの幅の線で描画
ax.plot([1, 3], [3, 1], linewidth=5.5, label='5.5')
# 10ポイントの幅の線で描画
ax.plot([1, 3], [1, 3], linewidth=10, label='10')
ax.legend()
plt.show()

"""
線の幅を指定
linestyle引数で線の種類を指定できる
破線（--）, 一点鎖線（-.）, 点線（:）で
それぞれ描画する
"""
fig, ax = plt.subplots()
# 破線で描画
ax.plot([1, 3], [3, 1], linestyle='--', label='dashed')
# 一点鎖線で描画
ax.plot([1, 3], [1, 3], linestyle='-.', label='dashdot')
# 点線で描画
ax.plot([1, 3], [2, 2], linestyle=':', label='dotted')
ax.legend()
plt.show()

# フォント
"""
タイトル、凡例、軸ラベルなどのテキストに対しても
スタイルが設定できる
size引数を使用してフォントサイズを、weight引数を使用すると
フォントの太さを指定できる
family引数を使用してフォントの種類が指定でき
serif,sans-serif,cursive,fantasy,monospaceがデフォルトで使用できる
"""
fig, ax = plt.subplots()
ax.set_xlabel('xlabel', family='fantasy', size=20, weight='bold')
ax.set_ylabel('ylabel', family='cursive', size=40, weight='light')
ax.set_title('graph title', family='monospace', size=25, weight='heavy')
plt.show()

"""
フォントの設定を辞書データとして作成
fontdict引数に一度に指定できる
"""
# フォントのスタイルを辞書で定義
fontdict = {
    'family': 'fantasy',
    'size': 20,
    'weight': 'normal',
}
fig, ax = plt.subplots()
ax.set_xlabel('xlabel', fontdict=fontdict)
ax.set_ylabel('ylabel', fontdict=fontdict)
# 個別指定したsizeで上書き可能
ax.set_title('graph title', fontdict=fontdict, size=40)
plt.show()

# テキスト描画
"""
textメソッドを使用するとグラフに任意のテキストを指定できる
第一、第二引数にはテキストの左下のX,Y座標を指定。
"""
fig, ax = plt.subplots()
ax.text(0.2, 0.4, 'Text', size=20)  # Textというテキストを描画
plt.show()

# pandasオブジェクトからグラフ描画
"""
pandasのDataFrame, Seriesからグラフを描画できる
"""
matplotlib.style.use('ggplot')  # スタイルを指定

# DataFrameを作成
df = pd.DataFrame({'A': [1, 2, 3], 'B': [3, 1, 2]})
df.plot()  # 折れ線グラフを描画
plt.show()

# ランダムに3行2列のデータを生成してDataFrameを作成
np.random.seed(123)
df2 = pd.DataFrame(np.random.rand(3, 2), columns=['y1', 'y2'])
df2.plot.bar()  # 棒グラフを描画
plt.show()

df2.plot.bar(stacked=True)  # 積み上げ棒グラフを描画
plt.show()
