from typing import TypeVar, Protocol

T = TypeVar("T")


class ListProtocol(Protocol[T]):
    def append(self, item: T) -> None:
        pass

    def prepend(self, item: T) -> None:
        pass

    def remove(self, item: T) -> T | None:
        pass

    def remove_at(self, index: int) -> T | None:
        pass

    def get(self, index: int) -> T | None:
        pass

    def insert_at(self, item: T, index: int) -> None:
        pass

    @property
    def length(self) -> int:
        pass


def test_list(list_imp: ListProtocol[int]):
    list_imp.append(5)
    list_imp.append(7)
    list_imp.append(9)

    assert list_imp.get(2) == 9
    assert list_imp.remove_at(1) == 7
    assert list_imp.length == 2

    list_imp.append(11)
    assert list_imp.remove_at(1) == 9
    assert list_imp.remove(9) is None
    assert list_imp.remove_at(0) == 5
    assert list_imp.remove_at(0) == 11
    assert list_imp.length == 0

    list_imp.prepend(5)
    list_imp.prepend(7)
    list_imp.prepend(9)

    assert list_imp.get(2) == 5
    assert list_imp.get(0) == 9
    assert list_imp.remove(9) == 9
    assert list_imp.length == 2
    assert list_imp.get(0) == 7
    list_imp.insert_at(10, 1)
    assert list_imp.get(1) == 10
    assert list_imp.length == 3
