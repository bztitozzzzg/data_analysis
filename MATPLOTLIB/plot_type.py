import matplotlib.pyplot as plt
import numpy as np

# 折れ線グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 1, 2]
ax.plot(x, y1)  # 折れ線グラフを描画
ax.plot(x, y2)

plt.show()

# sin,cosカーブ曲線
x = np.arange(0.0, 15.0, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='sin')
ax.plot(x, y2, label='cos')
ax.legend()

plt.show()

# 棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [10, 2, 3]
ax.bar(x, y)  # 棒グラフを描画

plt.show()

# tick_label引数で目盛り設定
fig, ax = plt.subplots()
x = [1, 2, 3]
y = [10, 2, 3]
labels = ['spam', 'ham', 'egg']
# ax.bar(x, y, tick_label=labels)  # ラベルを指定
ax.barh(x, y, tick_label=labels)  # ラベルを指定

plt.show()

# 複数の棒グラフを描画
fig, ax = plt.subplots()
x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ['spam', 'ham', 'egg']

# y1とy2を足した値を格納
y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]

# y1とy2を足した高さの棒グラフを描画
ax.bar(x, y_total, tick_label=labels, label='y1')
ax.bar(x, y2, label='y2')
ax.legend()

plt.show()

# 散布図
"""
散布図を作成するにはscatterメソッドを使用。
散布図を再現するために、乱数のseedを指定
"""
fig, ax = plt.subplots()

# ランダムに50個の要素を生成
np.random.seed(123)
x = np.random.rand(50)
y = np.random.rand(50)

ax.scatter(x, y)  # 散布図を描画

plt.show()

# マーカーを変更して散布図を描画
fig, ax = plt.subplots()

# ランダムに50個の要素を生成
np.random.seed(123)
x = np.random.rand(50)
y = np.random.rand(50)

ax.scatter(x[0:10], y[0:10], marker='v', label='triangle down')  # 下向き三角
ax.scatter(x[10:20], y[10:20], marker='^', label='triangle up')  # 上向き三角
ax.scatter(x[20:30], y[20:30], marker='s', label='square')  # 正方形
ax.scatter(x[30:40], y[30:40], marker='*', label='start')  # 星型
ax.scatter(x[40:50], y[40:50], marker='x', label='x')  # X
ax.legend()

plt.show()

# ヒストグラム
"""
ヒストグラムを描画するためにはhistメソッドを使用。
以下は正規分布に従うランダムな値をヒストグラムで描画
"""

# データを生成
np.random.seed(123)
mu = 100  # 平均値
sigma = 15  # 標準偏差
x = np.random.normal(mu, sigma, 1000)

fig, ax = plt.subplots()

# ヒストグラムを描画
n, bins, patches = ax.hist(x)

plt.show()

"""
nには各ビン(棒)の度数（要素数）が格納されている。
binsにはビンの境界の値、patchesにはビンを描画するための情報が入っている
nとbinsを仕様とすると以下のコードで度数分布表が出力できる
"""
for i, num in enumerate(n):
    print('{:.2f} - {:.2f}: {}'.format(bins[i], bins[i + 1], num))

# histメソッドの引数にorientation='horizontal'と指定
# 横向きのヒストグラムを描画できる
fig, ax = plt.subplots()
ax.hist(x, orientation='horizontal')
plt.show()

# histメソッドの引数にstacked=Trueと指定
# 積み上げたヒストグラムが描画される
fig, ax = plt.subplots()
np.random.seed(123)
mu = 100  # 平均値
x0 = np.random.normal(mu, 20, 1000)
x1 = np.random.normal(mu, 15, 1000)
x2 = np.random.normal(mu, 10, 1000)
labels = ['x0', 'x1', 'x2']
ax.hist((x0, x1, x2), label=labels, stacked=True)
plt.show()

# 箱ひげ図
"""
箱ひげ図を描画するにはboxplotメソッドを使用。
"""
# 異なる標準偏差でデータを生成
np.random.seed(123)
x0 = np.random.normal(0, 20, 1000)
x1 = np.random.normal(0, 15, 1000)
x2 = np.random.normal(0, 10, 1000)

fig, ax = plt.subplots()
labels = ['x0', 'x1', 'x2']
ax.boxplot((x0, x1, x2), labels=labels)  # 箱ひげ図を描画
plt.show()

# boxplotの引数にvert=Falseを指定
# 横向きの箱ひげ図を描画
fig, ax = plt.subplots()
labels = ['x0', 'x1', 'x2']
ax.boxplot((x0, x1, x2), labels=labels, vert=False)  # 横向きの箱ひげ図を描画
plt.show()

# 円グラフ
"""
円グラフはpieメソッドを使用。
"""
labels = ['spam', 'ham', 'egg']
x = [10, 3, 1]
fig, ax = plt.subplots()
ax.pie(x, labels=labels)  # 円グラフを描画
plt.show()

"""
アスペクト比を保持するために、サブプロットに対して
axis('equal')と指定
"""
fig, ax = plt.subplots()
ax.pie(x, labels=labels)
ax.axis('equal')  # アスペクト比を保持して描画する
plt.show()

"""
円グラフはデフォルトでは右（時計の3時の位置）から
反時計回りの順番に各要素が配置される。
上（時計の12時の位置）から描画を始めるには
startangle=90（90度の位置）と指定し、時計回りに配置するには
conterclock=Falseと指定
"""
fig, ax = plt.subplots()
ax.pie(x, labels=labels, startangle=90, counterclock=False)  # 上から時計回り
ax.axis('equal')
plt.show()

"""
影をつけるにはshadow=Trueと指定
autopct='%1.2f%%'のように指定すると
値のパーセント表記が追加される
autopctでは何桁まで表示するか指定できる
"""
fig, ax = plt.subplots()
ax.pie(x, labels=labels, startangle=90, counterclock=False,
       shadow=True, autopct='%1.2f%%')  # 影と%表記を追加
ax.axis('equal')
plt.show()
