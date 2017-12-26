# coding: utf8


def corruption_checksum_v1(data):
    """Part One"""
    ma, mi = 0, 100000
    ep = [int(a) for a in data.split('\t')]
    for n in ep:
        if n < mi:
            mi = n
        if n > ma:
            ma = n

    return ma - mi


def corruption_checksum_v2(data):
    """Part Two"""
    ep = [int(a) for a in data.split('\t')]
    lg = len(ep)
    sa = 0
    for i in xrange(lg):
        for j in xrange(i + 1, lg):
            if ep[i] * ep[j] == 0:
                continue
            if ep[i] >= ep[j] and ep[i] % ep[j] == 0:
                sa += ep[i] / ep[j]
            elif ep[i] < ep[j] and ep[j] % ep[i] == 0:
                sa += ep[j] / ep[i]

    return sa


if __name__ == '__main__':
    s1 = 0
    s2 = 0
    with open('input.txt', 'r') as f:
        for l in f.readlines():
            s1 += corruption_checksum_v1(l)
            s2 += corruption_checksum_v2(l)

    print('Solution of Day 2 Part One: {0}'.format(s1))
    print('Solution of Day 2 Part Two: {0}'.format(s2))
