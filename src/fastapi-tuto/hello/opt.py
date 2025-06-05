from typing import Optional


def get_profile(email: str, username: Optional[str], age: Optional[int]) -> dict:
    profile = {"email": email}
    if username:
        profile["username"] = username
    if age:
        profile["age"] = age
    return profile
