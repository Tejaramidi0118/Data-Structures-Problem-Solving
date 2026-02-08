# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        pos = length - n

        if pos == 0:
            return head.next

        curr = head
        for _ in range(1, pos):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return head
        