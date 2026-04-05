class Solution:

    def encode(self, strs: List[str]) -> str:
        stack = []
        encodedStr = ""
        for word in strs:
            length = str(len(word))
            encodedStr += length
            encodedStr += "#"
            encodedStr += word

        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        freq = ""

        while i < len(s):
            if s[i].isdigit():
                freq += s[i]
                i += 1
            elif s[i] == "#":
                length = int(freq)
                i += 1
                decodedStr.append(s[i:i+length])
                i += length
                freq = ""
        
        return decodedStr

