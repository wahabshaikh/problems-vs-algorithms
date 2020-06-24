# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, args):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        pass

    def insert(self, args):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        pass

    def find(self, args):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pass


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, args):
        # Initialize the node with children as before, plus a handler
        pass

    def insert(self, args):
        # Insert the node as before
        pass