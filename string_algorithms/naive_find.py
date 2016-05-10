def find(pattern, text):
    results = []
    for i in range(len(text) - len(pattern)):
        found = True
        for j, p in enumerate(pattern):
            if text[i + j] != p:
                found = False
                break
        if found:
            results.append(i)
    return results
