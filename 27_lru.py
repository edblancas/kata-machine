from typing import Any

# we combine the use of a double linked list with a hash map to get constant
# time lookup, insertion and deletion from any place
class LRU:
    def __init__(self, length: int):
        self.length = length

    def update(self, key: Any, value: Any) -> None:
        return

    def get(self, key: Any) -> Any | None:
        return None

