from typing import NewType


class HotDog:
    pass


ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)


# 以下のような場合に有効
UserId = NewType('UserId', str)


def validate_user_id(uid: str) -> UserId:
    if not uid.isalnum() or len(uid) != 10:
        raise ValueError("Invalid user ID")
    return UserId(uid)


def get_user_info(uid: UserId):
    ...
