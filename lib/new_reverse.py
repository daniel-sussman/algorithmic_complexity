def new_reverse(list):
    l = len(list)
    new_list = [None] * l
    for i in range(l):
        new_list[l - i - 1] = list[i]
    return new_list