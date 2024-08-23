def bubble_sort(arr: list[int]) -> None:
    bubble_sort_prime(arr)

def bubble_sort_prime(arr: list[int]) -> None:
    # here doesn't matter if the range is too large, cuz the next
    # for only enter at most when range(0, 1), i.e. when the second
    # argument is <= 0 it doesn't enter the for
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

def bubble_sort_me(arr: list[int]) -> None:
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

