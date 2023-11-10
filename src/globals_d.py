from __future__ import annotations

from typing import TypeVar, Generic

from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Point:
    x: int
    y: int


class BinaryNode(Generic[T]):
    def __init__(self, value: T, left: BinaryNode | None = None, right: BinaryNode | None = None):
        self.value: T = value
        self.left: BinaryNode = left
        self.right: BinaryNode = right
