10:25
Big O Time Complexity
TLDR; 1. growth is with respect to the input 2. constants are dropped 3. worst case is usually the way we measure

01:01
Arrays Data Structure
Some languages are not exactly an array, e.g. js sure do some things that optimize a list [], e.g. when you put an element at a 1mil position, maybe they convert it to a map, etc.

06:26
Arrays Data Structure
when he refer to an array is like, in node, an array buffer is aa contiguous piece of memory: const a = new ArrayBuffer(6) and a view to that buffer as a 1byte integer: const a8 = new Uint8Array(s) and put an 8bit int a8[0] = 45

06:34
Arrays Data Structure
when he refers to a list is not quite that

07:35
Binary Search Algorithm
log2(N) = K K is the times we have to halve the array to get to find the value (or if not exitst)

08:11
Binary Search Algorithm
If you scan the input of the halves, like the merge sort is N*log2(N)

01:35
Pseudo Code Binary Search
IMPORTANT!! Almost alway I calculated the middle with the length of the array, like m = array.length/2.

But this way of calculate the middle is better because we are thinking in terms of indices of the array.

05:27
Pseudo Code Binary Search
Our hi pointer is like a stop pointer that tell us not to cross that line, we don't want to look in there.

00:54
Bubble Sort
Fun Story about code simplicity of bubble sort

05:33
Bubble Sort
Fun Story about bubble sort complexity time

14:22
Linked List Data Structures
deletion and insertion is O(1), get to the element to do that is O(n) actually indexing

02:50
RingBuffer
most langs dont convert from intergers to floats, they have to have your permision. Thats why in python 5/2 = 2 reminder 1. and 5%2 = 1

03:32
RingBuffer
we can technically extend the case, as long as we know the sums. i.e. as long as we know the result of the case, fn call for the args in question

06:23
RingBuffer
Object pool

07:08
Data Structures Q&A
const a = [] in javascript is not an array, is an array list. Cuz have operation for growth, push and pop at the end, it keeps track of a bunch of things. So is an array list aka dynamic array,

12:40
Data Structures Q&A
You step more into DS in the backend, and in the frontend when you are developing libraries.

14:41
Data Structures Q&A
Big data is like the core concepts but more complicated and doing that distributely.

14:41
Data Structures Q&A
You can extend your base case as long as you know, for example in this case the sum of other numbers. We can use a base case of for example if n == 3: return 5

11:37
Recursion
for each call we have: return address, return value, and the argument.

11:37
Recursion
recursion breaks down into 2 things: base case and the recursion call.

11:37
Recursion
the recursion call has:

pre: for doing things before the recursion, in this example is only n +
recurse
post: like doing log
01:58
QuickSort Algorithm
Stock problem always ask by companies

09:58
QuickSort Algorithm
for each level of the tree we need to scan all the array again, and we do this log n that's the formula n/(2^k) = 1. So we do a log n amount of n's. So the running time is O(n log n).

10:43
QuickSort Algorithm
quicksort not always runs quick, when choosing the last elem as the pivot, when we have an array in reverse order, meaning in desc order, then quicksort runs in O(n^2)

12:03
QuickSort Algorithm
so there are some strategies ike choose the middle elem or random one, but at the end you will be in the range of nlogn and n^2 running time, but more often in the best case.

so, in comparison with the mergesort, that always is O(nlogn) but with space O(n), this is not space efficient.

so there you have some tradeoffs of the algo, but quicksort is more optimum so is more used.

09:12
Linked List: prepend, insertAt, & append
BUG: This should be curr.prev.next = node; Using curr.prev.next = curr; would be linking the previous node to curr, which would break the doubly linked structure.

09:21
Linked List: remove, get, & removeAt
BUG: There are a couple of bugs here that Prime fixes in the Debugging Linked Lists lesson

12:54
Linked List: remove, get, & removeAt
BUG: Line 54 should be node.prev.next = node

08:16
Tree Traversals
For general tree, you can do pre-order or post-order traversal. But is more difficult to do in-order, cuz how you know where is the middle, as with binary tree is evident that is right, visit the node, and then left.
Visit the node is depending what you are doing, in this case where are only printing the value.

00:49
Implement Tree Traversal
Good tip is alway create a second function whenever we are doing recursion.

01:29
Implement Tree Traversal
The call-stack keep the order for us in the traversal of a tree.

12:00
Implement Tree Traversal
This types of traversals are called deep first search. As we go deep until we can't. Here we use a stack for visiting the nodes, the callstack.
We also have breath first search, and we use a queue for the order of visiting the nodes.

13:33
Implement Tree Traversal
Here we see visually how we use a stack for visiting the nodes.

05:50
Breadth-First Search
Each level of a binary tree is aprox half the size of the tree above it.
e.g. level 3 has 8 nodes, and the sum of the levels 0-2 is 7.
So it has nodes at the level - 1

06:19
Breadth-First Search
So use a properly queue when doing BFS, or else we are going to have terrible running times.
e.g. if we use an [] and shift and unshift in javascript, as for each element we shift or unshift we need to move all the elements.
So al the end using the array list in javascript it will add O(n^2) to our running time complexity.

06:09
Implement Breadth-First Search
What's easier?

DFS, cuz recursive seems more simple, but comes with a cost cuz each recursive call we at minimum have to have return address, parameters passed to the function, return values.
Iterative BFS is a bit messier.
02:32
Search Practice
Check if two trees have the same values and the same structure:

We need to use deep first search, cuz this traversal preserve structure.
BFS do not preserve structure.
08:42
Depth-First: Find
Binary search trees aka BST are great for quiick finding when we need to add things and still have some great time complexity for search. But the traversal comes with a cost and tree sometimes get out of sync.

Cuz imagine if we already have a array list, then imagine if we have to add or remove, we have a running time of n.

00:54
Depth-First: Insert
Big O for find in a BST is O(h) being h the height of the tree. Where can be between log n and n. For example, in a skewed BST is going to b n and in a complete BST is going to be log n.
The range is on how well balanced is our BST.

06:22
Depth-First: Delete
To delete we have 3 cases:

case 1: no child; so we just delete
case 2: one chid; so se set parent to child of the node to delete
case 3: two children; we have 2 options: get the smallest node on the larger side (right side) or get the largest on the smallest side (left side) and replace it with the node to delete. If we have the height of the sub-tree at any node, we should select the option with the higher height so the whole tree should be more balanced and therefore we have better time to search.
00:35
Binary Search Tree Q&A
After insertion by definition the tree is most be unbalanced, here is where the algo AVL and red-black come into play to balance again the tree.

01:24
Binary Search Tree Q&A
And here we have trade-offs, i.e. if I don't find that often but insert a lot then red black; but if I find a lot and rarely insert then AVL might be better.

03:43
Binary Search Tree Q&A
in order traversal of a BST print in order the values. So the BST is more a strong ordering than a weak ordering (like the quick-sort).

03:19
Implement Depth-First Search
we are reducing our search space by half every single step by only checking once; either right or left. That's why we have the return in both options where we go right or left.

04:36
Implement Depth-First Search
Now we compare Binary search on an array that is a little more complicated cuz hi and lo, but it's always O(log n). But binary search on a tree is easier but our low and hi are predetermined for us so the running time is in the range of O(log n) to O(height).

02:53
Heap
Heaps maintain a weak order.

03:18
Heap
min max heap aka priority queue

03:36
Heap
heaps are full or complete trees, meaning that is always adding from left to right, and it never has any empty spaces.

05:07
Heap
when we insert we insert at the next node available from left to right and bubble up while maintaining the condition for a min/max heap, e.g. for a min heap, is my parent greater than me, yes we swap it, if not or if we are at the root then we finished.

06:21
Heap
When we get the root, we delete it effectively so we put the last node at the root and heapify down. e.g. for a min heap, get the minimum of the two children and compare against that; so is our node greater that the smallest of the children, if yes then we swap it and go again until we are at a leaf.

08:12
Heap
For getting the place where we need to add a node we need to traverse the tree and it's hard, so we use an array instead of a node based data structure.

09:36
Heap
we implement a heap in an arraylist cuz we need to growth it.

14:10
Heap
We use the formulas, for children of a node, left = i*2 + 1 and right = i*2 + 2, and the parent for any node parent = floor((i-1)/2).

In real programming langs XD that the division return an integer and not a float. For prog langs that return a float we use floor.

14:23
Heap
And we heapify_downd(0) and heapify_up(arr.lenght)

02:37
Implementing Heap
for update, we need to use a hashmap to keep track of the index and value of each node.

05:06
Implement DFS on Adjacency List
the base cases are part of the loop in bfs
