def capital_indexes(text: str):
    indexes = []
    i = 0
    for char in text:
        if (char.upper() == char):
            indexes.append(i)
        i += 1
    return indexes