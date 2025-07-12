def multiplication(n):
    result = []
    for i in range(1, n+1):
        for s in range(1, 6):
            if i == s-1:
                break
            else:
                result.append(f"{i} * {s} = {i * s}")
    return result