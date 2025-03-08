def mergesort(arr: list[int]) -> None:
    mergesort_rec(arr)

def mergesort_rec(arr): ...

# without using a helper array to sort and modify the passed array
# but a new array sorted is returned
# i think this is easier
# from WilliamFiset video
def mergesort_rec_2(arr): ...

# modifies the current array and also return it
def mergesort_iter(arr):...
