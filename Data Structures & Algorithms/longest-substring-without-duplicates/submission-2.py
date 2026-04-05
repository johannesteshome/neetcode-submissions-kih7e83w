class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        Max = float("-inf")

        i = 0
        j = 1
        charSet = set(s[j-1])

        while j < len(s):
            if s[j] in charSet:
                Max = max(Max, j-i)
                charSet.remove(s[i])
                i += 1
            else:
                charSet.add(s[j])
                j += 1
        
        Max = max(Max, j-i)

        return Max
