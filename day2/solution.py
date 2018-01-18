# coding: utf8

from itertools import combinations


def corruption_checksum_v1(data):
    """Corruption Checksum."""
    ma, mi = 0, 10000000
    for num in data.split('\t'):
        t = int(num)
        if t > ma:
            ma = t
        if t < mi:
            mi = t

    return ma - mi


def corruption_checksum_v2(data):
    """Corruption Checksum."""
    sa = 0
    for a, b in combinations(data.split('\t'), 2):
        ta, tb = int(a), int(b)
        if ta % tb == 0:
            sa += ta / tb
        elif tb % ta == 0:
            sa += tb / ta

    return sa


if __name__ == '__main__':
    total_v1 = total_v2 = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            total_v1 += corruption_checksum_v1(line.strip())
            total_v2 += corruption_checksum_v2(line.strip())

    print('Solution of Day 2 Part One: {0}'.format(total_v1))
    print('Solution of Day 2 Part Two: {0}'.format(total_v2))

