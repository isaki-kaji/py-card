from collections import defaultdict
import dataclasses


@dataclasses.dataclass
class Cookbook:
    author: str


def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter = defaultdict(lambda: 0)
    for cb in cookbooks:
        counter[cb.author] += 1
    return counter
