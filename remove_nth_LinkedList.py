# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create two pointers: slow and fast
        slow = fast = head
        
        # Move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        
        # If the fast pointer reaches the end, remove the first node
        if not fast:
            return head.next
        
        # Move both pointers until the end of the list is reached
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return head
