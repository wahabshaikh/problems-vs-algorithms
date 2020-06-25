def merge_sort(input_list):
    n = len(input_list)

    if n <= 1:
        return input_list

    mid = n // 2

    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    sorted_list = []
    n_l, n_r = len(left), len(right)    
    l, r = 0, 0

    while len(sorted_list) != n_l + n_r:
        if left[l] < right[r]:
            sorted_list.append(left[l])

            if l == n_l - 1:
                sorted_list.extend(right[r:])
                r += n_r - r
            else:
                l += 1

        else:
            sorted_list.append(right[r])

            if r == n_r - 1:
                sorted_list.extend(left[l:])
                l += n_l - l
            else:
                r += 1
            
    return sorted_list



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
        
    sorted_list = merge_sort(input_list)

    maximum = ''
    for digit in sorted_list[::-2]: # O(n)
        maximum += str(digit)

    # Odd-indexed digits for min
    minimum = ''
    for digit in sorted_list[-2::-2]:
        minimum += str(digit)

    return int(maximum), int(minimum)


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





