import matplotlib.pyplot as plt

"""
オブジェクト指向スタイル
描画オブジェクトに対してサブプロットを追加して
サブプロットに対してグラフを描画する
1つのfigureオブジェクトに対して複数のサブプロットを
指定できる
"""
# データを用意
x = [1, 2, 3]
y = [2, 4, 9]

# 描画オブジェクト(fig)とサブプロット(ax)を生成
fig, ax = plt.subplots()

ax.plot(x, y)  # 折れ線グラフを描画
ax.set_title('OOP-style')  # タイトルを指定

plt.show()  # グラフを描画
