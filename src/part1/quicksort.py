def quicksort(arr: list[int]) -> None:
    return quicksort_iter(arr)


def quicksort_rec(arr: list[int]) -> None:
    def qs(lo, hi):
        if lo >= hi:
            return
        pivot = partition(lo, hi)
        qs(lo, pivot - 1)
        qs(pivot + 1, hi)

    def partition(lo, hi):
        pivot = arr[hi]
        idx = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                idx += 1
                arr[idx], arr[j] = arr[j], arr[idx]
        idx += 1
        arr[hi] = arr[idx]
        arr[idx] = pivot
        return idx

    qs(0, len(arr) - 1)


from collections import deque

def quicksort_iter(arr: list[int]) -> None:
    def partition(lo, hi):
        pivot = arr[hi]
        idx = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                idx += 1
                arr[j], arr[idx] = arr[idx], arr[j]
        idx += 1
        arr[hi] = arr[idx]
        arr[idx] = pivot
        return idx

    q = deque()
    q.append([0, len(arr) - 1])
    while q:
        lo, hi = q.popleft()
        if lo >= hi: continue
        pivot = partition(lo, hi)
        q.append([lo, pivot - 1])
        q.append([pivot + 1, hi])
