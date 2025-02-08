def quicksort(arr: list[int]) -> None:
    return quicksort_iter(arr)


def quicksort_rec(arr: list[int]) -> None:
    def partition(lo, hi):
        idx = lo - 1
        piv = arr[hi]
        for i in range(lo, hi):
            if arr[i] <= piv:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]

        idx += 1
        arr[hi] = arr[idx]
        arr[idx] = piv
        return idx

    def qs(lo, hi):
        if hi <= lo:
            return
        piv = partition(lo, hi)
        qs(lo, piv - 1)
        qs(piv + 1, hi)

    qs(0, len(arr) - 1)


def quicksort_iter(arr: list[int]) -> None:
    stack = []
    def partition(lo, hi):
        idx = lo - 1
        piv = arr[hi]
        for i in range(lo, hi):
            if arr[i] <= piv:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]

        idx += 1
        arr[hi] = arr[idx]
        arr[idx] = piv
        return idx

    stack.append([0, len(arr) - 1])
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            piv = partition(lo, hi)
            stack.append([lo, piv - 1])
            stack.append([piv + 1, hi])
