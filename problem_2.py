def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list) - 1

    def binary_search(input_list, start, end, number):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid

        left = binary_search(input_list, start, mid - 1, number)
        right = binary_search(input_list, mid + 1, end, number)
        
        return max(left, right)

    return binary_search(input_list, start, end, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass", rotated_array_search(input_list, number))
    else:
        print("Fail", rotated_array_search(input_list, number))

''' Test case 1: Random values '''
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Output:
# Pass 0
# Pass 5
# Pass 2
# Pass 3
# Pass -1


''' Test case 2: Empty list '''
test_function([[], -1])
# Output:
# Pass -1


''' Test case 3: Rotated on first element '''
test_function([[1, 2, 3, 4, 0], 0])
# Output:
# Pass 4


''' Test case 4: Only one element '''
test_function([[1], 1])
# Output:
# Pass 0

