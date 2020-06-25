# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, node):
        # Insert the node as before
        if node not in self.children:
            self.children[node] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for route in path:
            node.insert(route)
            node = node.children[route]

        node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        for route in path:
            if route not in node.children:
                return None
            node = node.children[route]

        return node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler=None, error_404_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)
        self.error_404_handler = error_404_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)

        self.router.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        path = self.split_path(path)

        if len(path) == 0:
            return self.router.handler

        found = self.router.find(path)

        return self.error_404_handler if not found else found

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return [route for route in path.split('/') if route]

# Here are some test cases and expected outputs you can use to test your implementation


# Test Case 1

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# Test Case 2
router = Router("root", "Error 404: Page Not Found")
router.add_handler("/hello", "hello")
router.add_handler("/hello/world", "hello")

print(router.lookup("/"))
# OUTPUT: root

print(router.lookup("/hello"))
# OUTPUT: hello

print(router.lookup("/hello/world"))
# OUTPUT: hello

print(router.lookup("/Hello"))
# OUTPUT: Error 404: Page Not Found


# Test Case 3
router = Router(error_404_handler="Error 404")
print(router.lookup("/"))
# OUTPUT: None

router.add_handler("/", "root")
print(router.lookup("/"))
# OUTPUT: None

router.add_handler("", "root")
print(router.lookup(""))
# OUTPUT: None

router.add_handler("/admin", "admin")
print(router.lookup("/admin"))
# OUTPUT: admin

print(router.lookup("/admin/dashboard"))
# OUTPUT: Error 404



