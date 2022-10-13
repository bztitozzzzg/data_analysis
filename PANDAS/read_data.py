import pandas as pd

# データ読み込み：csvファイル
df = pd.read_csv("data/201704health.csv", encoding="utf-8")
print("data/201704health.csv")
print(df)

# データ読み込み：Excelファイル
df = pd.read_excel("data/201704health.xlsx")
print("data/201704health.xlsx")
print(df)

# データ読み込み：WebサイトのHTMLから表を取得
url = "https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%83%E3%83%97%E3%83%AC%E3%83%99%E3%83%AB%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E4%B8%80%E8%A6%A7"
tables = pd.read_html(url)
print(len(tables))

# 国別コードトップレベルドメインを取得
print(tables[4])
