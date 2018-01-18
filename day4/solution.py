# coding: utf8


def high_entropy_passphrases_v1(s):
    """Check whether a sequece is a valid passphrase."""
    mmap = {}
    for word in s.split(' '):
        if word not in mmap:
            mmap[word] = 0
        mmap[word] += 1
        if mmap[word] > 1:
            return False

    return True


def high_entropy_passphrases_v2(s):
    """Check whether a sequece is a valid passphrase."""
    mmap = {}
    for word in s.split(' '):
        m = {}
        for letter in word:
            if letter not in m:
                m[letter] = 0
            m[letter] += 1
        k = hash(tuple(sorted(m.iteritems())))
        if k not in mmap:
            mmap[k] = 0
        mmap[k] += 1
        if mmap[k] > 1:
            return False

    return True


if __name__ == '__main__':
    total_v1 = total_v2 = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if high_entropy_passphrases_v1(line.strip()):
                total_v1 += 1
            if high_entropy_passphrases_v2(line.strip()):
                total_v2 += 1

    print('Solution of Day 4 Part One: {0}'.format(total_v1))
    print('Solution of Day 4 Part Two: {0}'.format(total_v2))

