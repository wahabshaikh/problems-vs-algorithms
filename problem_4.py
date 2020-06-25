def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i_0 = 0
    i_2 = len(input_list) - 1

    i = 0
    while i <= i_2:
        if input_list[i] == 0:
            input_list[i], input_list[i_0] = input_list[i_0], input_list[i]
            i_0 += 1
            i += 1
        elif input_list[i] == 2:
            input_list[i], input_list[i_2] = input_list[i_2], input_list[i]
            i_2 -= 1
        else:
            i += 1

    return input_list
        

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


''' Test case 1: Unsorted Lists '''
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 1, 0])

# OUTPUT:
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 1, 2]
# Pass


''' Test case 2: Same element '''
test_function([0, 0, 0])
test_function([1, 1, 1])
test_function([2, 2, 2])
# OUTPUT:
# [0, 0, 0]
# Pass
# [1, 1, 1]
# Pass
# [2, 2, 2]
# Pass


''' Test case 3: Single element '''
test_function([0])
test_function([1])
test_function([2])
# OUTPUT:
# [0]
# Pass
# [1]
# Pass
# [2]
# Pass


''' Test case 4: Empty list '''
test_function([])
# OUTPUT:
# []
# Pass
