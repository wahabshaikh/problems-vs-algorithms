# Problem 4: Dutch National Flag Problem

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the number of elements in the `input_list`

I declare two variables - `i_0` to keep 0s at the beginning of the list and `i_2` to keep 2s at the end of the list. 

I construct a `while` loop that runs till the list is sorted. If I encounter 0, I send it to the beginning of the list because `i_0` is 0. I then increment `i_0`, so the next 0 I encounter will take that place. If I encounter 2, I send it to the end of the list because `i_2` is the last index. I then decrement `i_2`, so the next 2 I encounter will take that place. Otherwise, the element is 1 and I just move to the next index. This way 0s are stacked at the beginning and 2s are stacked at the end automatically stacking the 1s in the middle. 

Since every element is visited once, the time complexity is linear (`O(n)`).

The `input_list` contains `n` elements. Hence, space complexity is `O(n)`.