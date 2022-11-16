try :
    num = 1 / 0
except ZeroDivisionError :
    print('0で割ることはできません')
finally :
    num = 0 / 1
    print(num)