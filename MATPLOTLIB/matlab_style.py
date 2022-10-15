import matplotlib.pyplot as plt
import matplotlib.style

# ggplotスタイルを指定
matplotlib.style.use('ggplot')

# MATLABスタイル
"""
MATLABスタイルは数値解析ソフトウェアである
MATLABと似た形式
"""
# データを用意
x = [1, 2, 3]
y = [2, 4, 9]

plt.plot(x, y)  # 折れ線グラフを描画
plt.title('MATLAB-style')  # グラフにタイトルを設定

plt.show()  # グラフを表示
