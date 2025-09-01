# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for head in lists:
            if head:
                heappush(heap,(head.val,id(head),head))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            val,_,node = heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heappush(heap,(node.next.val,id(node.next),node.next))
        
        return dummy.next