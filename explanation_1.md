# Problem 1: Square Root of an Integer

## Time Complexity: O(logn)
## Space Complexity: O(1)

I have used the `binary search` algorithm to find the square root of a given number. Since, I need to return the floor value, I store the result in a variable `res` if the result is not a perfect square root. Since, the search space is reduced by half everytime, the time complexity is `O(logn)`.

Storage is not required. Hence, space complexity is `O(1)`.