import pandas as pd
import numpy as np

df = pd.read_excel("data/201704health.xlsx")

# 不要なカラムの削除
df = df.drop("日付", axis=1)
print(df)

# カラム挿入
df.loc[:, "歩数/カロリー"] = df.loc[:, "歩数"] / df.loc[:, "摂取カロリー"]
print(df)

# 歩数/カロリーを基に、運動指数カラムを追加する
# 条件は、3以下をLow, 3を超え6以下をMid, 6を超えるのをHigh
# exercise_judgeという関数で作成


def exercise_judge(ex):
    if ex <= 3.0:
        return "Low"
    elif 3.0 < ex <= 6.0:
        return "Mid"
    else:
        return "Hight"


df.loc[:, "運動指数"] = df.loc[:, "歩数/カロリー"].apply(exercise_judge)
# pickleでデータ出力
df.to_pickle("data/df_201704health.pickle")

"""
運動指数に入っている["High","Mid","Low"]のデータを
3カラムに分割し該当箇所に1を入れ
非該当箇所に0を入れたDataFrameをget_dummies関数を作成
引数にprefix="運動"と与えてカラム名の先頭の文字を決める
One-hotエンコーディングという技術を使っている
"""
df_moved = pd.get_dummies(df.loc[:, "運動指数"], prefix="運動")
print(df_moved)

df_moved.to_pickle("data/df_201704moved.pickle")
