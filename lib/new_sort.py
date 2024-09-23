def new_sort(list, result=[]):
    while len(result) < len(list):
        i, lowest = find_lowest(list)
        result.append(lowest)
        list = list[:i] + list[i + 1:]
    return result
    
def find_lowest(list):
    lowest = (None, float('inf'))
    for i in range(len(list)):
        if list[i] < lowest[1]:
            lowest = (i, list[i])
    return lowest

