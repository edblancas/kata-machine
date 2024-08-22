def binary_search(haystack: list[int], needle:int) -> bool:
    return binary_search_prime(haystack, needle)

def binary_search_me(haystack: list[int], needle:int) -> bool:
    if len(haystack) == 0:
        return False

    lo = 0
    hi = len(haystack) - 1

    while lo <= hi:
        # using integer division, e.g. math.floor(a/b)
        m = lo + (hi - lo)//2
        if haystack[m] == needle:
            return True
        elif haystack[m] > needle:
            hi = m - 1
        else:
            lo = m + 1

    return False

def binary_search_prime(haystack: list[int], needle: int) -> bool:
    if len(haystack) == 0:
        return False

    # we are using half-open intervals [from, to)
    lo = 0
    hi = len(haystack)

    while lo < hi:
        m = lo + (hi - lo)//2
        v = haystack[m]
        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1

    return False

