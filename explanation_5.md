# Problem 5: Autocomplete with Tries

## Time Complexity: O(m * n)
## Space Complexity: O(n)

### Here, m is the length of the word and n is the total number of words

I have used the `Trie` data structure to implement the autocomplete feature. The `insert` and `search` operations take `O(m*n)` time for a word of length `m` in a `trie` where total number of words are `n`.

Space Complexity is `O(n)` because in the worst case scenario, all the letters of the word are unique. Hence, we have to make `n` nodes.