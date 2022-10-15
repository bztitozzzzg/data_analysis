import re


def re_compile(str):
    prog = re.compile(r'py?(th|ers)oni?(a[lmn]|c)?', re.IGNORECASE)
    ret = prog.search(str)
    if ret is None:
        print('エラー:', str)
    else:
        print("正規表現チェックOK:", ret[0])


re_compile('Python')  # 1
re_compile('personal')  # 2
re_compile('pythomian')  # 3
re_compile('PYTHONIC')  # 4
re_compile('The Zen of Python')  # 5

"""
実行結果
正規表現チェックOK: Python
正規表現チェックOK: personal
エラー: pythomian
正規表現チェックOK: PYTHONIC
正規表現チェックOK: Python
"""
