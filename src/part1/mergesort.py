# recursive and iterative

def mergesort(arr: list[int]) -> None:
    mergesort_rec(arr)

def mergesort_rec(arr):
    helper_arr = [None] * len(arr)
    def ms(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        ms(lo, mid)
        ms(mid + 1, hi)
        merge(lo, hi, mid)

    def merge(lo, hi, mid):
        # copy range to the helper
        helper_arr[lo:hi + 1]  = arr[lo:hi + 1]

        left_helper = lo
        right_helper = mid + 1
        curr = lo

        while left_helper <= mid and right_helper <= hi:
            if helper_arr[left_helper] <= helper_arr[right_helper]:
                arr[curr] = helper_arr[left_helper]
                left_helper += 1
            else:
                arr[curr] = helper_arr[right_helper]
                right_helper += 1
            curr += 1

        # why only copy the numbers left on the left side?
        # cuz the right elements are already there, the original array
        # and if right elems are left, that means that those are greater than all
        # copied to the target array, and the left part is empty.
        if mid - left_helper + 1 > 0: 
            # if there are elems in the left side, we add 1 cuz are indices and we need no. elems
            arr[curr:hi+1] = helper_arr[left_helper:mid+1]

    ms(0, len(arr) - 1)


# to complicated
def mergesort_iter(arr):
    pass
