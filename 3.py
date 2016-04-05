#! -*- coding: utf-8 -*-

from levenshtein import *


if __name__ == '__main__':
    dictionary = None
    with open('formy.txt', encoding="iso-8859-2") as f:
        dictionary = f.readlines()

    dictionary = list(map(lambda x: x.strip(), dictionary))

    while True:
        word_a = input('word> ')
        suggestion_dist = len(word_a)
        suggestion = ''
        for word in dictionary:
            dist = levenshtein_distance(
                word_a, word,
                lambda x, xp, y, yp: 0 if x == y else 1,
                lambda x, xp, y, yp: 1,
            )
            if dist < suggestion_dist:
                suggestion = word
                suggestion_dist = dist

        if suggestion_dist < 3:
            print(suggestion, suggestion_dist)
