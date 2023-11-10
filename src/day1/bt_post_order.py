from src.globals_d import BinaryNode


def walk(curr: BinaryNode[int] | None, path: list[int]) -> list[int]:
    if curr is None:
        return path

    # recurse
    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.value)

    return path


def bt_post_order(head: BinaryNode[int]) -> list[int]:
    return walk(head, [])
