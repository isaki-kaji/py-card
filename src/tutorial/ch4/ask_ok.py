'''
'y', 'ye', 'yes'が入力されたらTrueを、'n', 'no', 'nop', 'nope'が入力されたらFalseを返す関数。
指定の値以外が入力されたらリトライ。
リトライはデフォルトで4回まで。それを超えたらエラーを返す。
'''


def ask_ok(prompt, retries=4, reminder="再試行してください"):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if (retries < 0):
            raise ValueError()
        print(reminder)
