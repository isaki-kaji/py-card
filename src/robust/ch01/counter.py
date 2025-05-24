from collections import Counter
import dataclasses


@dataclasses.dataclass
class Cookbook:
    author: str


def create_author_count_mapping(cookbooks: list[Cookbook]):
    return Counter(book.author for book in cookbooks)
