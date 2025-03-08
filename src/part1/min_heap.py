# insert, delete aka poll/pop, with heapify up and down
# for update we need to keep a hashmap from index to valu

# Follow-up: 
#   1. Make it generic so it holds any value 
#   2. Make it configurable, like java, pass a comparator so you can make it 
#      min or max heap.

# principles of a min hesp:
# 1. a min heap binary tree is a tree where the root element is the minimum
# the above definition holds true for all the sub trees in the tree
# 2. it is also a complete binary tree except for the last level

class MinHeap():
    def __init__(self):
        self.length = 0
        self.arr = []

    def insert(self, value: int):
        if self.length == 0:
            

    def delete(self): ...
