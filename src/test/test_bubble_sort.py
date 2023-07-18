import pytest
from src.day1.bubble_sort import bubble_sort as bubble_fn


class TestBubbleSort:

    @pytest.fixture
    def foo(self):
        return [9, 3, 7, 4, 69, 420, 42]

    def test_bubble_sort(self, foo):
        assert bubble_fn(foo) == [3, 4, 7, 9, 42, 69, 420]
