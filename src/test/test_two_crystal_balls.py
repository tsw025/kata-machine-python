import random

from src.day1.two_crystal_balls import two_crystal_balls


class TestTwoCrystalBalls:
    def test_two_crystal_balls(self):
        idx = random.randint(0, 9999)
        data = [False] * 10000
        data[idx:] = [True] * (10000 - idx)

        assert two_crystal_balls(data) == idx
        assert two_crystal_balls([False] * 821) == -1
