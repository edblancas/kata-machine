# we combine the use of a double linked list with a hash map to get constant
# time lookup, insertion and deletion from any place
class LRU[K, V]:
    def __init__(self):
        self.length = 0

    def update(self, key: K, value: V) -> None:
        return

    def get(self, key: K) -> V | None:
        return None

