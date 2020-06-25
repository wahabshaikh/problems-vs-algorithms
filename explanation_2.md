# Problem 2: Search in a Rotated Sorted Array

## Time Complexity: O(logn)
## Space Complexity: O(n)

### Here, n is the number of elements in the `input_list`

I have used `recursion` because the problem can be broken down into a simple, reusable sub-problem.

I store the initial `start` and `end` indices. Then, I call the `binary_search()` function with the required paramaters. The function calculates the `mid` index and if the element at that index matches with `number` (search element), I return the index. Otherwise, I recursively call the funtion on the left and right sub-arrays.

If the `start` index crosses the `end` index, I'm sure the search element does not exist in that sub-array, so I return `-1`.

Since, there are no duplicates, I'll find the answer in only one of the left and right sub-arrays, or none. If I find the search element, it's index will definitely be greater than `-1`, so I return the `max` value from either of the `left` and `right` sub-arrays. If the search element is not found, `-1` is the `max` element and that is returned.

Since, the search space is broken into half everytime, the time complexity is `O(logn)`.

The `input_list` contains `n` elements. Hence, space complexity is `O(n)`.