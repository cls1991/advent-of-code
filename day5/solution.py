# coding: utf8


def maze_twisty_trampolines_v1(s):
    """A Maze of Twisty Trampolines, All Alike ---."""
    steps = 0
    cursor = 0
    maze = s[:]
    l = len(maze)

    while True:
        if cursor < 0 or cursor >= l:
            break
        instruction = maze[cursor]
        maze[cursor] += 1
        cursor += instruction
        steps += 1

    return steps


def maze_twisty_trampolines_v2(s):
    """A Maze of Twisty Trampolines, All Alike ---."""
    steps = 0
    cursor = 0
    maze = s[:]
    l = len(maze)

    while True:
        if cursor < 0 or cursor >= l:
            break
        instruction = maze[cursor]
        if instruction >= 3:
            maze[cursor] -= 1
        else:
            maze[cursor] += 1
        cursor += instruction
        steps += 1

    return steps


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        test = list(map(int, f.read().strip().split('\n')))

    print('Solution of Day 5 Part One: {0}'.format(maze_twisty_trampolines_v1(test)))
    print('Solution of Day 5 Part Two: {0}'.format(maze_twisty_trampolines_v2(test)))

