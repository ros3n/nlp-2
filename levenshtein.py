import numpy as np


def levenshtein_distance(word_a, word_b, indicator, indicator2):
    len_a = len(word_a)
    len_b = len(word_b)

    if min(len_a, len_b) == 0:
        return max(len_a, len_b)

    distance = np.empty([len_a + 1, len_b + 1])

    for i in range(0, len_a + 1):
        distance[i][0] = i

    for j in range(0, len_b + 1):
        distance[0][j] = j

    for i, a in enumerate(word_a, start=1):
        for j, b in enumerate(word_b, start=1):
            ap = word_a[i - 2] if i > 1 else '*'
            bp = word_b[j - 2] if j > 1 else '#'
            distance[i][j] = min(
                distance[i - 1][j] + indicator2(a, ap, b, bp),
                distance[i][j - 1] + indicator2(a, ap, b, bp),
                distance[i - 1][j - 1] + indicator(a, ap, b, bp)
            )

    return distance[len_a][len_b]
