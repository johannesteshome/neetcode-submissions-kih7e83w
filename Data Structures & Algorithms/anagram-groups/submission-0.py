class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            alphabet = [0 for _ in range(26)]

            for char in word:
                idx = ord(char) - 97
                alphabet[idx] += 1
            
            strRep = " ".join(map(str, alphabet))
            res[strRep].append(word)
        
        return list(res.values())