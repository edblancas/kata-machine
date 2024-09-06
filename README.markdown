# Kata Machine

This is based in the front end masters courses of algorithm prep from 
The Primeagen.

Part 1:
<https://frontendmasters.com/courses/algorithms/>

Part 2:
<https://frontendmasters.com/courses/advanced-algorithms/>

For more info see the README files of the part1 and part2 inside this repo.

The order of the files is:

```
├── part1
│   ├── 1_linear_search.py
│   ├── 2_binary_search_list.py
│   ├── 3_two_crystal_balls.py
│   ├── 4_bubble_sort.py
│   ├── 5_singly_linked_list.py
│   ├── 6_queue.py
│   ├── 7_stack.py
│   ├── 8_ring_buffer.py
│   ├── 9_recursion_sum_of_n.py
│   ├── 10_recursion_maze_solver.py
│   ├── 11_quicksort.py
│   ├── 12_mergesort.py
│   ├── 13_doubly_linked_list.py
│   ├── 14_binary_tree_pre_order.py
│   ├── 15_binary_tree_in_order.py
│   ├── 16_binary_tree_post_order.py
│   ├── 17_binary_search_tree.py
│   ├── 18_compare_binary_trees.py
│   ├── 19_dfs_on_bst.py
│   ├── 20_min_heap.py
│   ├── 21_trie.py
│   ├── 22_bfs_graph_adj_matrix.py
│   ├── 23_bfs_graph_adj_list.py
│   ├── 24_dfs_graph_adj_matrix.py
│   ├── 25_dfs_graph_adj_list.py
│   ├── 26_dijkstra_adj_list.py
│   ├── 27_lru.py
├── part2
│   ├── 1_binary_search_tree.py
│   ├── 2_bst_avl.py
│   ├── 3_bst_black_red.py
│   ├── 4_m_way_b_tree.py
│   ├── 5_bfs_nodes_hops_away.py
│   ├── 6_dfs_topological_sort.py
│   ├── 7_prims.py
│   ├── 8_kruskal.py
│   ├── 9_ford_fulkerson_max_flow.py
│   ├── 10_ford_fulkerson_min_cut.py
│   ├── 11_factorial.py
│   ├── 12_fibonacci.py
│   ├── 13_max_subarray.py
│   ├── 14_coin_change_problem.py
│   ├── 15_bloom_filter.py
```

# Tests

To run tests for a file in specific:


```
python3 -m unittest discover  -p 'test*linear*.py'
# to run all tests inside test/
python3 -m unittest
```

The above run for the `test/test_1_linear_search.py`.

With Neotest you can use `:lua require('neotest').watch.toggle()` to watch
a test file that will run each time you save the source/test file.

More info [here](https://github.com/nvim-neotest/neotest#watch-tests).

The `./test/__init__.py` is necessary for Neotest to work.

But `./test/__init__.py`, `./test/part1/__init__.py`, and `./test/part2/__init__.py` 
are necessary for the unittest runner to work, i.e. `python3 -m unittest` commands.
