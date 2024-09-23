def primitive_sort(list):
    zeros = []
    ones = []
    for e in list:
        zeros.append(e) if e == 0 else ones.append(e)
    return zeros + ones