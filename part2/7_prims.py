# is to build a minimum spaning tree after one tree
# greedy algo
# we use edge list, i.e. (from-node, to-node, with-weight)
# Steps:
# 1. start picking one node
# 2. add to a coll
# 3. smallest edge to unvisited nodes (the actuall min spaning tree)

# we use a min heap aka priority queue to get the time complexity to O(|E| log |E|)
# log n, cuz is the time complexity of insert and remove in the min heap

# we can get better time complexity if we use a PIQ aka priority indexed queue
# we are gona init a priority queue, except the pq is not having edges in it
# it's gona have vertices with their minimum known distance
# O(E log V), and V<=E, this cuz we at most have V nodes in the min heap and
# the update operation is O(log V)
