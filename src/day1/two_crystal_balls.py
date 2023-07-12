import math


def two_crystal_balls(breaks: list[bool]) -> int:
    # Given two crystal balls that will break if dropped from high enough
    # distance, determine the exact spot in which it will break in the most
    # optimized way
    """
    solution:
        given bool [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
        the fastest to get the 1 and return index.

    time-complexity:
        if we traverse linear - O(N)
        if we do binary-search O(logN) + O(N)

    seems like they are both expensive, not seems like it is!!
    so what can we do:
        instead of breaking the array into half, we can jump
        on the array in some number (small) value, and then if the ball breaks.
        travel from last point of the jump to the intial break.

        eg: jump sqrt(N) times. O (sqrt(N))
    """
    jump = math.floor(math.sqrt(len(breaks)))

    i = jump
    for x in range(len(breaks)):
        if i > len(breaks):
            return -1
        if breaks[i]:
            break
        i += jump

    i -= jump
    for x in range(jump):
        if i > len(breaks):
            return -1
        if breaks[i]:
            return i
        i += 1

    return -1
