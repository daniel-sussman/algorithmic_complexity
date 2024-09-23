

def binary_search(sorted_list, item, low=0, high=None):
    high = high or len(sorted_list) - 1
    if high == low:
        return low
    else:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        binary_search(sorted_list, item, low, high)