# Trie Tree
# implementation: with nodes, arrays, hash
# problem: autocomplete english dictionary
# operations: insert, delete
# follow-up: cache system

# O(h), h = height of the tree
# Is constant time cuz it's delimited by the longest english word
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    # we could use a dict of 26 str/char
    # but just a list with 26 places is more perfomant 
    # char place = ord(char) - ord('a')
    letter: list[Node | None] = field(default_factory=lambda: [None] * 26)
    word_end: bool = False

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, item: str) -> None:
        curr = self.root
        for c in item:
            place = Trie._char_place(c)
            if not curr.letter[place]:
                curr.letter[place] = Node()
            curr = curr.letter[place]
        curr.word_end = True

    @staticmethod
    def _char_place(char: str) -> int:
        return ord(char) - ord('a')

    @staticmethod
    def _char_str(place: int) -> str:
        return chr(place + ord('a'))

    # TODO do it DFS recursively deleting in post-order operation
    def delete(self, item: str) -> None:
        curr = self.root
        for c in item:
            place = Trie._char_place(c)
            before = curr.letter
            curr = curr.letter[place]
        curr.word_end = False
        for node in curr.letter:
            if node:
                return
        before.letter[place] = None

    def find(self, partial: str) -> list[str]:
        autocomplete_strs: list[str] = []
        curr = self.root
        for char in partial:
            place = Trie._char_place(char)
            curr = curr.letter[place]
        self._get_all_words(autocomplete_strs, list(partial), curr)
        return autocomplete_strs

    # DFS in pre-order traversal, we see it and added
    # this will be in alphabetical order
    # TODO Do it in BFS, and DFS iterative
    def _get_all_words(self, list_words, partial_list, node):
        if not node:
            return
        if node.word_end:
            list_words.append(''.join(partial_list))

        for i, char_node in enumerate(node.letter):
            if char_node:
                partial_list.append(self._char_str(i))
            self._get_all_words(list_words, partial_list, char_node)

        partial_list.pop()
