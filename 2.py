#! -*- coding: utf-8 -*-

from levenshtein import *


def indicator(a, ap, b, bp):
    diacritical_signs = [
        ('a', 'ą'), ('c', 'ć'), ('e', 'ę'), ('l', 'ł'), ('n', 'ń'), ('o', 'ó'),
        ('s', 'ś'), ('z', 'ż'), ('z', 'ź')
    ]

    orthographic_errors = [
        ('h', 'ch'), ('ż', 'rz'), ('ó', 'u')
    ]

    for pair in orthographic_errors:
        if len(pair[1]) == 2:
            if (a == pair[0] and bp + b == pair[1]) or (ap + a == pair[1] and b == pair[0]):
                return -0.5
        elif (a == pair[0] and b == pair[1]) or (a == pair[1] and b == pair[0]):
            return 0.5

    if ap + a == b + bp:
        return 0.5

    if a == b:
        return 0

    for pair in diacritical_signs:
        if (a == pair[0] and b == pair[1]) or (a == pair[1] and b == pair[0]):
            return 0.5

    if (a == pair[0] and b == pair[1]) or (a == pair[1] and b == pair[0]):
        return 0.5

    return 1


def ort_indicator(a, ap, b, bp):
    orthographic_errors = [
        ('h', 'ch'), ('ż', 'rz')
    ]
    for pair in orthographic_errors:
        if (a == pair[0] and bp + b == pair[1]) or (ap + a == pair[1] and b == pair[0]):
            return -0.5

    if ap + a == b + bp:
        return -0.5

    return 1


if __name__ == '__main__':
    while True:
        word_a = input('first word> ')
        word_b = input('second word> ')
        print(levenshtein_distance(
            word_a, word_b, indicator, ort_indicator
        ))
