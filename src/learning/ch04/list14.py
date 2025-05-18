'''
objがintの時は絶対値を出力し、strの時は先頭の文字を出力する。
'''

obj = -123

match obj:
    case int():
        print(abs(obj))
    case str():
        print(obj[0])
    case _:
        print("意図しない型です。")
