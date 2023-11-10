from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, nex: Node | None = None, prev: Node | None = None):
        self.item = item
        self.nex = nex
        self.prev = prev


class DoublyLinkedList(Generic[T]):

    def __init__(self):
        self._length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, item: T) -> None:
        node = Node(item)
        self._length += 1

        if not (self.head and self.tail):
            self.head = node
            self.tail = node
            return

        tail = self.tail
        node.prev = tail
        self.tail.nex = node
        self.tail = node

    def prepend(self, item: T) -> None:
        node = Node(item)
        self._length += 1

        if not (self.head and self.tail):
            self.head = node
            self.tail = node
            return

        first = self.head
        node.nex = first
        self.head.prev = node
        self.head = node

    def insert_at(self, item: T, idx: int):
        if idx >= self.length:
            self.append(item)
            return
        if idx <= 0:
            self.prepend(item)
            return

        node = Node(item)
        self._length += 1
        curr = self.head
        for i in range(idx):
            curr = curr.nex

        node.nex = curr
        node.prev = curr.prev
        curr.prev = node
        node.prev.nex = node

    def remove(self, item: T) -> T | None:
        if not (self.head and self.tail):
            return

        curr = self.head
        if curr.item == item:
            self.head = curr.nex
            curr.nex.prev = None
            self._length -= 1
            return curr.item

        while curr:
            if curr.item == item:
                node = curr
                if curr and curr.prev:
                    curr.prev.nex = curr.nex
                if curr.nex:
                    curr.nex.pre = node.prev
                self._length -= 1
                return node.item
            curr = curr.nex

    def remove_at(self, index: int) -> T | None:
        if index < 0:
            return

        if index > self.length:
            return

        self._length -= 1
        curr = self.head

        if index == 0:
            self.head = curr.nex
            if self.head:
                self.head.prev = None
            return curr.item

        for i in range(0, index):
            curr = curr.nex

        node = curr
        curr.prev.nex = curr.nex
        curr.nex.prev = curr.prev

        return node.item

    def get(self, index: int) -> T | None:
        if index < 0:
            return

        if index > self.length - 1:
            return

        curr = self.head
        for i in range(0, index):
            curr = curr.nex

        return curr.item

    @property
    def length(self) -> int:
        return self._length
