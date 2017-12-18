# coding: utf8


def inverse_captcha_v1(data):
    """Part One"""
    s_sum = 0
    ll = len(data)
    for i in xrange(0, ll):
        if data[i] == data[(i + 1) % ll]:
            s_sum += int(data[i])

    return s_sum


def inverse_captcha_v2(data):
    """Part Two"""
    s_num = 0
    ll = len(data)
    for i in xrange(0, ll):
        if data[i] == data[(i + ll / 2) % ll]:
            s_num += int(data[i])

    return s_num


if __name__ == '__main__':
    with open('input.txt') as f:
        source = f.read()
    print('Solution of Day 1 Part One: {0}'.format(inverse_captcha_v1(source)))
    print('Solution of Day 1 Part Two: {0}'.format(inverse_captcha_v2(source)))
