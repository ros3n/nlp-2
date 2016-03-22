#! -*- coding: utf-8 -*-

from levenshtein import *


if __name__ == '__main__':
    while True:
        word_a = input('first word> ')
        word_b = input('second word> ')
        print(levenshtein_distance(
            word_a, word_b, lambda x, y: 0 if x == y else 1
        ))
