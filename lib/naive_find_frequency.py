"""
Find frequency of each element in a limited range array in less than O(n) time

Given a sorted array arr[] of positive integers, the task is to find the frequency for each element in the array. Assume all elements in the array are less than some constant M

Note: The naive version will aim for O(n) complexity.

"""

def naive_find_frequency(arr):
    frequencies = {}
    for n in arr:
        if frequencies.get(n):
            frequencies[n] += 1
        else:
            frequencies[n] = 1
    return frequencies