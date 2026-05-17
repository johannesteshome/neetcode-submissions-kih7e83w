class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()       

    def insert(self, word: str) -> None:
        trie = self.trie
        
        for i in range(len(word)):
            char = word[i]
            if char not in trie.chars:
                trie.chars[char] = TrieNode()
            trie = trie.chars[char]
            if i == len(word) - 1:
                trie.isEndOfWord = True
            

    def search(self, word: str) -> bool:
        trie = self.trie
        
        for i in range(len(word)):
            char = word[i]
            if char not in trie.chars:
                return False
            trie = trie.chars[char]
            if i == len(word) - 1:
                return trie.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in trie.chars:
                return False
            trie = trie.chars[char]
            if i == len(prefix) - 1:
                return True
        
        return False
        