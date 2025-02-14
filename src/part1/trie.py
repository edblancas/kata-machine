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


class TNode:
    def __init__(self):
        self.letter = dict()
        self.word_end = False


class Trie():
    def __init__(self):
        self.root = TNode()


    def insert(self, item: str) -> None:
        curr = self.root
        for c in item:
            if curr.letter.get(c):
                curr = curr.letter[c]
            else:
                curr.letter[c] = TNode()
                curr = curr.letter[c]
        curr.word_end = True


    def delete(self, item: str) -> None:
        def has_letters(tnode):
            return len(tnode.letter) > 0

        def delete_rec(curr, idx):
            if idx >= len(item):
                curr.word_end = False
                return

            delete_rec(curr.letter.get(item[idx]), idx + 1)

            if not has_letters(curr):
                del curr

        delete_rec(self.root, 0)


    def find(self, partial: str) -> list[str]:
        def find_partial():
            curr = self.root
            for c in partial:
                if curr.letter.get(c):
                    curr = curr.letter[c]
            return curr

        sub_tree = find_partial()
        path = []

        def dfs(curr, curr_str):
            if curr.word_end:
                path.append(''.join([partial] + curr_str))
            if not curr:
                return

            for k, v in curr.letter.items():
                curr_str.append(k)
                dfs(v, curr_str)
                curr_str.pop()

        dfs(sub_tree, [])
        return path
