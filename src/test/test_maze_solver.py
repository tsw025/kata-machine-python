import pytest
from src.day1.maze_solver import maze_solver
from src.globals_d import Point


def test_maze_solver():
    maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]

    maze_result = [
        Point(10, 0),
        Point(10, 1),
        Point(10, 2),
        Point(10, 3),
        Point(10, 4),
        Point(9, 4),
        Point(8, 4),
        Point(7, 4),
        Point(6, 4),
        Point(5, 4),
        Point(4, 4),
        Point(3, 4),
        Point(2, 4),
        Point(1, 4),
        Point(1, 5),
    ]

    # There is only one path through
    result = maze_solver(maze, "x", (10, 0), (1, 5))
    print (result)
    assert draw_path(maze, result) == draw_path(maze, maze_result)


def draw_path(data, path):
    data2 = [list(row) for row in data]
    for p in path:
        if 0 <= p.y < len(data2) and 0 <= p.x < len(data2[p.y]):
            data2[p.y][p.x] = '*'
    return [''.join(d) for d in data2]