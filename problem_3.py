from heapq import heapify, heappush, heappop

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return None, None

    min_heap = []
    heapify(min_heap)

    for val in input_list: # O(n)
        heappush(min_heap, val) # O(logn)

    sorted_list = []
    while min_heap: # O(n)
        sorted_list.append(heappop(min_heap)) # O(logn)

    max = ''
    for digit in sorted_list[::-2]: # O(n)
        max += str(digit)

    # Odd-indexed digits for min
    min = ''
    for digit in sorted_list[-2::-2]:
        min += str(digit)

    return int(max), int(min)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    try:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    except TypeError:
        if output == solution:
            print("Pass")
        else:
            print("Fail")


''' Test case 1: Sorted lists '''
test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[5, 4, 3, 2, 1], [531, 42]])
# OUTPUT:
# (531, 42)
# Pass
# (531, 42)
# Pass

''' Test case 2: Unsorted list '''
test_function([[4, 9, 2, 5], [94, 52]])
# OUTPUT:
# (94, 52)
# Pass


''' Test case 3: Same list element '''
test_function([[0, 0, 0], [0, 0]])
test_function([[1, 1, 1], [11, 1]])
test_function([[2, 2, 2], [22, 2]])
# OUTPUT:
# (0, 0)
# Pass
# (11, 1)
# Pass
# (22, 2)
# Pass


''' Test case 3: Empty list '''
test_function([[], (None, None)])
# OUTPUT:
# (None, None)
# Pass

''' Test case 4: Single list element '''
test_function([[0], (None, None)])
test_function([[1], (None, None)])
test_function([[2], (None, None)])
# OUTPUT:
# (None, None)
# Pass
# (None, None)
# Pass
# (None, None)
# Pass





