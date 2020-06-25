## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

            
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        if len(self.children) == 0:
            return results
            
        for char in self.children:
            results.extend(self.children[char].suffixes(suffix+char))

        return results


def test(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

# Test Case 1
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

test('f')
# OUTPUT:
# un
# unction
# actory

test('b')
# OUTPUT:
# b not found


MyTrie = Trie()
test("Hello")
# OUTPUT:
# Hello not found


# Test Case 3: Mixed character set
MyTrie = Trie()
wordList = [
    "AB de Villiers", "100", "*bold*", "iPhone"
]
for word in wordList:
    MyTrie.insert(word)

test('*')
# OUTPUT:
# bold*

test('i')
# OUTPUT:
# Phone

test('1')
# OUTPUT:
# 00



