import numpy as np
import pandas as pd

# read_csvメソッド
df = pd.read_csv("data/c01.csv", encoding="shift-jis")
print(df)
"""
実行結果
                                               都道府県コード 都道府県名   元号  和暦（年）   西暦（年）    注    人口（総数）     人口（男）     人口（女）
0                                                   00    全国   大正    9.0  1920.0  NaN  55963053  28044185  27918868
1                                                   01   北海道   大正    9.0  1920.0  NaN   2359183   1244322   1114861
2                                                   02   青森県   大正    9.0  1920.0  NaN    756454    381293    375161
3                                                   03   岩手県   大正    9.0  1920.0  NaN    845540    421069    424471
4                                                   04   宮城県   大正    9.0  1920.0  NaN    961768    485309    476459
..                                                 ...   ...  ...    ...     ...  ...       ...       ...       ...
977                                                 45   宮崎県   平成   27.0  2015.0  NaN   1104069    519242    584827
978                                                 46  鹿児島県   平成   27.0  2015.0  NaN   1648177    773061    875116
979                                                 47   沖縄県   平成   27.0  2015.0  NaN   1433566    704619    728947
980                         1)　沖縄県は調査されなかったため，含まれていない。   NaN  NaN    NaN     NaN  NaN       NaN       NaN       NaN
981  2)　長野県西筑摩群山口村と岐阜県中津川市の境界紛争地域人口（男39人，女34人）は全国に含...   NaN  NaN    NaN     NaN  NaN       NaN       NaN       NaN        

[982 rows x 9 columns]
"""

print(end='\n')

# to_csvメソッド
sample_df = pd.DataFrame(np.arange(20).reshape((5, 4)),
                         index=["1行目", "2行目", "3行目", "4行目", "5行目"],
                         columns=["A列", "B列", "C列", "D列"])
print(sample_df)
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
2行目   4   5   6   7
3行目   8   9  10  11
4行目  12  13  14  15
5行目  16  17  18  19
"""

print(end='\n')

sample_df.to_csv("data/sample_df.csv")
"""
実行結果
data/sample_df.csv
,A列,B列,C列,D列
1行目,0,1,2,3
2行目,4,5,6,7
3行目,8,9,10,11
4行目,12,13,14,15
5行目,16,17,18,19
"""

print(end='\n')

# read_excelメソッド
df = pd.read_excel("data/c01.xlsx")
print(df)
"""
実行結果
     Unnamed: 0                                            都道府県コード 都道府県名   元号  和暦（年）   西暦（年）    注    人口（総数）     人口（男）     人口
（女）
0             0                                                 00    全国   大正    9.0  1920.0  NaN  55963053  28044185  27918868
1             1                                                 01   北海道   大正    9.0  1920.0  NaN   2359183   1244322   1114861
2             2                                                 02   青森県   大正    9.0  1920.0  NaN    756454    381293    375161
3             3                                                 03   岩手県   大正    9.0  1920.0  NaN    845540    421069    424471
4             4                                                 04   宮城県   大正    9.0  1920.0  NaN    961768    485309    476459
..          ...                                                ...   ...  ...    ...     ...  ...       ...       ...       ...
977         977                                                 45   宮崎県   平成   27.0  2015.0  NaN   1104069    519242    584827
978         978                                                 46  鹿児島県   平成   27.0  2015.0  NaN   1648177    773061    875116
979         979                                                 47   沖縄県   平成   27.0  2015.0  NaN   1433566    704619    728947
980         980                         1)　沖縄県は調査されなかったため，含まれていない。   NaN  NaN    NaN     NaN  NaN       NaN       NaN       NaN
981         981  2)　長野県西筑摩群山口村と岐阜県中津川市の境界紛争地域人口（男39人，女34人）は全国に含...   NaN  NaN    NaN     NaN  NaN       NaN       NaN      
 NaN

[982 rows x 10 columns]
"""

print(end='\n')

sample_df = pd.DataFrame(np.arange(20).reshape((5, 4)),
                         index=["1行目", "2行目", "3行目", "4行目", "5行目"],
                         columns=["A列", "B列", "C列", "D列"])
print(sample_df)
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
2行目   4   5   6   7
3行目   8   9  10  11
4行目  12  13  14  15
5行目  16  17  18  19
"""

print(end='\n')

# to_excelメソッド
sample_df.to_excel("data/sample_df.xlsx")
"""
実行結果
C:\work\data_analysis\DIVE_INTO_EXAM\PANDAS\data\sample_df.xlsx
"""

print(end='\n')

# read_htmlメソッド
url = "https://www.e-stat.go.jp/stat-search/files?page=1&query=%E4%BA%BA%E5%8F%A3&layout=dataset&stat_infid=000032126213&metadata=1&data=1"
tables = pd.read_html(url)
print(len(tables))
"""
実行結果
4
"""
df = tables[0]
print(df)
"""
実行結果
            0                                                  1    2
0       政府統計名                                               人口推計   詳細
1     政府統計コード                                           00200524  NaN
2       調査の概要  人口推計は、国勢調査による人口を基に、その後の各月における出生・死亡、入国・出国などの人口の...  NaN
3       提供統計名                                               人口推計  NaN
4       提供分類1                                           各月1日現在人口  NaN
5        統計表名  年齢(5歳階級)、男女別人口(2021年5月平成27年国勢調査を基準とする推計値、2021年...  NaN
6   データセットの概要                                                NaN  NaN
7   統計分野（大分類）                                              人口・世帯  NaN
8   統計分野（小分類）                                                 人口  NaN
9        担当機関                                                総務省  NaN
10       担当課室                                      統計局統計調査部国勢統計課  NaN
11    政府統計URL        http://www.stat.go.jp/data/jinsui/index.htm  NaN
12      統計の種類                                               基幹統計  NaN
13       調査年月                                          2021年 10月  NaN
14    公開年月日時分                                   2021-10-20 14:00  NaN
15       提供周期                                                 月次  NaN
16     集計地域区分                                               該当なし  NaN
"""

print(end='\n')

# to_pickleメソッド
df.to_pickle("data/stock_df.pickle")
"""
実行結果
C:\work\data_analysis\DIVE_INTO_EXAM\PANDAS\data\stock_df.pickle
"""

print(end='\n')

# read_pickleメソッド
stock_df = pd.read_pickle("data/stock_df.pickle")
print(stock_df)
"""
実行結果
            0                                                  1    2
0       政府統計名                                               人口推計   詳細
1     政府統計コード                                           00200524  NaN
2       調査の概要  人口推計は、国勢調査による人口を基に、その後の各月における出生・死亡、入国・出国などの人口の...  NaN
3       提供統計名                                               人口推計  NaN
4       提供分類1                                           各月1日現在人口  NaN
5        統計表名  年齢(5歳階級)、男女別人口(2021年5月平成27年国勢調査を基準とする推計値、2021年...  NaN
6   データセットの概要                                                NaN  NaN
7   統計分野（大分類）                                              人口・世帯  NaN
8   統計分野（小分類）                                                 人口  NaN
9        担当機関                                                総務省  NaN
10       担当課室                                      統計局統計調査部国勢統計課  NaN
11    政府統計URL        http://www.stat.go.jp/data/jinsui/index.htm  NaN
12      統計の種類                                               基幹統計  NaN
13       調査年月                                          2021年 10月  NaN
14    公開年月日時分                                   2021-10-20 14:00  NaN
15       提供周期                                                 月次  NaN
16     集計地域区分                                               該当なし  NaN
"""
