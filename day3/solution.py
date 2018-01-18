# coding: utf8

from math import (
    ceil, sqrt
)

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

NEIGHBORS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def spiral_memory_v1(n):
    """Fill up spiral array."""
    radius = int(ceil(sqrt(float(n))))
    spiral_array = [[-1 for _ in range(radius)] for _ in range(radius)]
    if radius % 2 == 0:
        sx = radius / 2
        sy = radius / 2 - 1
    else:
        sx = sy = radius / 2
    tx, ty = sx, sy
    cursor = 1
    direction = 3
    while True:
        if spiral_array[tx][ty] == -1:
            spiral_array[tx][ty] = cursor
            cursor += 1
            if cursor > n:
                break
        if direction == 0 and spiral_array[tx - 1][ty] == -1:
            direction = 1
        elif direction == 1 and spiral_array[tx][ty - 1] == -1:
            direction = 2
        elif direction == 2 and spiral_array[tx + 1][ty] == -1:
            direction = 3
        elif direction == 3 and spiral_array[tx][ty + 1] == -1:
            direction = 0

        dx, dy = DIRECTIONS[direction]
        tx, ty = tx + dx, ty + dy

    return abs(tx - sx) + abs(ty - sy)


def spiral_memory_v2(n):
    """Construct spiral array iteratively."""
    spiral = {}
    spiral[(0, 0)] = 1
    sx, sy = 0, 0
    direction = 0
    step = 0
    steps_spiral = 1
    next_spiral = False

    while True:
        dx, dy = DIRECTIONS[direction]
        sx, sy = sx + dx, sy + dy
        total = 0
        for neighbor in NEIGHBORS:
            tx, ty = sx + neighbor[0], sy + neighbor[1]
            if (tx, ty) in spiral:
                total += spiral[(tx, ty)]

        if total > n:
            return total
        spiral[(sx, sy)] = total
        step += 1
        if step == steps_spiral:
            direction = (direction + 1) % 4
            step = 0
            if next_spiral:
                steps_spiral += 1
            next_spiral = not next_spiral


if __name__ == '__main__':
    test = 368078
    print('Solution of Day 3 Part One: {0}'.format(spiral_memory_v1(test)))
    print('Solution of Day 3 Part Two: {0}'.format(spiral_memory_v2(test)))

