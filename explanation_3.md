# Problem 3: Rearrange Array Elements

## Time Complexity: O(nlogn)
## Space Complexity: O(n)

### Here, n is the number of elements in the `input_list`

I use `merge sort` to sort the `input_list`. The time complexity is `O(nlogn)`.

I iterate over the `sorted_list` backwards, and concatenate the digits at even indices to get the `max`, and at odd indices to get the `min`. I then typecast them back to `int` and return them.

Hence, overall time complexity is `O(logn)`.

The `input_list` contains `n` elements. The recursive stack takes logarithmic space. Hence, overall space complexity is `O(n)`.