# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        hasCycle = None

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hasCycle = True
                break

        
        if hasCycle:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow

        else:
            return None
                 
