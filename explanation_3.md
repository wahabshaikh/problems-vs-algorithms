# Problem 3: Rearrange Array Elements

## Time Complexity: O(nlogn)
## Space Complexity: O(n)

### Here, n is the number of elements in the `input_list`

I have used `heapq` module to implement a `min-heap`. `heappush()` and `heappop()` functions take logarithmic time (`O(logn)`).

I iterate over the `input_list` in linear time, and push each element in the `min_heap` in logarithmic time. The whole operation takes `O(nlogn)`.

I declare a `sorted_list` to store the elements in ascending order. I repeatedly pop out the smallest element from the `min_heap` until it is empty, and append it to the `sorted_list` in constant time.  The whole operation takes `O(nlogn)`.

I iterate over the `sorted_list` backwards, and concatenate the digits at even indices to get the `max`, and at odd indices to get the `min`. I then typecast them back to `int` and return them.

Hence, overall time complexity is `O(logn)`.

The `input_list` contains `n` elements. Hence, space complexity is `O(n)`.