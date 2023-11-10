from src.globals_d import BinaryNode


def walk(curr: BinaryNode[int] | None, path: list[int]) -> list[int]:
    if curr is None:
        return path

    # recurse
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)

    return path


def bt_in_order(head: BinaryNode[int]) -> list[int]:
    return walk(head, [])
