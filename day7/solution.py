# coding: utf8

import re

PATTERN = re.compile(r'(?P<program>[a-z]+) \((?P<weight>\d+)\)( -> )?(?P<children>[a-z, ]+)?')


def recursive_circus_v1(circuits):
    """Recursive Circus."""
    programs = {}
    for name in circuits.keys():
        programs[name] = 0
    for circuit in circuits.values():
        if 'children' in circuit:
            for child in circuit['children']:
                programs[child] += 1

    for name, count in programs.items():
        if count == 0:
            return name

    raise ValueError('No bottom program found!')


def recursive_circus_v2(circuits):
    """Recursive Circus."""

    def calc_weight(program):
        weight = circuits[program]['weight']
        if 'children' in circuits[program]:
            for child in circuits[program]['children']:
                weight += calc_weight(child)

        return weight

    def check_balance(program):
        weights = {}
        if 'children' in circuits[program]:
            for child in circuits[program]['children']:
                check_balance(child)
                weight = calc_weight(child)
                if weight not in weights:
                    weights[weight] = []
                weights[weight].append(child)

            if len(set(weights.keys())) > 1:
                unbalanced_weight = normal_weight = 0
                for weight, programs in weights.items():
                    if len(programs) == 1:
                        unbalanced_weight = weight
                    else:
                        normal_weight = weight

                unbalanced_program = weights[unbalanced_weight][0]
                balance_weight = circuits[unbalanced_program]['weight'] + normal_weight - unbalanced_weight
                circuits[unbalanced_program]['weight'] = balance_weight
                print('Solution of Day 7 Part Two: {0}'.format(balance_weight))

    bottom_program = recursive_circus_v1(circuits)
    check_balance(bottom_program)


if __name__ == '__main__':
    circuits = {}
    with open('input.txt', 'r') as f:
        for m in re.finditer(PATTERN, f.read().strip()):
            name = m.group('program')
            weight = m.group('weight')
            children = m.group('children')
            circuits[name] = {'weight': int(weight)}
            if children:
                circuits[name]['children'] = children.split(', ')

    print('Solution of Day 7 Part One: {0}'.format(recursive_circus_v1(circuits)))
    recursive_circus_v2(circuits)

