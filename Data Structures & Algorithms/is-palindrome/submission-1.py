class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        rear = len(s) - 1

        while front < rear:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[rear].isalnum():
                rear -= 1
                continue

            if s[rear].lower() == s[front].lower():
                front += 1
                rear -= 1
            else:
                return False
        
        return True
            