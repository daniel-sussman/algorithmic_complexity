def fibonacci(n):
    if n < 2:
        return [0] * n

    result = [0, 1] + ([None] * (n - 2))
    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2]
    return result
