# coding: utf8


def corruption_checksum_v1(data):
    """Part One"""
    ma, mi = 0, 0
    ep = [int(a) for a in data.split('\t')]
    for n in ep:
        if n < mi:
            mi = n
        elif n > ma:
            ma = n

    return ma - mi


if __name__ == '__main__':
    s1 = 0
    with open('input.txt', 'r') as f:
        for l in f.readlines():
            s1 += corruption_checksum_v1(l)

    print('Solution of Day 2 Part One: {0}'.format(s1))
