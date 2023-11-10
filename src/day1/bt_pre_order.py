from src.globals_d import BinaryNode


def walk(curr: BinaryNode[int] | None, path: list[int]) -> list[int]:
    if curr is None:
        return path

    # pre
    path.append(curr.value)
    # recurse
    walk(curr.left, path)
    walk(curr.right, path)
    # post

    return path


def bt_pre_order(head: BinaryNode[int]) -> list[int]:
    return walk(head, [])
