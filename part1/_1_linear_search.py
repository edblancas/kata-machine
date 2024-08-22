def linear_search(haystack: list[int], needle: int) -> bool:
    for e in haystack:
        if e == needle:
            return True
    return False

