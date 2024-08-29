# recursive and iterative

# in a binary tree we have n = 2^k, this give us the nodes for each level of the
# tree, e.g. k = 1, we have 2 nodes for the level 1, and so
# and the formula to get k aka levels of tree, is log base 2 of n
# so at the end we go over all the elements, n, log n times
# O(n log n) time, n = # elems in the arr, log n = levels of the tree

# TIPS:
# - Is lo <= hi, cuz:
#   1. if the left side only has 1 element then 
#      qs(lo, piv - 1), lo and piv - 1 are equals
#   2. But if the left partition has lo elements then
#      qs(lo, piv - 1), lo and piv are equal
#
# - We use idx = lo - 1, so it is simpler when we swap and when we move the pivot
#   if we don't do it then at the end the idx is at the place to swap our pivot
#   and that is more confusing
#
# - We use simple list destructure to do de swap easier
#   arr[p1], arr[p2] = arr[p2], arr[p1]
#
# - The algo from primeagen is easier than the other
#
# - If we need other pivot we swap the selected pivot to the last place, as it is
#   how this algo works
#
# - ALWAYS CHECK THE ORDER WHEN SWAPPING THINGS OUT

def quicksort(arr: list[int]) -> None:
    return quicksort_rec(arr)


def quicksort_rec(arr: list[int]) -> None:

    def qs(lo, hi):
        if hi <= lo:
            return

        piv = sort_pivot(lo, hi)
        qs(lo, piv - 1)
        qs(piv + 1, hi)

    def sort_pivot(lo, hi):
        idx = lo - 1  # to simplify
        piv_val = arr[hi]
        # sort all but the pivot, in weak order
        for i, e in enumerate(arr[lo:hi], lo):
            if e <= piv_val:
                idx += 1
                # I had these ones swapped XD
                arr[i] = arr[idx]
                arr[idx] = e
        # the pivot must be one after the barrier of the less than and greter than
        # the pivot, at this point the pivot is the last elem
        idx += 1
        # I had these ones swapped XD
        arr[hi] = arr[idx]
        arr[idx] = piv_val
        # we move the pivot and we have weak order on the right and left
        # e.g. [3, 1, 4, 10, 30, 22, 11], piv = 10

        return idx

    qs(0, len(arr) - 1)


def quicksort_iter(arr: list[int]) -> None:
    pass
