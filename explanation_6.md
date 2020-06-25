# Problem 1: Unsorted Integer Array

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the number of elements in the `input_list`

I initialize two variables - `min` with an infinitely large value and `max` with an infinitely small value. I do this so that the first element of the `input_list` is assigned to both `min` and `max` when the iteration begins.

Next, I iterate through the `input_list` in linear time. I compare each element with `min` and update it i(f the element is smaller. Same, with the `max` variable - update if element is larger. I do this for every element in the `input_list`. Hence, time complexity is `O(n)`.

The `input_list` contains `n` elements. Hence, space complexity is `O(n)`.