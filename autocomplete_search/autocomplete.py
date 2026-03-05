# Autocomplete Search System using Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word into Trie
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    # Collect suggestions
    def suggestions(self, node, prefix, words):

        if node.is_end:
            words.append(prefix)

        for char in node.children:
            self.suggestions(node.children[char], prefix + char, words)

    # Autocomplete function
    def autocomplete(self, prefix):

        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        words = []
        self.suggestions(node, prefix, words)

        return words


# Create Trie
trie = Trie()

# Words database
words = [
    "apple",
    "application",
    "april",
    "banana",
    "ball",
    "bat",
    "cat",
    "car",
    "carbon"
]

# Insert words
for word in words:
    trie.insert(word)

# User input
prefix = input("Enter search text: ")

# Get suggestions
results = trie.autocomplete(prefix)

print("\nSuggestions:")

for word in results:
    print(word)