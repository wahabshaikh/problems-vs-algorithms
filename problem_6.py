import math

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None


    minimum = math.inf
    maximum = -math.inf

    for val in vals:
        if val < minimum:
            minimum = val

        if val > maximum:
            maximum = val

    return minimum, maximum


''' Test case 1: Array of random numbers '''
import random

l = [i for i in range(0, 10)]
random.shuffle(l)

print(get_min_max(l))
# Output: (0, 9)


''' Test case 2: Empty array '''
l = []

print(get_min_max(l))
# Output: (None, None)


''' Test case 3: Array of same numbers '''
l = [0] * 10

print(get_min_max(l))
# Output: (0, 0)


''' Test case 4: Array containing infinity as value '''
l = [math.inf, -math.inf]

print(get_min_max(l))
# Output: (-inf, inf)