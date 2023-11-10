from src.day1.bt_in_order import bt_in_order
from .tree import tree


def test_in_order():
    result = bt_in_order(tree)
    expected_result = [
        5,
        7,
        10,
        15,
        20,
        29,
        30,
        45,
        50,
        100,
    ]
    assert result == expected_result
