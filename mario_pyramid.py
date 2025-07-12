def mario(m):
    result = []
    for s in range(1, m):
        result.append(' ' * (9 - s) + '*' * s)
    return result