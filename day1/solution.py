# coding: utf8


def inverse_captcha(data):
    s_sum = 0
    ll = len(data)
    for i in xrange(0, ll):
        if data[i] == data[(i + 1) % ll]:
            s_sum += int(data[i])

    return s_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        source = f.read()
    print(inverse_captcha(source))
