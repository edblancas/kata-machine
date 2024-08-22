from math import floor

def binary_search(arr, needle) -> bool:
    if len(arr) == 0:
        return False

    hi = len(arr)
    lo = 0

    while lo < hi:
        m = floor(lo + (hi - lo)/2)
        v = arr[m]

        if v > needle:
            hi = m
        elif v < needle:
            lo = m + 1
        else:
            return True

    return False

