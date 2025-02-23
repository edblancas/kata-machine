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

# modifies the current array and also return it
def mergesort_iter(arr):
    def merge(left, right):
        l, r = 0, 0
        sorted_list = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                sorted_list.append(left[l])
                l += 1
            else:
                sorted_list.append(right[r])
                r += 1
        sorted_list.extend(left[l:])
        sorted_list.extend(right[r:])
        return sorted_list

    width = 1
    n = len(arr)
    if n < 1: return []
    while width < n:
        for i in range(0, n, 2*width):
            left = arr[i:i+width]
            right = arr[i+width:i+2*width]
            arr[i:i+2*width] = merge(left, right)
        width *= 2
    return arr
