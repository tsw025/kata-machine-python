from src.day1.bt_pre_order import bt_pre_order
from .tree import tree


def test_pre_order():
    result = bt_pre_order(tree)
    expected_result = [20, 10, 5, 7, 15, 50, 30, 29, 45, 100]
    assert result == expected_result
