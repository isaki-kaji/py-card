'''
drinkがビール、日本酒、ワインのうちのどれかであれば醸造酒、ウイスキー、ブランデー、ジンのうちのどれかであれば蒸留酒と出力する。
'''


def sake(drink):
    match drink:
        case "ビール" | "日本酒" | "ワイン":
            print("醸造酒")
        case "ウイスキー" | "ブランデー" | "ジン":
            print("蒸留酒")
        case _:
            print("その他")


print(sake("水"))
