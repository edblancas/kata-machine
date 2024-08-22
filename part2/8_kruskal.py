# build a minimum spaning tree after one tree
# we use edge list, i.e. (from-node, to-node, with-weight)
# Steps:
# 1. Sort E
# O(E log E)
# you can use Union Find and Path Compression to make it more faster
# use it when you have a graph that is sparse, sorting is not that expensive
# it's pretty low, and algorithm is sorta simple
