# -*- coding: utf-8 -*-


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    numbers = []
    for k in range(n):
        if k % 3 == 1:
            numbers.append(k**2)
    return numbers


if __name__ == '__main__':
    num = 7
    if squares_by_comp(num) != squares_by_loop(num):  # Skal jeg fylle inn n her?
        print('ERROR')
