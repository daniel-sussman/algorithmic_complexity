"""
Find frequency of each element in a limited range array in less than O(n) time

Given a sorted array arr[] of positive integers, the task is to find the frequency for each element in the array. Assume all elements in the array are less than some constant M

Note: Do this without traversing the complete array. i.e. expected time complexity is less than O(n)

"""

def find_frequency(arr, min=None, max=None):
    # print(f'printing frequency pattern of {arr} - min: {min}, max: {max}') # for testing
    if len(arr) == 0:
        return {}
    
    min = min or arr[0]
    max = max or arr[-1]
    if len(arr) == 1 or min == max:
        return {min: len(arr)}
    if len(arr) == 2:
        return {min: 1, max: 1}
    
    mid_index = len(arr) // 2
    left = arr[:mid_index]
    right = arr[mid_index:]

    left_dict = find_frequency(left, min=min, max=left[-1])
    right_dict = find_frequency(right, min=arr[mid_index], max=max)
    for key in right_dict:
        if key in left_dict:
            right_dict[key] += left_dict[key]

    return {**left_dict, **right_dict}