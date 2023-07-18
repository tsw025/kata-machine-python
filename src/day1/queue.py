from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional[Node[T]] = None


class Queue(Generic[T]):
    """
    Implemented a Quote with Linked List.

    Of course, this should have been done by having a Tail.
    But I just did it for fun.
    """
    _length: int = 0

    def __init__(self):
        self.head: Optional[Node[T]] = None

    def enqueue(self, item: T) -> None:
        self._length += 1
        if not self.head:
            self.head = Node(item)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(item)

    def dequeue(self) -> Optional[T]:
        if not self.head:
            return None

        head = self.head
        self.head = self.head.next
        self._length -= 1
        data = head.data
        del head
        return data

    def peek(self) -> Optional[T]:
        return self.head.data

    def __len__(self) -> int:
        return self._length
