import matplotlib.pyplot as plt
import matplotlib.style

fig, ax = plt.subplots(2)  # 2つのサブプロットを配置
plt.show()

# 2つのサブプロット
fig, axes = plt.subplots(2, 2)
plt.show()

# 2行2列のサブプロット
fig, axes = plt.subplots(ncols=2)  # 1行2列のサブプロットを配置
plt.show()

# グラフのスタイル
# スタイルの一覧を表示
print(matplotlib.style.available)

# グラフのスタイルにclassicを指定
matplotlib.style.use('classic')
fig, ax = plt.subplots()
ax.plot([1, 2])
plt.show()

# タイトル
fig, axes = plt.subplots(ncols=2)

# サブプロットにタイトルを設定
axes[0].set_title('subplot title 0')
axes[1].set_title('subplot title 1')

# 描画オブジェクトにタイトルを設定
fig.suptitle('figure title')

plt.show()

# 軸ラベル
fig, ax = plt.subplots()

ax.set_xlabel('x label')  # X軸にラベルを設定
ax.set_ylabel('y label')  # Y軸にラベルを設定

plt.show()

# 凡例
fig, ax = plt.subplots()

# 凡例用のラベルを設定
ax.plot([1, 2, 3], [2, 4, 9], label='legend label')
ax.legend(loc='best')  # 凡例を表示
# 凡例の表示位置は変更できる
# upper left/right lower left/rightなど
plt.show()

# ファイル出力
fig, ax = plt.subplots()
ax.set_title('subplot title')
fig.savefig('sample-figure.png')  # png形式で保存
fig.savefig('sample-figure.svg')  # svg形式で保存
