# Trie Tree
# implementation: with nodes, arrays, hash
# problem: autocomplete english dictionary
# operations: insert, delete
# follow-up: cache system

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    letter: list[Node | None] = field(default_factory=lambda: [None] * 26)
    word_end: bool = False

class Trie():
    def __init__(self): ...

    def insert(self, item: str) -> None: ...

    def delete(self, item: str) -> None: ...

    def find(self, partial: str) -> list[str]: ...
