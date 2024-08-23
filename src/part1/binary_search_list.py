def binary_search(haystack: list[int], needle:int) -> bool:
    return binary_search_tailrec_me(haystack, needle)

def binary_search_tailrec_me(haystack: list[int], needle:int) -> bool:
    lo = 0
    hi = len(haystack) - 1
    return binary_search_railrec_aux_geek(haystack, needle, lo, hi, (hi + lo)//2)

def binary_search_railrec_aux_geek(haystack: list[int], needle:int, lo: int, hi: int, m: int) -> bool:
    if lo <=hi:
        m = (hi + lo)//2
        if haystack[m] == needle:
            return True
        elif haystack[m] > needle:
            return binary_search_railrec_aux_me(haystack, needle, lo, m - 1, m)
        else:
            return binary_search_railrec_aux_me(haystack, needle, m + 1, hi, m)
    # is the same putting the else and the return False
    # else:
    return False

def binary_search_railrec_aux_me(haystack: list[int], needle:int, lo: int, hi: int, m: int) -> bool:
    if lo > hi:
        return False
    if haystack[m] == needle:
        return True
    elif haystack[m] > needle:
        return binary_search_railrec_aux_me(haystack, needle, lo, m - 1, (hi + lo)//2)
    else:
        return binary_search_railrec_aux_me(haystack, needle, m + 1, hi, (hi + lo)//2)

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

