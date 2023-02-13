# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while prev is not None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
