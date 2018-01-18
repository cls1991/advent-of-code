# coding: utf8


def high_entropy_passphrases(s):
    """Check whether a sequece is a valid passphrase."""
    mmap = {}
    for word in s.split(' '):
        if word not in mmap:
            mmap[word] = 0
        mmap[word] += 1
        if mmap[word] > 1:
            return False

    return True


if __name__ == '__main__':
    total = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if high_entropy_passphrases(line.strip()):
                total += 1

    print('Solution of Day 4 Part One: {0}'.format(total))


