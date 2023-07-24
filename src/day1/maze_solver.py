from typing import List
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def walk(maze: list, wall: str, curr: Point, end: Point, seen: List[List[bool]], path: List[Point]) -> bool:
    # Base cases
    # if current is off the map
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False

    # if it's a wall
    if maze[curr.y][curr.x] == wall:
        return False

    # if it's the end
    if curr.x == end.x and curr.y == end.y:
        path.append(curr)
        return True

    if seen[curr.y][curr.x]:
        return False

    # pre
    seen[curr.y][curr.x] = True
    path.append(curr)
    # recurse
    for i in range(0, len(directions)):
        x, y = directions[i]
        if walk(maze, wall, Point(curr.x + x, curr.y + y), end, seen, path):
            return True

    # post
    path.pop()

    return False


def maze_solver(maze, obstacle, start, end) -> list[Point]:
    seen: List[List[bool]] = []
    path: List[Point] = []
    curr = Point(start[0], start[1])
    end = Point(end[0], end[1])

    for i in range(0, len(maze)):
        seen.append([False] * len(maze[0]))

    walk(maze, wall=obstacle, curr=curr, end=end, seen=seen, path=path)

    return path
