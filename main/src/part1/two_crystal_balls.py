# Given two crystal balls that will break if dropped form high enough distance,
# determine the exact spot in which it will break in the most optimized way.
import math

# time complexity O(sqrt(n)), n = len(breaks)
def two_crystal_balls(breaks: list[bool]) -> int:
    if breaks[0]:
        return 0

    jump = math.floor(math.sqrt(len(breaks)))

    for jump in range(jump, len(breaks), jump):
        if breaks[jump]:
            break

    jump -= jump

    for step in range(jump, len(breaks)):
        if breaks[step]:
            return step

    return -1
