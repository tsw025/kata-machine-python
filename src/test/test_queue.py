import pytest
from src.day1.queue import Queue


class TestQueue:

    @pytest.fixture
    def queue(self):
        return Queue()

    def test_queue(self, queue):
        queue.enqueue(5)
        queue.enqueue(7)
        queue.enqueue(9)

        assert queue.dequeue() == 5
        assert len(queue) == 2

        queue.enqueue(11)
        assert queue.dequeue() == 7
        assert queue.dequeue() == 9
        assert queue.peek() == 11
        assert queue.dequeue() == 11
        assert queue.dequeue() is None
        assert len(queue) == 0

        queue.enqueue(69)
        assert queue.peek() == 69
        assert len(queue) == 1
        assert queue.dequeue() == 69
        assert queue.dequeue() is None
        assert len(queue) == 0
