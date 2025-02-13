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

# Me: This implementation doesnt clear or set to None the values in the array,
#     only decrements the length
class MinHeap():
    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, value: int):
        # wonk work with python, only js
        # self.data[0] = value
        self.data.append(value)
        self.heapify_up(self.length)
        self.length += 1


    def delete(self):
        if self.length == 0: 
            return None

        val = self.data[0]

        self.length -= 1
        # wont work with python
        # if self.length == 1:
        #     self.data = []
        #     return val

        self.data[0] = self.data[self.length]
        self.heapify_down(0)
        return val


    def parent(self, idx):
        return (idx - 1) // 2


    def left(self, idx):
        return idx * 2 + 1


    def right(self, idx):
        return idx * 2 + 2


    def heapify_up(self, idx):
        if idx == 0:
            return

        p = self.parent(idx)
        parent_value = self.data[p]
        value = self.data[idx]

        if parent_value > value:
            self.data[p], self.data[idx] = value, parent_value
            self.heapify_up(p)


    def heapify_down(self, idx):
        l_idx = self.left(idx)
        r_idx = self.right(idx)

        if idx >= self.length or l_idx >= self.length:
            return

        l_val = self.data[l_idx]
        r_val = self.data[r_idx]
        val = self.data[idx]

        if l_val < r_val and val > l_val:
            self.data[l_idx] = val
            self.data[idx] = l_val
            self.heapify_down(l_idx)
        if l_val > r_val and val > r_val:
            self.data[r_idx] = val
            self.data[idx] = r_val
            self.heapify_down(r_idx)
