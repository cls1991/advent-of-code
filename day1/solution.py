# coding: utf8


def inverse_captcha_v1(data):
    """Inverse Captcha."""
    total = 0
    ll = len(data)
    for i in range(0, ll):
        if data[i] == data[(i + 1) % ll]:
            total += int(data[i])

    return total


def inverse_captcha_v2(data):
    """Inverse Captcha."""
    total = 0
    ll = len(data)
    for i in range(0, ll):
        if data[i] == data[(i + ll / 2) % ll]:
            total += int(data[i])

    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        test = f.read()
    print('Solution of Day 1 Part One: {0}'.format(inverse_captcha_v1(test)))
    print('Solution of Day 1 Part Two: {0}'.format(inverse_captcha_v2(test)))

