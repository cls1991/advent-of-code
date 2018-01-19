# coding: utf8

import operator
import re

PATTERN = re.compile(r'([a-z]+) \((\d+)\)')


def recursive_circus_v1(s):
    """Recursive Circus."""
    ts = s[:]
    circus = {}
    for c in ts:
        t = c.split(' -> ')
        parent_edge = t[0].split(' ')[0]
        if parent_edge not in circus:
            circus[parent_edge] = 0
        if len(t) > 1:
            for edge in t[1].split(', '):
                if edge not in circus:
                    circus[edge] = 0
                circus[edge] += 1

    circus_sorted = sorted(circus.items(), key=operator.itemgetter(1))

    return circus_sorted[0][0]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        test = f.read().strip().split('\n')

    print('Solution of Day 7 Part One: {0}'.format(recursive_circus_v1(test)))

