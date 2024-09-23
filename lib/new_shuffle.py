import random

def new_shuffle(list):
    indices = set()
    while len(indices) < len(list):
        indices.add(random.randint(0, len(list) - 1))
    return [list[i] for i in indices]