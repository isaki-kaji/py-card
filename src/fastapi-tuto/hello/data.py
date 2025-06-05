"""UserクラスはIDと名前を属性に持つ
パスパラメータでuser_idを要し、ユーザが存在すればそれを、存在しなければ404を返す。"""

from fastapi import FastAPI, HTTPException
from typing import Optional


class Book:
    def __init__(self, id: int, cateogry: str):
        self.id = id
        self.category = cateogry


books: list[Book] = []


def get_books_by_category(category: Optional[str] = None) -> list[Book]:
    if category is None:
        return books
    return [book for book in books if book.category == category]
