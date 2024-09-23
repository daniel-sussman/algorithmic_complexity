def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result