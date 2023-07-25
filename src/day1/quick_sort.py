def partition(arr, hi, lo):
    pivot = hi

    # Index of the smaller element
    idx = lo - 1

    for j in range(lo, hi):
        if arr[j] <= arr[pivot]:
            idx += 1
            arr[idx], arr[j] = arr[j], arr[idx]

    idx += 1
    arr[idx], arr[pivot] = arr[pivot], arr[idx]
    return idx


def qs(arr, hi, lo):
    if lo < hi:
        pivot = partition(arr, hi, lo)

        qs(arr, pivot - 1, lo)
        qs(arr, hi, pivot + 1)


def quick_sort(arr):
    qs(arr, len(arr) - 1, 0)
