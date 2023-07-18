import pytest
from src.day1.stack import Stack


class TestStack:

    @pytest.fixture
    def stack(self):
        return Stack()

    def test_stack(self, stack):
        stack.push(5)
        stack.push(7)
        stack.push(9)

        assert stack.pop() == 9
        assert len(stack) == 2

        stack.push(11)
        assert stack.pop() == 11
        assert stack.pop() == 7
        assert stack.peek() == 5
        assert stack.pop() == 5
        assert stack.pop() is None

        # Just wanted to make sure that I couldn't blow up myself when I remove everything
        stack.push(69)
        assert stack.peek() == 69
        assert len(stack) == 1
