# Problem 7: Request Routing in a Web Server with a Trie

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the total parts of the path

I have used the `Trie` data structure to implement the router. The `insert` and `search` operations take `O(n)` time.

Space Complexity is `O(n)` because in the worst case scenario, all the parts of the path are unique. Hence, we have to make `n` parts.