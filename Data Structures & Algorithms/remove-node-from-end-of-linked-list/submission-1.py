# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        dummy = head

        while head:
            length += 1
            head = head.next
        
        if length == 1:
            return None
        
        head = dummy

        i = 0
        prev = None
        while head:
            if n == length - i:
                if prev:
                    prev.next = head.next
                    break
                else:
                    dummy = head.next
            i += 1
            prev = head
            head = head.next

        
        return dummy
