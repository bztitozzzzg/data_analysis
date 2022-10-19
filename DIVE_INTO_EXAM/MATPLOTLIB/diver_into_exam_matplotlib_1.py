import matplotlib.style
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.show()

"""
実行結果
※DIVER_INTO_EXAM.xlsx#シート「Matplotlibとは」参照
"""

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
#ax.plot(x, y)
plt.show()

print(end='\n')

x1 = [1, 2, 3]
y1 = [2, 4, 6]
x2 = [1, 2, 3]
y2 = [-2, -4, -6]

fig, axes = plt.subplots(2)
axes[0].plot(x1, y1)
axes[1].plot(x2, y2)
plt.show()

print(end='\n')

fig, ax = plt.subplots(2, 2)
plt.show()

print(end='\n')

fig, ax = plt.subplots(ncols=2)
plt.show()

print(end='\n')

# 利用可能なスタイル一覧を表示（available）
matplotlib.style.available
print(matplotlib.style.available)
"""
実行結果
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

print(end='\n')

# use関数（指定したいスタイルを指定することで、スタイルを変更）
# matplotlib.style.use('seaborn')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

print(end='\n')

# dark_backgroundスタイル
# matplotlib.style.use('dark_background')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

print(end='\n')

x1 = [1, 2, 3]
y1 = [2, 4, 6]
x2 = [1, 2, 3]
y2 = [-2, -4, -6]

fig, axes = plt.subplots(1, 2)
axes[0].plot(x1, y1)
axes[1].plot(x2, y2)
axes[0].set_title('Subplot1 title')
axes[1].set_title('Subplot2 title')
fig.suptitle('Graph title')
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X lable')
ax.set_ylabel('Y lable')
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, label='sample legend')
ax.legend()
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, label='sample legend')
ax.legend(loc='lower right')
plt.show()

print(end='\n')

"""
解説
matplotlibのsubplotsには引数として、nrowsとrcolsがあります。
縦にnrows個、横にnclos個を描画する事が可能です。
また、引数は省略も可能です。
"""
fig, ax = plt.subplots(ncols=1)
plt.show()
