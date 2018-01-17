# coding: utf8

from math import (
    ceil, sqrt
)

DIRECTIONS = {
    'UP': 1,
    'RIGHT': 2,
    'DOWN': 3,
    'LEFT': 4
}


def spiral_memory_v1(n):
    """Build spiral array with square size of n."""
    radius = int(ceil(sqrt(float(n))))
    spiral_array = [[-1 for _ in range(radius)] for _ in range(radius)]
    if radius % 2 == 0:
        sx = radius / 2
        sy = radius / 2 - 1
    else:
        sx = sy = radius / 2
    tx, ty = sx, sy
    cursor = 1
    direction = DIRECTIONS['DOWN']
    while True:
        if spiral_array[tx][ty] == -1:
            spiral_array[tx][ty] = cursor
            cursor += 1
            if cursor > n:
                break
        if direction == DIRECTIONS['RIGHT']:
            if spiral_array[tx - 1][ty] == -1:
                direction = DIRECTIONS['UP']
                tx -= 1
            else:
                ty += 1
        elif direction == DIRECTIONS['UP']:
            if spiral_array[tx][ty - 1] == -1:
                direction = DIRECTIONS['LEFT']
                ty -= 1
            else:
                tx -= 1
        elif direction == DIRECTIONS['LEFT']:
            if spiral_array[tx + 1][ty] == -1:
                direction = DIRECTIONS['DOWN']
                tx += 1
            else:
                ty -= 1
        else:
            if spiral_array[tx][ty + 1] == -1:
                direction = DIRECTIONS['RIGHT']
                ty += 1
            else:
                tx += 1

    return abs(tx - sx) + abs(ty - sy)


if __name__ == '__main__':
    test = 368078
    print('Solution of Day 3 Part One: {0}'.format(spiral_memory_v1(test)))
