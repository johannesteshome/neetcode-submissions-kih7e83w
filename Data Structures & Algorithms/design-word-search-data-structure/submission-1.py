class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.trie

        for i in range(len(word)):
            if word[i] not in trie.chars:
                trie.chars[word[i]] = TrieNode()
            trie = trie.chars[word[i]]
            if i == len(word) - 1:
                trie.isEndOfWord = True
 
    def search(self, word: str) -> bool:
        trie = self.trie

        def dfs(i, trie):
            
            if i == len(word):
                return trie.isEndOfWord

            if word[i] in trie.chars:
                if dfs(i + 1, trie.chars[word[i]]):
                    return True
            elif word[i] == '.':
                for char in trie.chars:
                    if dfs(i + 1, trie.chars[char]):
                        return True
            
            return False

        return dfs(0, trie)

