from src.day1.bt_post_order import bt_post_order
from .tree import tree


def test_post_order():
    result = bt_post_order(tree)
    expected_result = [
        7,
        5,
        15,
        10,
        29,
        45,
        30,
        100,
        50,
        20,
    ]
    assert result == expected_result
