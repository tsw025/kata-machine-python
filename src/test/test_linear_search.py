import pytest

from src.day1.linear_search_list import linear_search as linear_fn


class TestLinearSearch:
    @pytest.fixture
    def foo(self):
        return [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    def test_linear_search(self, foo):
        assert linear_fn(foo, 69) == True
        assert linear_fn(foo, 1336) == False
        assert linear_fn(foo, 69420) == True
        assert linear_fn(foo, 69421) == False
        assert linear_fn(foo, 1) == True
        assert linear_fn(foo, 0) == False
