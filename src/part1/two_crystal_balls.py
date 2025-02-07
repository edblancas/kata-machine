import math

def two_crystal_balls(breaks: list[bool]) -> int:
    step = math.floor(math.sqrt(len(breaks)))

    for i in range(0, len(breaks), step):
        if breaks[i] == True:
            break

    print('first break', i)
    i -= step
    print('go back step to', i)

    for j in range(i, len(breaks)):
        if breaks[j] == True:
            print('second crystal break, first breat at', j)
            return j

    return -1
