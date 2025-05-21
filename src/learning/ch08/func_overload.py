from typing import overload, Union

"""
引数valueがintであればstrに変換して返し、strであれば文字列の長さをintで返す関数
"""


@overload
def process(value: int) -> str: ...
@overload
def process(value: str) -> int: ...


def process(value: int | str) -> int | str:
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return len(value)
    else:
        raise TypeError("不正な型です。")


print(process())
