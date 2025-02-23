def binary_search(haystack: list[int], needle: int) -> bool:
    lo, hi = 0, len(haystack) - 1

    while lo <= hi:
        m = (lo + hi) // 2
        if haystack[m] == needle:
            return True
        elif haystack[m] < needle:
            lo = m + 1
        else:
            hi = m - 1

    return False
