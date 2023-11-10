from src.day1.doubly_linked_list import DoublyLinkedList
from src.test.test_list import test_list


class TestDoublyLinkedList:
    def test_doubly_linked_list(self):
        list = DoublyLinkedList()
        test_list(list)