def mergesort(arr: list[int]) -> None:
    return mergesort_rec(arr)

def mergesort_rec(arr):
    def ms(lo, hi):
        if lo == hi:
            return [arr[lo]]
        mid = (lo + hi) // 2
        left = ms(lo, mid)
        right = ms(mid + 1, hi)
        out = merge(left, right)
        return out

    def merge(left, right):
        sorted_list = []
        l, r = 0, 0
        while l != len(left) or r != len(right):
            if l == len(left):
                sorted_list.append(right[r])
                r += 1
            elif r == len(right):
                sorted_list.append(left[l])
                l += 1
            elif left[l] < right[r]:
                sorted_list.append(left[l])
                l += 1
            else:
                sorted_list.append(right[r])
                r += 1
        return sorted_list

    if len(arr) == 0:
        return []
    return ms(0, len(arr) - 1)

# to complicated
def mergesort_iter(arr):
    pass
