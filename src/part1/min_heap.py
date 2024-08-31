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

# children i*2 + 1/2
# parent (i-1)//2

# insert: insert at the first leaf empty from left to right, then bubble up
# pop: remove the head/root value, then remove the first empty leaf from left to
#      right and set value to the head/root and bubble down.

# min heap
# bubble up: check if I'm < than my parent, yes: change value with it, repeat
# bubble down: If I'm > than the smallest of my children swap it with it, repeat

class MinHeap():
    def __init__(self):
        self.length = 0
        self.arr = []

    def insert(self, value: int):
        self.arr.append(value)
        self.length += 1
        if self.length > 0:
            self._bubble_up()

    def delete(self):
        if self.length == 0:
            return None
        item = self.arr[0]
        self.arr[0] = self.arr[self.length - 1]
        self.length -= 1
        self._bubble_down()
        return item

    # would be better a classmethod cuz we save mem cuz all the instances
    # would have the same impl, but for convenience we use an instance
    # method as we access the attr of the instance easier
    def _bubble_up(self):
        item = self.arr[self.length - 1]
        pos = self.length - 1
        parent_idx = (pos - 1)//2
        while parent_idx >= 0 and item < self.arr[parent_idx]:
            # only swap the parent, we set the item at the end
            self.arr[pos] = self.arr[parent_idx]
            pos = parent_idx
            parent_idx = (pos - 1)//2
        self.arr[pos] = item

    def _bubble_down(self):
        item = self.arr[0]
        pos = 0
        while True:
            left_child = pos*2 + 1
            right_child = pos*2 + 2
            # if we pass the length the las pos will be the last node available
            # that we removed and put it at 0
            if left_child >= self.length or right_child >= self.length:
                break
            if right_child + 1 <= self.length and self.arr[left_child] > self.arr[right_child]:
                pos_swap = right_child
            else:
                # if only has left or left is lesser than right
                pos_swap = left_child
            if pos_swap < self.length and item <= self.arr[pos_swap]:
                break
            if pos_swap >= self.length:
                pos_swap = self.length
            self.arr[pos] = self.arr[pos_swap]
            pos = pos_swap
        self.arr[pos] = item
