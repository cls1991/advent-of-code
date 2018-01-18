# coding: utf8


def memory_reallocation_v1(s):
    """Memory Reallocation."""
    cycles = 0
    banks = s[:]
    ll = len(banks)
    seen = []
    uk = ''.join(list(map(str, banks)))

    while uk not in seen:
        seen.append(uk)
        key_chosen = banks.index(max(banks))
        value_chosen = banks[key_chosen]
        banks[key_chosen] = 0

        while value_chosen > 0:
            value_chosen -= 1
            key_chosen += 1
            if key_chosen >= ll:
                key_chosen = 0
            banks[key_chosen] += 1

        uk = ''.join(list(map(str, banks)))
        cycles += 1

    return cycles


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        test = list(map(int, f.read().strip().split('\t')))

    print('Solution of Day 6 Part One: {0}'.format(memory_reallocation_v1(test)))

