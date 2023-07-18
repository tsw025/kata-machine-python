def bubble_sort(arr: list[int]) -> list[int]:
    """Sorts an array using bubble sort algorithm.

    Args:
        arr (list): Array to be sorted.

    Returns:
        list: Sorted array.
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
