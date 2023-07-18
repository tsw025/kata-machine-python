from typing import TypeVar, Generic

T = TypeVar('T')


class StackNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.prev: StackNode[T] = None


class Stack:
    _length = 0

    def __init__(self):
        self.head = None

    def push(self, item):
        node = StackNode(item)
        self._length += 1
        if not self.head:
            self.head = node
            return

        node.prev = self.head
        self.head = node

    def pop(self):
        if not self.head:
            return None

        self._length -= 1
        head = self.head
        self.head = self.head.prev
        data = head.data
        del head
        return data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length
