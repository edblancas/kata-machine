# Given two crystal balls that will break if dropped form high enough distance,
# determine the exact spot in which it will break in the most optimized way.

import math

def two_crystal_balls(breaks: list[bool]) -> int:
    step = math.floor(math.sqrt(len(breaks)))
    for n in range(0, len(breaks), step):
        if breaks[n]:
            break

    n -= step
    for n in range(n, len(breaks)):
        if breaks[n]:
            return n

    return -1

