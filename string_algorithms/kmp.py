def find(pattern, text):
    # Compute fail function
    p = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = p[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            p[i] = j
    # find
    results = []
    j = 0
    for i in range(0, len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = p[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                results.append(i - j)
                j = p[j - 1]
            j += 1

    return results
