def binary_search(haystack: list[int], needle: int) -> bool:
    hi = len(haystack) - 1
    lo = 0

    while lo <= hi:
        # m = (lo + hi) // 2
        m = lo + (hi - lo) // 2
        v = haystack[m]
        if v == needle:
            return True
        elif needle < v:
            hi = m - 1
        else:
            lo = m + 1

    return False
