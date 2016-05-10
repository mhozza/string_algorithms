def preprocess(pattern):
    p = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = p[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = p[j - 1]
        if pattern[i] == pattern[j]:
            p[i] = j + 1
    return p


def find(pattern, text):
    p = preprocess(pattern)
    results = []
    j = 0
    for i, c in enumerate(text):
        while j > 0 and c != pattern[j]:
            j = p[j - 1]
        if c == pattern[j]:
            if j == len(pattern) - 1:
                results.append(i - j)
                j = p[j - 1]
            else:
                j += 1
    return results
