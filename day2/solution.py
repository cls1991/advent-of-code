# coding: utf8

from itertools import combinations


def corruption_checksum_v1(data):
    """Corruption Checksum."""
    array = list(map(int, data.split('\t')))
    return max(array) - min(array)


def corruption_checksum_v2(data):
    """Corruption Checksum."""
    sa = 0
    for a, b in combinations(list(map(int, data.split('\t'))), 2):
        if a % b == 0:
            sa += a / b
        elif b % a == 0:
            sa += b / a

    return sa


if __name__ == '__main__':
    total_v1 = total_v2 = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            total_v1 += corruption_checksum_v1(line.strip())
            total_v2 += corruption_checksum_v2(line.strip())

    print('Solution of Day 2 Part One: {0}'.format(total_v1))
    print('Solution of Day 2 Part Two: {0}'.format(total_v2))

