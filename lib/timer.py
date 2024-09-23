import timeit
import importlib
import random


# The names of the .py files you want to test (without the .py)
# files = ["reverse", "shuffle", "sort"]
files = ["o_n2"]

# The input sizes you want to test
inputs = [i for i in range(5000, 100001, 5000)]

def time_algorithm(algorithm, size):
    setup = f'from {algorithm} import {algorithm};'

    test_input = list(range(1, size+1))
    random.shuffle(test_input)
    test = f'{algorithm}({test_input})'
    
    time_taken = timeit.timeit(test, setup=setup, number=100) / 100
    return time_taken

for alg in files:
    for size in inputs:
        print(time_algorithm(alg, size))
        # print(f'Algorithm: {alg}, Input size: {size}, Time: {time_algorithm(alg, size)}')
    print("-------")
