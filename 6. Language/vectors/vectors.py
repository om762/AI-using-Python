from scipy.spatial.distance import cosine

import math
import numpy as np

with open("words.txt", encoding="utf-8") as f:
    words = dict()
    for line in f:
        row = line.split()
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        words[word] = vector


def distance(word1, word2):
    w1 = words[word1]
    w2 = words[word2]
    return cosine(w1, w2)


def closest_words(embedding):
    distances = {
        w: distance(embedding, words[w])
        for w in words
    }
    return sorted(distances, key=lambda w: distances[w])[:10]


def closest_word(embedding):
    return closest_words(embedding)[0]

