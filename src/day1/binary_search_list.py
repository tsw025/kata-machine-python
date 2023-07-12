def binary_search_list(haystack: list[int], needle: int) -> bool:
    """Return True if needle is in haystack."""
    mid = len(haystack) // 2
    if not haystack:
        return False

    if haystack[mid] == needle:
        return True
    elif needle < haystack[mid]:
        return binary_search_list(haystack[:mid], needle)
    elif needle > haystack[mid]:
        return binary_search_list(haystack[mid + 1:], needle)

    return False
