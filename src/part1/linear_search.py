def linear_search(haystack: list[int], needle: int) -> bool:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return True

    return False
